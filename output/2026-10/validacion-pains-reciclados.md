# Validación — Pains reciclados, octubre 2026

## Resultado global: APTO CON CORRECCIONES MENORES (con incidencias menores de voz y longitud pendientes de decisión)

Alcance: `output/2026-10/calendario-pains-reciclados.md` (tabla de calendario + 20 posts). Los bloques "Primer comentario (texto)" de Enrique se han tratado como comentario fijado y no cuentan para longitud ni emojis del post. No hay casos de éxito. No se ha tocado `validacion.md`.

## Correcciones aplicadas automáticamente
- `calendario-pains-reciclados.md` — Los 20 posts no tenían el campo `TEMA` en la cabecera de entrega (PERFIL / FECHA / PILAR / PAIN # / TEMA / FORMATO). Se ha añadido `TEMA:` a los 20, copiando literalmente la columna "Tema / Enfoque" de la tabla. No se ha tocado ningún texto de post.

## Incidencias que requieren decisión del orquestador
- [MENOR] Enrique Saa, 21/10 (pain 15) — Voz: máximo 3 emojis por post ("Nunca usa emojis acumulados... máximo 3") — El post lleva 4: tres ✔️ más el 👇 de la CTA. Opciones: pasar la lista a guiones largos (—), o fusionar dos ítems.
- [MENOR] Emma González, 19/10, 22/10 y 26/10 (pains 5, 10, 19) — Voz: Emma no usa "vosotros" para dirigirse al lector genérico (usa "tú") — Las preguntas de cierre dicen "se os va... deberíais" (19/10), "os preguntan" (22/10) y "os pilló" (26/10). Habría que reescribirlas en tú ("se te va", "te preguntan", "te pilló").
- [MENOR] Cecilio Labrada, 16/10 (pain 11) — Regla 1 de su voz: abrir con frase de menos de 10 palabras o con pregunta con dato — Abre con "En los años que llevo en este sector, he visto muchas transitarias pequeñas que directamente no cotizan." (17 palabras, y es además una credencial en la apertura).
- [MENOR] Cecilio Labrada, 30/10 (pain 14) — Coherencia del texto, no de voz — El texto dice "Pero tiene un coste" (singular) y después "El primero lo paga el recién llegado... El segundo, el veterano", sin antecedente para "primero/segundo". Conviene decir "tiene dos costes" o reformular. Además la escena arranca en "Lunes, primera semana" y se publica un viernes (inocuo).
- [MENOR] Visual Trans, 08/10 (pain 9) — Voz VT: párrafos de máximo 2-3 frases y nunca más de 4 líneas — El tercer párrafo ("Y entonces cuentan la escena...") tiene 5 frases y unas 58 palabras. Conviene partirlo en dos o tres párrafos.
- [MENOR] Enrique Saa, 28/10 (pain 18) — Longitud: rango 150-350 palabras — Unas 144 palabras en el post, sin el comentario. Queda por debajo del mínimo.
- [MENOR] Enrique Saa, 14/10 (pain 13) — Longitud: rango 150-350 palabras — Unas 148 palabras, en el borde inferior. Son 2 menos de lo ideal, así que basta añadir una frase corta.
- [MENOR] Emma González, 13/10, 19/10, 22/10 y 26/10 — Longitud — Salen unas 164, 152, 164 y 154 palabras. La mayoría de sus posts mide 200-400, y el rango 100-180 es el de evento/feria. Estos son posts de reflexión sectorial, así que quedan entre ambos rangos. Se reporta como desviación a decidir, no como error duro.
- [OBSERVACIÓN] Visual Trans, 22/10 y 27/10 — Longitud — Unas 110 y 105 palabras. Voz_VT da 80-180 para posts de personas/clientes y 200-350 para producto o normativa. Los pains no tienen rango propio. Caen en 80-180 y no se considera error, pero 27/10 (OEA, normativo) podría quedar corto. Los otros dos VT (08/10 con 155 y 13/10 con 143) están dentro de 80-180.
- [MENOR] Cifras o datos fuera de `Contexto_Visual_Trans.txt` (afirmaciones de hecho sin respaldo):
  - Laura Díaz, 29/10: "sigue pasando en empresas que facturan millones al año".
  - Laura Díaz, 15/10: "La mayoría de responsables no sabe responder".
  - Visual Trans, 27/10: sostiene que entre los requisitos del estatus OEA hay uno sobre el software. Se alinea con el pain 17, pero `Contexto` no lo recoge. El propio calendario ya avisa de que no se afirma homologación de vForwarding. Eso sí queda bien: no se afirma.
  - Cecilio Labrada, 30/10: "un sector que habla del relevo generacional como uno de sus grandes retos".
  - Emma González, 26/10: "resolver lo urgente en cinco minutos, desde donde estés". Es una promesa de rapidez que implica una capacidad móvil que `Contexto` no menciona (solo habla de acceso desde cualquier ordenador con internet).
  - Enrique Saa, 08/10: cita ICS2 y "Ley de Movilidad Sostenible". ICS2 sale en `Pains_Unificados.txt` y la ley en `Voz_Enrique.txt`, pero no en `Contexto`. Son referencias normativas reales y no cifras.
  - Las cifras restantes son ilustrativas y están declaradas como tales: quince ofertas, 9:15, 17:50, veinte kilómetros, tres días parado, cinco años de licencia. Solo se confirman las de empresa, que salen de `Contexto`: desde 1999 y más de 300 empresas. Conxemar 6-8 oct 2026 y stand están respaldados en `input/eventos/Eventos_Campañas.txt` y `INBOX_procesado.md`.
- [MENOR] Cecilio Labrada, 12/10 — Calendario — El 12 de octubre es fiesta nacional en España (Fiesta Nacional). Es lunes, así que cumple el criterio "lunes-viernes", pero conviene valorar si se publica o se mueve. Mismo aviso para cualquier programación en Metricool.
- [OBSERVACIÓN] Enrique Saa, 14/10 y 21/10 — Regla 1 de voz: abrir con frase de menos de 15 palabras que contenga fecha, hecho inminente o instrucción. Ambas aperturas son afirmaciones de menos de 15 palabras, pero sin fecha ni instrucción. No es incumplimiento de "lo que nunca haría" (no hay pregunta retórica).
- [OBSERVACIÓN] Comentarios fijados de Enrique (14/10 y 28/10) — Llevan 4 ✔️ cada uno. Vale como comentario aparte, pero si se aplica el límite de 3 emojis también a ellos, conviene recortar.
- [OBSERVACIÓN] Textos que usan "oferta/ofertas" (Cecilio 12/10) y "compró" (Enrique 14/10) — Son usos descriptivos del sector (oferta = cotización; compra de licencia pasada), no venta directa. No se marcan.

## Checklist de restricciones absolutas
- [x] Casos de éxito nunca redactados — No aplica: no hay posts de ese pilar en este archivo.
- [ ] Voz respetada en los 5 perfiles — No cumplido del todo: Enrique 21/10 (4 emojis), Emma 19/10, 22/10 y 26/10 ("vosotros"), Cecilio 16/10 (apertura larga), VT 08/10 (párrafo largo). Ningún "nunca haría" duro: no hay pregunta de apertura ni de cierre en Enrique, no hay hashtags en el cuerpo de Laura, no hay "Nos complace".
- [x] Solo días laborables — Las 17 fechas del 08/10 al 30/10 caen de lunes a viernes y los días de la semana de la tabla coinciden con el calendario de octubre de 2026. Nota: el 12/10 es festivo nacional.
- [x] No-solapamiento de pains — Cada pain 1-20 aparece exactamente una vez. En los tres días con 2 posts (08/10, 13/10, 22/10) los pains difieren. Ningún perfil publica en días consecutivos (Enrique 08, 14, 21, 28; Cecilio 12, 16, 23, 30; Laura 09, 15, 20, 29; Emma 13, 19, 22, 26; VT 08, 13, 22, 27). Hecha la verificación contra `Pains_Unificados.txt`: los números y los temas coinciden.
- [x] Sin lenguaje de venta directa — Sin "contrata", "descuento", "compra ahora" ni equivalentes.
- [ ] Longitud dentro de rango por perfil — No cumplido: Enrique 28/10 (~144) y 14/10 (~148) bajo 150, y los 4 posts de Emma por debajo de su rango habitual. Laura (~650-1100 caracteres, rango 300-1700) y Cecilio (~150-190 palabras, rango 100-250 el corto) están dentro. VT dentro de 80-180 salvo la observación anterior.
- [x] Cierres obligatorios respetados — Enrique cierra los 4 con 👇 al primer comentario, en línea propia, sin pregunta; no hay posts de cliente de VT, así que no aplica el "Gracias a... por confiar en Visual Trans". Los cierres de los demás perfiles son de los tipos permitidos (pregunta abierta o remate corto), y los remates finales de VT tienen 12 palabras o menos.
- [x] Hashtags correctos — No hay hashtags en ningún post. No se exigen, ya que solo Laura los usa "cuando los usa".
- [x] Formato de entrega correcto en todos los posts — Tras la corrección, los 20 llevan PERFIL / FECHA / PILAR / PAIN # / TEMA / FORMATO. La fecha va sin año (DD/MM), igual que en el calendario.

Nota sobre los recuentos de palabras: son manuales y pueden desviarse unas 2-4 palabras. Los casos al borde (Enrique 14/10) deben leerse con esa tolerancia.
