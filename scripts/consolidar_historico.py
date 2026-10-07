#!/usr/bin/env python3
"""Consolida exportaciones de LinkedIn (SHIELD) y Metricool en un único histórico de rendimiento.

Uso:
    python3 -I scripts/consolidar_historico.py --salida input/historico/rendimiento_historico.csv \
        --shield export1.csv [export2.csv ...] \
        --metricool "Emma González=ruta.csv" "Cecilio Labrada=ruta.csv" ... "Visual Trans=ruta.csv"

Reglas:
  * Solo posts con texto propio e impresiones > 0 (se descartan reposts sin comentario, 0 impresiones).
  * Si el mismo post está en SHIELD y Metricool, gana Metricool (export más reciente = cifras más maduras).
  * pilar / pain / categoria son INFERIDOS del texto con reglas simples (columna `etiquetas` = inferido).
    No son datos reales: sirven para buscar patrones, nunca como verdad.
  * Rasgos del texto (apertura, cierre, cifras, emojis...) se calculan de forma determinista.
"""
import argparse
import csv
import glob
import re
import unicodedata
from datetime import datetime

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
PERFIL = {"Emma": "Emma González", "Cecilio": "Cecilio Labrada", "Enrique": "Enrique Saa", "Laura": "Laura Díaz"}
FORMATO = {"IMAGE": "imagen", "MULTIIMAGE": "carrusel de imágenes", "VIDEO": "vídeo", "EXTERNAL_VIDEO": "vídeo",
           "DOCUMENT": "documento", "ARTICLE": "enlace/artículo", "TEXT": "solo texto", "POLL": "encuesta",
           "SHARE": "compartido con comentario", "CELEBRATION": "imagen", "EVENT": "evento", "UNKNOWN": "", "": ""}

# --- clasificación inferida --------------------------------------------------------------------
def sin_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn")


RE_CASO = re.compile(r"gracias a .{0,80}por confiar|confiar en (visual trans|nosotros)|\d+ años de confianza|veinte años|20 años|"
                     r"nos comenta|nos cuenta|cuando un cliente habla|ha vuelto a elegir|moderniza su|impulsa la digitalizacion|"
                     r"por confiar en")
RE_EVENTO = re.compile(r"\bferia\b|webinar|congreso|\bsil\b|conxemar|empack|foro aduanero|mesa redonda|stand\b|"
                       r"te esperamos|nos vemos|jornada|directo|inscri|registr|evento|cita imprescindible|encuentro")
RE_NORMA = re.compile(r"5 de octubre|dca\b|e-?cmr|ley \d|ley de movilidad|normativa|reglamento|ics2|obligatori|h1\b|h7\b|"
                      r"declaracion|sancion|aduanas? (de la )?ue|\boea\b|taric|arancel")
RE_DATO = re.compile(r"informe|trimestre|segun (el|los|datos)|estadistic|indice|datos oficiales|\d+(,\d+)?\s?%.*(crece|cae|sube|baja|retroced)|"
                     r"drewry|diario del puerto|barometro|record")
RE_PROD = re.compile(r"tariff code|vforwarding|nueva version|hemos lanzado|acabamos de lanzar|lanzamiento|agentes? de ia|"
                     r"visual trans destinara|1,5 millones|vtrans|nuestra solucion")
RE_PAIN = re.compile(r"manual|transcrip|teclear|doble entrada|mismo dato|copiando y pegando|errores? de|documentacion|"
                     r"soporte|erp|excel|rentabilidad|margen|datos para decidir|clics|expediente|trazabilidad|tarifas|"
                     r"cotiza|cierre mensual|visibilidad|proveedor|licencia|equipo de trafico|buscar documentos|ocr")

PAINS = [  # (nº pain, patrón) — el primero que casa gana
    (4, r"doble entrada|mismo dato|cuatro veces|4 veces|cuatro sistemas|copiando y pegando|introduce el mismo"),
    (3, r"transcrip|introducir datos|teclear|picar|manual(es)?\b|trabajo administrativo|clics|ocr|ia documental|procesar documentos"),
    (5, r"documentacion|gestion documental|buscar documentos|bl de|carpetas"),
    (1, r"rentabilidad|margen por|cuanto gana"),
    (2, r"datos (correctos|enterrados)|decisiones|corazonadas|cierre mensual"),
    (9, r"soporte"),
    (7, r"cambios legales|adaptad[oa] a|sin estar preparado|esta mi software preparado"),
    (8, r"erp generalista|herramientas no|no hablan|no habla con|sistemas (que )?no se"),
    (10, r"trazabilidad|seguimiento de (una )?mercancia"),
    (12, r"tarifas"),
    (16, r"trayectoria|veinte anos|20 anos|confianza"),
    (17, r"\boea\b"),
]


def clasifica(texto, fmt):
    t = sin_acentos(texto)
    cat = "institucional/otros"
    if RE_CASO.search(t):
        cat = "caso_exito"
    elif RE_EVENTO.search(t) and not RE_PAIN.search(t[:200]):
        cat = "evento"
    elif RE_PROD.search(t) and len(t) < 1400 and re.search(r"lanz|nueva|acaba de|2\.0|mejora|83,87|1,5 millones", t):
        cat = "producto"
    elif RE_NORMA.search(t) and re.search(r"5 de octubre|ley|normativa|obligatori|dca|e-?cmr|h1|h7|ics2|reglamento", t):
        cat = "normativa"
    elif RE_DATO.search(t):
        cat = "dato_sector"
    elif RE_PAIN.search(t):
        cat = "pain"
    pilar = {"caso_exito": "Casos de éxito", "evento": "Noticias", "normativa": "Noticias", "dato_sector": "Noticias",
             "pain": "Pains", "producto": "Otro", "institucional/otros": "Otro"}[cat]
    pain = ""
    if cat == "pain":
        for n, pat in PAINS:
            if re.search(pat, t):
                pain = str(n)
                break
    return cat, pilar, pain


# --- rasgos del texto -------------------------------------------------------------------------------
RE_EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⏳✅❌]")


def rasgos(texto):
    t = texto.strip()
    lineas = [l for l in t.split("\n") if l.strip()]
    primera = lineas[0].strip() if lineas else ""
    ultima = lineas[-1].strip() if lineas else ""
    apertura = ("pregunta" if primera.startswith(("¿", "Y si", "Cuánto")) or primera.endswith("?")
                else "cifra" if re.match(r"^[\d\"“]*\d", primera) or re.search(r"\d+([.,]\d+)?\s?%", primera[:60])
                else "escena/frase corta" if len(primera) < 70
                else "afirmación larga")
    cierre = ("pregunta" if ultima.endswith("?") or "¿" in ultima
              else "CTA comentarios" if re.search(r"comentario|👇|enlace", ultima, re.I)
              else "frase" if ultima else "")
    return {
        "primera_linea_car": len(primera),
        "apertura": apertura,
        "cierre": cierre,
        "n_parrafos": len(lineas),
        "tiene_cifra": "sí" if re.search(r"\d", t) else "no",
        "n_emojis": len(RE_EMOJI.findall(t)),
        "tiene_enlace": "sí" if re.search(r"https?://", t) else "no",
        "menciona": "sí" if re.search(r"@\w|@\[", t) else "no",
        "aqui_viene_lo_brutal": "sí" if "lo brutal" in t.lower() else "no",
    }


# --- lectura de fuentes ----------------------------------------------------------------------------
def num(v):
    try:
        v = str(v).strip().replace(",", ".")
        return float(v) if v else None
    except ValueError:
        return None


def clave(texto):
    return re.sub(r"\W+", "", sin_acentos(texto))[:90]


def registro(perfil, fecha, texto, tipo, imp, reac, com, comp, clics, fuente):
    inter = sum(x or 0 for x in (reac, com, comp))
    return {"perfil": perfil, "dt": fecha, "texto": texto, "tipo": tipo, "imp": imp, "inter": inter, "clics": clics,
            "fuente": fuente}


def leer_shield(rutas):
    vistos = {}
    for patron in rutas:
        for ruta in glob.glob(patron):
            with open(ruta, encoding="utf-8", newline="") as f:
                for r in csv.DictReader(f):
                    if not r["text"].strip():
                        continue
                    imp = num(r["numImpressions"])
                    if not imp:
                        continue
                    perfil = PERFIL.get(r["firstName"])
                    if not perfil:
                        continue
                    dt = datetime.fromisoformat(r["createdAt (TZ=Europe/Madrid)"])
                    vistos[r["urn"]] = registro(perfil, dt, r["text"], r["type"], imp, num(r["numReactions"]),
                                                num(r["numComments"]), num(r["numShares"]), None, "linkedin")
    return list(vistos.values())


def leer_metricool(perfil, ruta):
    out = []
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f, delimiter=";"):
            imp = num(r["Impressions"])
            if not r["Title"].strip() or not imp:
                continue
            out.append(registro(perfil, datetime.strptime(r["Date"], "%Y-%m-%d %H:%M"), r["Title"], r["Type"], imp,
                                num(r["Reactions"]), num(r["Comments"]), num(r["Shares"]), num(r.get("Clicks", "")),
                                "metricool"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shield", nargs="*", default=[])
    ap.add_argument("--metricool", nargs="*", default=[], help='"Perfil=ruta.csv"')
    ap.add_argument("--salida", required=True)
    ap.add_argument("--enriquecer", default="", help="CSV con columna `texto` (p. ej. un rendimiento.csv mensual): añade los rasgos del texto y escribe --salida")
    a = ap.parse_args()

    if a.enriquecer:
        with open(a.enriquecer, encoding="utf-8", newline="") as f:
            filas = list(csv.DictReader(f))
        nuevas = list(rasgos("x").keys())
        campos = list(filas[0].keys()) + [c for c in nuevas if c not in filas[0]]
        with open(a.salida, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=campos)
            w.writeheader()
            for r in filas:
                r.update({k: v for k, v in rasgos(r.get("texto", "")).items()})
                w.writerow(r)
        print(f"Enriquecidas {len(filas)} filas")
        return

    recs = leer_shield(a.shield)
    n_shield = len(recs)
    met = []
    for par in a.metricool:
        perfil, ruta = par.split("=", 1)
        met += leer_metricool(perfil, ruta)

    # dedupe: Metricool sustituye al SHIELD si es el mismo post (mismo perfil, mismo texto, ±2 días)
    idx = {}
    for i, r in enumerate(recs):
        idx.setdefault((r["perfil"], clave(r["texto"])), []).append(i)
    reemplazos = nuevos = 0
    descartar = set()
    for m in met:
        hit = [i for i in idx.get((m["perfil"], clave(m["texto"])), []) if abs((recs[i]["dt"] - m["dt"]).days) <= 2]
        if hit:
            descartar.update(hit)
            reemplazos += 1
        else:
            nuevos += 1
    final = [r for i, r in enumerate(recs) if i not in descartar] + met
    # elimina duplicados exactos dentro de Metricool
    uniq = {}
    for r in final:
        uniq[(r["perfil"], clave(r["texto"]), r["dt"].date())] = r
    final = sorted(uniq.values(), key=lambda r: (r["perfil"], r["dt"]))

    cols = ["id_post", "fecha", "dia_semana", "hora", "perfil", "pilar", "pain", "formato", "longitud", "impresiones",
            "interacciones", "clics", "engagement_rate", "categoria", "primera_linea_car", "apertura", "cierre",
            "n_parrafos", "tiene_cifra", "n_emojis", "tiene_enlace", "menciona", "aqui_viene_lo_brutal",
            "fuente", "etiquetas", "texto"]
    with open(a.salida, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for i, r in enumerate(final, 1):
            cat, pilar, pain = clasifica(r["texto"], r["tipo"])
            row = {
                "id_post": f"H{i:04d}", "fecha": r["dt"].strftime("%Y-%m-%d"), "dia_semana": DIAS[r["dt"].weekday()],
                "hora": r["dt"].hour, "perfil": r["perfil"], "pilar": pilar, "pain": pain,
                "formato": FORMATO.get(r["tipo"], ""), "longitud": len(r["texto"].strip()),
                "impresiones": int(r["imp"]), "interacciones": int(r["inter"]),
                "clics": "" if r["clics"] is None else int(r["clics"]),
                "engagement_rate": round(r["inter"] / r["imp"], 4), "categoria": cat,
                "fuente": r["fuente"], "etiquetas": "inferido", "texto": r["texto"].strip(),
            }
            row.update(rasgos(r["texto"]))
            w.writerow(row)
    print(f"SHIELD: {n_shield} | Metricool: {len(met)} (sustituyen {reemplazos}, nuevos {nuevos}) | total: {len(final)}")


if __name__ == "__main__":
    main()
