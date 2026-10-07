# Aprendizajes de calendario

Los lee `agente-calendario`. Los escribe `agente-aprendizajes` el día 1 de cada mes, a partir de
`output/AAAA-MM/rendimiento.csv` y de `input/historico/rendimiento_historico.csv`. Es un documento
acumulativo: no se sobrescribe, se añade evidencia.

**Son sugerencias, nunca mandan sobre lo fijo** (reparto de pilares 60/30/10, cadencia por perfil,
no-solapamiento de pains, días laborables). Si un dato choca con una regla fija, se anota como
observación y no se aplica.

Niveles de confianza: `hipótesis` (señal débil, pocos posts o sin pasar la corrección estadística),
`probable` (efecto claro y en el mismo sentido en casi todos los perfiles), `confirmado` (se mantiene
4 o más meses seguidos o lo valida un experimento).

## Base de partida (primera carga, 6-oct-2026)

Histórico de 348 posts desde julio de 2025 (Cecilio desde abril de 2025): empresa 80, Emma 88,
Laura 68, Cecilio 59, Enrique 53. Análisis completo en `input/historico/analisis_2026-10-06.md`.
Pilar, categoría y pain de esos posts son **inferidos** del texto (revisados por IA), no datos reales;
459 etiquetados, de los que 40 con confianza baja. Medianas de impresiones por perfil: empresa 960,
Emma 919, Cecilio 702, Laura 574, Enrique 443. Todo lo que sigue se mide como índice sobre la mediana
de cada perfil (1,00 = normal para ese perfil).

## Aprendizajes vigentes

- **A-01 · Volumen y objetivo de 100.000** — El alcance mensual depende sobre todo del número de posts:
  octubre de 2025 tuvo 63 posts y 88.057 impresiones; el resto de meses con 11-29 posts quedó entre
  8.700 y 48.000. La media por post es 1.106 y la mediana 762; el 10 % de posts mejores aporta el 36 %
  del alcance (hay pocos posts muy virales). Confianza: `probable`. Evidencia: 2025-04 a 2026-10, n=348.
  Acción: no recortar la cadencia de 65-70 posts; con la media actual, ~90 posts/mes llegarían a 100.000,
  así que el objetivo exige también subir la mediana (ver A-02 a A-06).
- **A-02 · Normativa rinde por encima de la media en alcance** — Posts de normativa (DCA, e-CMR, 5 de
  octubre): índice 1,38 (+40 % frente al resto, IC90 % +0,04 a +0,57, p=0,016; mismo sentido en 4 de 5
  perfiles). Más fuerte en Cecilio (2,66, n=5), Enrique (1,47) y Emma (1,38). Su engagement es menor
  (0,78, señal estadística): llega mucho, comentan poco. Confianza: `probable`. Vigencia: **revisar en
  noviembre**, la obligación del DCA entró en vigor el 5 de octubre de 2026 y el tema puede enfriarse.
  Acción: mantener normativa como ángulo prioritario de Noticias en Cecilio, Enrique y Emma.
- **A-03 · Los posts de eventos pesan mucho y alcanzan poco** — Son 83 de 348 posts (24 %), con índice 0,97
  de alcance (Cecilio 0,50, Enrique 0,62) pero el mejor engagement (+41 %, señal, 5/5 perfiles): conversan
  los contactos cercanos, no llega a audiencia nueva. Confianza: `probable`. Acción: limitar a una previa y
  un resumen por evento; en Cecilio y Enrique evitar los resúmenes de feria como contenido principal.
- **A-04 · Curiosidad concreta con producto Tariff Code** — Los 27 posts que mencionan Tariff Code
  tienen índice 1,65 frente a 0,98 del resto (p=0,004). Los tres mayores éxitos con ese gancho
  (producto cotidiano + dos códigos arancelarios + diferencia en euros) llegaron a 52×, 10× y 3,7× la
  mediana de su perfil. Confianza: `hipótesis` (n=3 con ese gancho exacto, efecto enorme).
  Acción: reservar 1 o 2 posts al mes por perfil con ese gancho, dentro del pilar Pains o Noticias
  (no como pilar nuevo). Ver experimento E-R2.
- **A-05 · Datos sorprendentes del sector > resúmenes de informe** — Los posts de `dato_sector` tienen el
  alcance más bajo (0,80, 4/5 perfiles), pero los dos que más alcanzaron fueron datos curiosos de
  contenedores (96 % fabricados por 3 empresas: 23,5×; 24 % de contenedores vacíos: 12,8×). Los
  resúmenes de informes trimestrales rindieron ~0,7-0,9. Confianza: `hipótesis`. Acción: en
  Noticias, preferir un único dato llamativo con "y por qué te afecta" antes que un resumen de informe.
- **A-06 · Formato: evitar el enlace/artículo directo; carrusel y vídeo sobresalen** — Enlace/artículo:
  índice 0,82 (n=32; Cecilio 0,55, Enrique 0,59); en septiembre de 2026, 11 posts con formato enlace
  tuvieron mediana de 284 impresiones frente a 902 del resto. Compartido con comentario: 0,66 (3/3
  perfiles). Vídeo: 1,12 (4/5 perfiles; Cecilio 1,82, Emma 1,48). Carrusel: 1,74 (n=21, p=0,003, sin
  pasar la corrección estadística; casi todo de la empresa, 1,26). Confianza: `probable` (enlace),
  `hipótesis` (carrusel, vídeo). Acción: no publicar enlace de artículo como formato principal de un
  post; usar imagen/vídeo/carrusel con el enlace en el primer comentario.
- **A-07 · Pains: el soporte (#9) destaca, la doble entrada (#4) flojea** — Pain #9: 1,39 (n=9);
  #4: 0,72 (n=10); el conjunto de Pains está en la media (0,98). Muestras pequeñas, sin significación.
  Confianza: `hipótesis`. Acción: ninguna por ahora; se probará con experimento al crecer la muestra.
- **A-08 · Día y hora: sin evidencia firme** — Viernes +13 % y jueves -14 % van en el mismo sentido en
  los 5 perfiles, pero sin significación (p=0,18 y 0,14). El 76 % de los posts sale antes de las 11:00;
  mediodía +12 % sin significación (n=58). Confianza: `hipótesis`. Acción: no mover días; ver E-C1.
- **A-09 · El mismo texto en dos perfiles el mismo día** — En 3 casos de texto repetido el mismo día, uno
  de los dos se hundió (p. ej., 26 impresiones frente a 1.071). Con separación de semanas, el rendimiento
  es igual (1,04 frente a 1,06; 12 textos). Confianza: `hipótesis` (n=3). Acción: reutilizar ángulos
  entre perfiles, pero separados al menos 7 días; nunca el mismo texto el mismo día.

## Experimentos activos

- **E-C1 · Hora de publicación** — A: mañana (antes de 10:00) frente a B: 12:00-13:30, mismo perfil, mismo
  pilar. Asignación: 4 posts por brazo repartidos entre Emma, Laura y la empresa (n=8 por brazo).
  Métrica: índice de impresiones. Éxito: B supera a A en más de un 15 % y el IC90 % no cruza 0.
  Estado: `propuesto` (arranca en el siguiente calendario).
- **E-C2 · Carrusel frente a imagen en pains de la empresa** — A: carrusel; B: imagen única; mismo pain.
  4 posts por brazo. Métrica: índice de impresiones. Éxito: A supera a B en más de un 20 %.
  Estado: `propuesto`.

## Experimentos cerrados

_Ninguno._

## Observaciones que chocan con reglas fijas (no se aplican)

_Ninguna por ahora. A vigilar: los eventos suponen el 24 % de los posts dentro del pilar Noticias; no
choca con el reparto 60/30/10, pero conviene que no copen el pilar (ver A-03)._

## Historial de actualizaciones

- 2026-10-06: carga inicial del histórico (348 posts, 5 perfiles). Aprendizajes A-01 a A-09 y
  experimentos E-C1, E-C2.
