# visualtrans-linkedin

Datos del **agente de contenido LinkedIn de Visual Trans / Visual MS**: empresa española de software B2B para logística y aduanas (eCMR, DUA, Intrastat, ICS2, AEAT, Verifactu).

El agente genera cada mes el calendario editorial de LinkedIn (~65-70 posts en 5 perfiles) con un único punto de validación humana. Objetivo de negocio: **100.000 impresiones/mes**.

Este repo contiene solo los **datos** (lo que el agente lee y lo que produce). La definición de los agentes y del comando vive en `arivas-web/visualtrans-agentes` (`.claude/agents/linkedin/` y `.claude/commands/pipeline-mensual.md`).

---

## Cómo funciona

Se lanza con un solo comando:

```
/pipeline-mensual octubre 2026
```

Una orquestación de subagentes, cada uno con una responsabilidad única, recorre estas fases:

| Fase | Agente | Qué hace |
|---|---|---|
| 0 | `agente-archivista` | Lee `input/inbox/INBOX.md`, clasifica cada línea y la vuelca al archivo de `input/` que le corresponde. Las entradas procesadas pasan a `INBOX_procesado.md`. |
| 1 | `agente-investigador` | Investiga tendencias, normativas y ferias del mes y decide el **pain prioritario**. Escribe `briefing.md`. |
| 2 | `agente-calendario` | Construye el calendario aplicando los pilares y las reglas de no-solapamiento. Lo envía como Google Sheets por correo. |
| 2 | **Validación humana** | **Única pausa del pipeline.** Se valida el calendario en el chat. Hasta entonces no se redacta nada. |
| 3 | `agente-redactor` | Redacta los posts. Se invoca 5 veces en paralelo, una por perfil, cada una con su documento de voz. |
| 3.5 | `agente-presentacion` | Genera un .pptx con un post por diapositiva para revisión visual (auxiliar, no bloquea). |
| 4 | `agente-validador` | Comprueba el resultado final contra las restricciones absolutas. Escribe `validacion.md`. |
| 4.5 | **Aprobación humana** | Se aprueban los posts ya validados. Al aprobar se crea `output/AAAA-MM/APROBADO.md`. |

Todo lo demás es autónomo. Las decisiones que antes requerían confirmación quedan registradas en `log-decisiones.md`, para auditar *después*, sin bloquear la ejecución.

---

## Estructura del repo

```
input/                              ← lo que LEE la IA
├── inbox/
│   ├── INBOX.md                    ← único archivo que se edita a mano
│   └── INBOX_procesado.md          ← histórico de entradas ya incorporadas (nunca se borra)
├── empresa/
│   ├── Contexto_Visual_Trans.txt   ← productos, propuesta de valor, argumentario
│   └── Pains_Unificados.txt        ← pains numerados con descripción completa
├── eventos/
│   └── Eventos_Campañas.txt        ← ferias, webinars, lanzamientos, normativas con fecha, campañas
└── voces/
    ├── Voz_VT.txt                  ← empresa (página de Visual Trans)
    ├── Voz_Ceci.txt                ← Cecilio Labrada
    ├── Voz_Emma.txt                ← Emma González
    ├── Voz_Enrique.txt             ← Enrique Saa
    └── Voz_Laura.txt               ← Laura Díaz

output/                             ← lo que GENERA la IA, un directorio por mes
└── AAAA-MM/
    ├── briefing.md                 ← investigación del mes y pain prioritario
    ├── calendario.md               ← calendario completo
    ├── posts/[perfil].md           ← posts redactados, uno por perfil
    ├── validacion.md               ← informe del agente-validador
    ├── log-decisiones.md           ← auditoría de decisiones autónomas
    └── APROBADO.md                 ← solo existe tras la aprobación humana
```

**Regla de oro:** `input/` es la fuente de verdad que lee el agente; `output/` es siempre regenerable. Nunca se escribe a mano en `output/`.

---

## Tu único trabajo manual: `input/inbox/INBOX.md`

Escribe ahí, cuando quieras, cualquier cosa suelta: una noticia, un evento nuevo, un cambio de tono para un perfil, un pain nuevo, una campaña que se activa, un caso de éxito disponible. No hay formato obligatorio, solo la fecha delante:

```
- 2026-09-22: [texto libre]
```

En la siguiente ejecución, el archivista la clasifica y la incorpora a `empresa/`, `eventos/` o `voces/`. Las entradas ambiguas o que contradicen una regla existente **no se descartan**: quedan como "requiere revisión" en el `log-decisiones.md` del mes y el pipeline continúa.

---

## Reglas de negocio

- **Pilares:** 60 % Noticias · 30 % Pains · 10 % Casos de éxito.
- **Casos de éxito:** nunca se redactan. Solo se reserva el hueco `CASO DE ÉXITO — pendiente Adrián`.
- **No-solapamiento de pains:**
  - nunca el mismo pain el mismo día en dos perfiles;
  - nunca en días consecutivos en el mismo perfil;
  - máximo 2 apariciones por pain al mes.
- **Restricciones absolutas:**
  - nunca lenguaje de venta directa;
  - solo días laborables;
  - cierres obligatorios por perfil;
  - la voz nunca se improvisa ni se mezcla entre perfiles. Cada post sigue su `Voz_*.txt`.

---

## Después de la aprobación

Crear `output/AAAA-MM/APROBADO.md` y hacer push a `main` es lo único que dispara la entrega a gráficas: un workflow de GitHub Actions avisa al repo del equipo de gráficas (`repository_dispatch`, evento `posts-aprobados`) con las rutas del calendario, los posts y la validación. Ese equipo genera las imágenes con Magnific y publica en Metricool.

---

## Notas para el agente

- Los agentes leen los archivos con **rutas relativas desde la raíz del repo**, p. ej. `Read input/voces/Voz_Ceci.txt`.
- Cada subagente lee lo que necesita en tiempo de ejecución. No hay copias duplicadas de las reglas: si cambia una regla, se cambia en su archivo de `input/`.
- Nunca usar `--force` ni `--no-verify`, ni reescribir historia ajena. El pipeline hace commit y push a `main` tras cada fase sin pedir confirmación. Las únicas pausas son las dos de contenido (calendario y posts).
- Los textos históricos dentro de `output/2026-10/` citan las rutas antiguas (`Voz_Laura.txt`, `Pains_Unificados.txt`…), anteriores a la reorganización en `input/`.
