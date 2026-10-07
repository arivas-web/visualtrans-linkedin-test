#!/usr/bin/env python3
"""Análisis estadístico del rendimiento de los posts de LinkedIn (solo librería estándar).

Uso:
    python3 -I scripts/analizar_rendimiento.py --corte AAAA-MM-DD [--salida ruta.md] rendimiento1.csv [rendimiento2.csv ...]

Qué hace:
  * Normaliza las impresiones de cada post por la mediana de su perfil (índice relativo al perfil),
    para poder comparar la página de empresa con los perfiles personales.
  * Excluye posts inmaduros (publicados menos de --madurez días antes del corte) y filas sin datos.
  * Por cada dimensión (pilar, pain, formato, día, hora, longitud, perfil) compara cada grupo con el
    resto con un test de permutación sobre la mediana, y corrige las comparaciones múltiples (FDR de
    Benjamini-Hochberg). Solo marca como señal lo que pasa n mínimo, tamaño de efecto y FDR.
  * Detecta atípicos (posts virales o hundidos) y los separa para que no distorsionen.
  * Correlación de Spearman entre longitud e índice, y evolución mensual.
Nunca inventa datos: las celdas vacías se ignoran y se cuentan.
"""
import argparse
import csv
import random
import statistics as st
from datetime import date, datetime, timedelta

MIN_N = 4          # tamaño mínimo de grupo para concluir algo
MIN_EFECTO = 0.15  # diferencia mínima de mediana del índice (15 %) para considerarla relevante
FDR_Q = 0.10       # tasa de falsos descubrimientos admitida
PERMS = 5000
random.seed(7)

DIMS = ["pilar", "pain", "formato", "dia_semana", "perfil", "hora_tramo", "longitud_tramo"]


def num(v):
    try:
        return float(str(v).strip().replace(",", ".")) if str(v).strip() != "" else None
    except ValueError:
        return None


def parse_fecha(v):
    v = (v or "").strip()
    if "/" in v:
        try:
            return datetime.strptime(v[:10], "%d/%m/%Y")
        except ValueError:
            return None
    try:
        return datetime.fromisoformat(v.replace("Z", "")[:19])
    except ValueError:
        return None


def tramo_hora(h):
    h = num(h)
    if h is None:
        return ""
    h = int(h)
    return "mañana(<11)" if h < 11 else "mediodía(11-14)" if h < 14 else "tarde(>=14)"


def cargar(rutas):
    filas = []
    for r in rutas:
        with open(r, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                row["_origen"] = r
                filas.append(row)
    return filas


def percentil(xs, p):
    xs = sorted(xs)
    if not xs:
        return None
    k = (len(xs) - 1) * p
    lo, hi = int(k), min(int(k) + 1, len(xs) - 1)
    return xs[lo] + (xs[hi] - xs[lo]) * (k - lo)


def perm_test(a, b):
    """p bilateral del test de permutación sobre la diferencia de medianas."""
    obs = abs(st.median(a) - st.median(b))
    pool = a + b
    na = len(a)
    ge = 0
    for _ in range(PERMS):
        random.shuffle(pool)
        if abs(st.median(pool[:na]) - st.median(pool[na:])) >= obs - 1e-12:
            ge += 1
    return (ge + 1) / (PERMS + 1)


def boot_ic(a, b):
    """IC 90 % bootstrap de la diferencia de medianas (a - b)."""
    ds = []
    for _ in range(1500):
        ra = [random.choice(a) for _ in a]
        rb = [random.choice(b) for _ in b]
        ds.append(st.median(ra) - st.median(rb))
    return percentil(ds, 0.05), percentil(ds, 0.95)


def rangos(xs):
    orden = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(orden):
        j = i
        while j + 1 < len(orden) and xs[orden[j + 1]] == xs[orden[i]]:
            j += 1
        for k in range(i, j + 1):
            r[orden[k]] = (i + j) / 2 + 1
        i = j + 1
    return r


def spearman(x, y):
    if len(x) < 5:
        return None, None
    rx, ry = rangos(x), rangos(y)
    def corr(a, b):
        ma, mb = st.mean(a), st.mean(b)
        num_ = sum((p - ma) * (q - mb) for p, q in zip(a, b))
        den = (sum((p - ma) ** 2 for p in a) * sum((q - mb) ** 2 for q in b)) ** 0.5
        return num_ / den if den else 0.0
    rho = corr(rx, ry)
    ge = 0
    ys = ry[:]
    for _ in range(PERMS):
        random.shuffle(ys)
        if abs(corr(rx, ys)) >= abs(rho) - 1e-12:
            ge += 1
    return rho, (ge + 1) / (PERMS + 1)


def bh(pvals, q):
    """Benjamini-Hochberg: devuelve el conjunto de índices que pasan el FDR."""
    m = len(pvals)
    orden = sorted(range(m), key=lambda i: pvals[i])
    corte = -1
    for rank, i in enumerate(orden, 1):
        if pvals[i] <= q * rank / m:
            corte = rank
    return {orden[k] for k in range(corte)} if corte > 0 else set()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="+")
    ap.add_argument("--corte", required=True, help="fecha de corte AAAA-MM-DD (último día con datos)")
    ap.add_argument("--madurez", type=int, default=7, help="días mínimos desde la publicación")
    ap.add_argument("--salida", default="")
    a = ap.parse_args()

    corte = datetime.strptime(a.corte, "%Y-%m-%d")
    filas = cargar(a.csv)
    total = len(filas)
    sin_datos = inmaduros = 0
    posts = []
    for r in filas:
        imp = num(r.get("impresiones"))
        fecha = parse_fecha(r.get("fecha"))
        if imp is None or imp <= 0 or fecha is None:
            sin_datos += 1
            continue
        if fecha > corte - timedelta(days=a.madurez):
            inmaduros += 1
            continue
        inter, clics = num(r.get("interacciones")), num(r.get("clics"))
        er = num(r.get("engagement_rate"))
        if er is None and inter is not None:
            er = inter / imp
        if er is not None and er > 1:   # venía en porcentaje
            er = er / 100
        longitud = num(r.get("longitud"))
        posts.append({
            "id": r.get("id_post", ""), "fecha": fecha, "mes": fecha.strftime("%Y-%m"),
            "perfil": r.get("perfil", ""), "pilar": r.get("pilar", ""), "pain": r.get("pain", ""),
            "formato": r.get("formato", ""), "dia_semana": r.get("dia_semana", ""),
            "hora_tramo": tramo_hora(r.get("hora")), "imp": imp, "inter": inter, "clics": clics,
            "er": er, "longitud": longitud,
        })

    out = []
    w = out.append
    w(f"# Análisis de rendimiento (corte {a.corte})\n")
    w(f"- Filas leídas: {total}. Usadas: {len(posts)}. Sin datos: {sin_datos}. Inmaduras (<{a.madurez} días): {inmaduros}.")
    if len(posts) < 12:
        w("- ⚠️ Muestra muy pequeña (<12 posts): todo lo que sigue es exploratorio.")

    # índice relativo al perfil
    por_perfil = {}
    for p in posts:
        por_perfil.setdefault(p["perfil"], []).append(p["imp"])
    base = {k: st.median(v) for k, v in por_perfil.items()}
    for p in posts:
        p["idx"] = p["imp"] / base[p["perfil"]] if base[p["perfil"]] else None
    w("\n## Línea base por perfil (mediana de impresiones)\n")
    w("| Perfil | n | Mediana impresiones | Mediana engagement |")
    w("|---|---|---|---|")
    for k, v in sorted(por_perfil.items()):
        ers = [p["er"] for p in posts if p["perfil"] == k and p["er"] is not None]
        w(f"| {k} | {len(v)} | {st.median(v):.0f} | {st.median(ers):.2%} |" if ers else f"| {k} | {len(v)} | {st.median(v):.0f} | – |")

    # tramos de longitud (terciles)
    ls = [p["longitud"] for p in posts if p["longitud"] is not None]
    if len(ls) >= 9:
        t1, t2 = percentil(ls, 1 / 3), percentil(ls, 2 / 3)
        for p in posts:
            L = p["longitud"]
            p["longitud_tramo"] = "" if L is None else f"corto(<={t1:.0f})" if L <= t1 else f"medio({t1:.0f}-{t2:.0f})" if L <= t2 else f"largo(>{t2:.0f})"
    else:
        for p in posts:
            p["longitud_tramo"] = ""

    # comparaciones grupo vs resto
    tests = []
    for dim in DIMS:
        grupos = {}
        for p in posts:
            if p[dim]:
                grupos.setdefault(p[dim], []).append(p)
        if len(grupos) < 2:
            continue
        for g, ps in grupos.items():
            resto = [p["idx"] for p in posts if p[dim] and p[dim] != g and p["idx"] is not None]
            ga = [p["idx"] for p in ps if p["idx"] is not None]
            if len(ga) < MIN_N or len(resto) < MIN_N:
                tests.append({"dim": dim, "g": g, "n": len(ga), "insuf": True})
                continue
            efecto = st.median(ga) - st.median(resto)
            p_ = perm_test(ga, resto)
            lo, hi = boot_ic(ga, resto)
            ers = [p["er"] for p in ps if p["er"] is not None]
            tests.append({"dim": dim, "g": g, "n": len(ga), "med": st.median(ga), "efecto": efecto,
                          "p": p_, "ic": (lo, hi), "er": st.median(ers) if ers else None, "insuf": False})
    validos = [t for t in tests if not t["insuf"]]
    pasan = bh([t["p"] for t in validos], FDR_Q)
    for i, t in enumerate(validos):
        t["senal"] = (i in pasan) and abs(t["efecto"]) >= MIN_EFECTO and not (t["ic"][0] <= 0 <= t["ic"][1])

    w(f"\n## Comparaciones (índice = impresiones / mediana del perfil; 1.00 = normal para ese perfil)\n")
    w(f"Criterio de señal: n≥{MIN_N} en ambos lados, |efecto|≥{MIN_EFECTO:.0%}, FDR q={FDR_Q} y IC90 % sin cruzar 0. "
      "El resto es ruido hasta que haya más datos.\n")
    w("| Dimensión | Grupo | n | Índice mediano | Efecto vs resto | IC90 % | p | Eng. mediano | Señal |")
    w("|---|---|---|---|---|---|---|---|---|")
    for t in sorted(validos, key=lambda t: (t["dim"], -t["med"])):
        er = f"{t['er']:.2%}" if t["er"] is not None else "–"
        w(f"| {t['dim']} | {t['g']} | {t['n']} | {t['med']:.2f} | {t['efecto']:+.2f} | [{t['ic'][0]:+.2f}, {t['ic'][1]:+.2f}] | {t['p']:.3f} | {er} | {'**SÍ**' if t['senal'] else 'no'} |")
    insuf = [t for t in tests if t["insuf"]]
    if insuf:
        w("\n**Muestra insuficiente (n<%d), no se concluye:** " % MIN_N + ", ".join(f"{t['dim']}={t['g']} (n={t['n']})" for t in insuf))

    # longitud
    pares = [(p["longitud"], p["idx"]) for p in posts if p["longitud"] is not None and p["idx"] is not None]
    rho, pr = spearman([x for x, _ in pares], [y for _, y in pares])
    w("\n## Longitud vs índice (Spearman)\n")
    w(f"- ρ = {rho:+.2f}, p = {pr:.3f} (n={len(pares)})" if rho is not None else "- Muestra insuficiente (n<5).")

    # atípicos
    idxs = [p["idx"] for p in posts]
    if len(idxs) >= 8:
        q1, q3 = percentil(idxs, .25), percentil(idxs, .75)
        alto, bajo = q3 + 1.5 * (q3 - q1), q1 - 1.5 * (q3 - q1)
        at = [p for p in posts if p["idx"] > alto or p["idx"] < bajo]
        w("\n## Atípicos (no se usan como evidencia de patrón; se estudian aparte)\n")
        w("\n".join(f"- {p['id']} ({p['perfil']}, {p['pilar']}, {p['pain']}, {p['formato']}, {p['dia_semana']}): índice {p['idx']:.2f}" for p in at) or "- Ninguno.")

    # top / bottom
    orden = sorted(posts, key=lambda p: -p["idx"])
    k = min(5, len(orden) // 2)
    if k:
        w("\n## Mejores y peores posts (para análisis cualitativo del texto)\n")
        w("**Top:**")
        w("\n".join(f"- {p['id']} · {p['perfil']} · {p['pilar']} · {p['pain']} · {p['formato']} · {p['dia_semana']} · {p['longitud']} car. · índice {p['idx']:.2f}" for p in orden[:k]))
        w("\n**Bottom:**")
        w("\n".join(f"- {p['id']} · {p['perfil']} · {p['pilar']} · {p['pain']} · {p['formato']} · {p['dia_semana']} · {p['longitud']} car. · índice {p['idx']:.2f}" for p in orden[-k:]))

    # evolución
    meses = sorted({p["mes"] for p in posts})
    if len(meses) > 1:
        w("\n## Evolución mensual\n")
        w("| Mes | n | Impresiones totales | Mediana por post |")
        w("|---|---|---|---|")
        for m in meses:
            ps = [p["imp"] for p in posts if p["mes"] == m]
            w(f"| {m} | {len(ps)} | {sum(ps):.0f} | {st.median(ps):.0f} |")

    texto = "\n".join(out) + "\n"
    if a.salida:
        with open(a.salida, "w", encoding="utf-8") as f:
            f.write(texto)
    print(texto)


if __name__ == "__main__":
    main()
