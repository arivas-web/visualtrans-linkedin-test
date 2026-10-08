# INBOX

Bandeja de entrada de texto libre. Escribe aquí cualquier cosa suelta que se te
ocurra: una noticia, un evento nuevo, un cambio de tono para algún perfil, un pain
nuevo, una campaña que se activa, un caso de éxito disponible, etc.

No hay formato obligatorio. Basta con una línea con fecha delante, así:

```
- 2026-09-22: [texto libre]
```

En cada ejecución del pipeline (`/pipeline-mensual`), el **agente-archivista** lee
este archivo completo, clasifica cada entrada, la incorpora al archivo estructurado
que le corresponde (`input/empresa/Contexto_Visual_Trans.txt`, `input/empresa/Pains_Unificados.txt`,
`input/voces/Voz_[perfil].txt` o `input/eventos/Eventos_Campañas.txt`) y la mueve a `INBOX_procesado.md` con la
fecha de proceso. Las entradas ambiguas o que contradicen una regla existente no se
descartan: quedan anotadas como "requiere revisión" en el log de decisiones del mes,
pero el pipeline continúa igualmente.

Tu único trabajo manual es añadir líneas aquí abajo cuando se te ocurra algo. No hace
falta tocar ningún otro archivo ni relanzar nada aparte del pipeline habitual.

---

<!-- Añade tus líneas nuevas debajo de esta marca. El archivista las retira de aquí
cuando las procesa. -->

<!-- Noticias del sector (recopiladas 2026-10-08). La fecha delante es la de la noticia o el hito, no la de entrada. Las marcadas "VERIFICAR" tienen fuentes contradictorias o una sola fuente. -->

- 2025-12-04: La Ley 9/2025 de Movilidad Sostenible se publicó en el BOE. Su disposición transitoria octava hace "necesariamente digital" el documento de control administrativo (DeCA) del transporte público de mercancías por carretera a partir del 5 de octubre de 2026 (Orden FOM/2861/2012). Fuente: https://www.muycanal.com/2026/03/06/carta-porte-digital-ecmr
- 2026-10-05: Desde hoy el DeCA es digital en el transporte público de mercancías por carretera en España. Solo afecta al transporte interior (nacional y cabotaje); los internacionales siguen con los documentos de los convenios. Fuente: https://www.apr.es/
- 2026-10-05: Aclaración sobre el eCMR: sigue siendo OPCIONAL en transporte internacional (el Protocolo adicional al CMR está en vigor para España desde 2011). Lo obligatorio el 5 de octubre es el DeCA electrónico. Varios proveedores de software lo presentan como "eCMR obligatorio" y alguna fuente da el 5 de septiembre como fecha: VERIFICAR siempre en el BOE. Fuente: https://kaleidotrans.com/ecmr-obligatorio-2026
- 2026-10-01: Congreso de Feteia en Tenerife (1-4 de octubre), con sesión técnica sobre novedades aduaneras en la que participó la Agencia Tributaria. Fuente: https://elmercantil.com/2026/06/04/los-transitarios-centran-su-congreso-en-el-estado-la-logistica-las-aduanas-y-la-vision-de-los-jovenes/
- 2026-10-02: Conclusiones del congreso de transitarios: Data Hub, comercio electrónico, coordinación administrativa y asesoramiento como claves del nuevo escenario aduanero. El artículo sostiene que la reforma del CAU abre al transitario una vía de diferenciación basada en datos y asesoramiento. Fuente: https://www.diarioelcanal.com/la-reforma-aduanera-abre-una-nueva-etapa-para-el-transitario-basada-en-los-datos-y-el-asesoramiento/
- 2026-10-01: Seminario web de la AEAT sobre comercio electrónico: cambios que entran en vigor en noviembre (tasa de tramitación por envío e identificadores de producto) y nueva versión de la guía de declaraciones de escaso valor (H7) hasta 150 €. VERIFICAR la tasa de tramitación: solo la menciona una fuente. Fuente: https://sede.agenciatributaria.gob.es/Sede/aduanas/novedades.html
- 2026-02-18: Se publica en el DOUE el Reglamento (UE) 2026/382, que elimina la franquicia de derechos de aduana para envíos de hasta 150 € de valor intrínseco. Fuente: https://www.camarazamora.com/reglamento-ue-2026-382-que-cambia-en-los-envios-de-menos-de-150-e-aduanas-ue
- 2026-07-01: Empieza el derecho de aduana fijo transitorio de 3 € para envíos de bajo valor (hasta el 1 de julio de 2028). VERIFICAR la unidad de cobro: unas fuentes dicen por artículo y otras por línea arancelaria. Se suma al IVA y también aplica con IOSS según un proveedor. Fuente: https://www.e-consulting.org/comunicacion/sala-de-prensa/la-union-europea-suprime-la-franquicia-aduanera-de-150-euros-y-establece-un-derecho-fijo-transitorio-hasta-2028
- 2026-10-01: Fecha límite para que la Comisión evalúe posibles desvíos de flujos comerciales tras eliminar la franquicia de 150 € (después, evaluación mensual). Fuente: https://www.camarazamora.com/reglamento-ue-2026-382-que-cambia-en-los-envios-de-menos-de-150-e-aduanas-ue
- 2028-01-01: Fecha prevista para el EU Customs Data Hub, que daría paso al régimen definitivo para los envíos de bajo valor. Fuente: https://www.e-consulting.org/comunicacion/sala-de-prensa/la-union-europea-suprime-la-franquicia-aduanera-de-150-euros-y-establece-un-derecho-fijo-transitorio-hasta-2028
- 2026-09-19: Publicación del nuevo Código Aduanero de la Unión según varias fuentes: ventanilla única que refunde sistemas nacionales y Autoridad Aduanera con sede en Lille; 12 meses para aplicar las reglas y calendario hasta 2031. VERIFICAR en EUR-Lex. Fuente: https://www.diariodelpuerto.com/logistica/entra-en-vigor-la-reforma-aduanera-de-la-union-europea-OH26656282
- 2026-02-03: ICS2 versión 3 obligatoria en todos los modos de transporte, con presentación múltiple de ENS. La responsabilidad del filer a nivel house no es transferible. Fuente: https://www.icustoms.ai/blogs/ics2-release-3-guide-for-freight-forwarders/
- 2026-05-04: Actualización de "stop words" en ICS2: una palabra de la lista usada sola en la descripción de la mercancía hace que se rechace la declaración (p. ej. "general goods"). Fuente: https://gofreight.com/blog/freight-forwarder-compliance-calendar
- 2026-06-01: Fin de los periodos transitorios de ICS2 en carretera (Polonia, Croacia, Letonia, Rumanía y Eslovaquia). La Comisión indica que desde esta fecha toda consignación que entre en la UE debe tener ENS válido. Algunas fuentes mencionan derogaciones nacionales: VERIFICAR país por país. Fuente: https://eurodebt.eu/en/ICS2-for-road-transport-June-2026-ends-the-era-of-the-old-customs-system-in-the-EU/
- 2026-12-31: Antes de fin de 2026 ICS2 debería permitir que varios operadores presenten datos parciales de ENS sobre el mismo envío (naviera e importador por separado). Fuente: https://www.icustoms.ai/blogs/ics2-release-3-guide-for-freight-forwarders/
- 2026-01-01: CBAM en periodo definitivo: solo los declarantes autorizados pueden importar mercancías del Anexo I. Excepción provisional para quien solicitó la autorización antes del 31 de marzo de 2026. En España, MITECO gestiona el Registro CBAM y la AEAT controla en frontera. Fuente: https://www.miteco.gob.es/es/cambio-climatico/temas/cbam/actores-cbam.html
- 2027-09-30: Vence la primera declaración CBAM anual (importaciones de 2026); los certificados se compran desde febrero de 2027, así que el coste de 2026 es retroactivo. Fuente: https://www.miteco.gob.es/es/cambio-climatico/temas/cbam/periodo-definitivo/declaracion-cbam.html
- 2026-10-05: La Comisión publica el precio de referencia del certificado CBAM del tercer trimestre de 2026: 82,32 €/t CO2 (Q1: 75,36 €; Q2: 75,28 €). Fuente: https://gmk.center/en/news/the-european-commission-has-announced-the-price-of-cbam-certificates-for-q3-2026/
- 2026-07-01: Tacógrafo inteligente obligatorio en furgonetas de 2,5 a 3,5 t en transporte internacional y cabotaje (Reglamento (UE) 2020/1054). Exentas las que operan solo dentro de España. La multa de 2.000 € que cita la prensa viene de una sola fuente: VERIFICAR con la DGT. Fuente: https://www.espaciofurgo.com/2026-el-ano-en-que-las-furgonetas-entraran-en-la-era-del-tacografo/
- 2026-02-06: Renovado el Comité Nacional del Transporte por Carretera para 2026-2029: Javier Arnedo, presidente del departamento de mercancías, propuesto por CETM (55,2 % de representatividad). Fuente: https://nuevecuatrouno.com/2026/02/06/rioja-javier-arnedo-presidente-comite-nacional-transporte-carretera/
- 2026-08-27: Drewry World Container Index: 4.473 $/FEU (-1 %). Shanghái-Génova 4.866 $ (-2 %) y Shanghái-Róterdam 4.287 $ (-3 %). Fuente: https://www.hellenicshippingnews.com/drewry-world-container-index-3/
- 2026-07-02: El WCI de Drewry llegó a 4.639 $/FEU, el nivel más alto desde septiembre de 2024, empujado por Asia-Europa. CMA CGM anunció FAK de 7.000 $/FEU Asia-Europa y 7.900-8.500 $ Asia-Med desde el 15 de julio. Fuente: https://container-news.com/drewrys-world-container-index-surges-8-on-asia-europe-rate-gains/
- 2026-08-27: Congestión en el puerto de Shanghái: la espera media de buques subió de 35 a 96 horas en una semana, con más blank sailings anunciados. Incertidumbre en Ormuz y reanudación cautelosa de tránsitos por Suez. Fuente: https://www.hellenicshippingnews.com/world-container-index-20-aug/
- 2026-10-01: APR advierte de que el aumento de capacidad marítima previsto para octubre no garantiza embarques más fiables y recomienda a quien importa desde Asia revisar salidas y proteger entregas críticas. Fuente: https://www.apr.es/
- 2026-07-31: Los puertos estatales españoles cerraron el primer semestre con 9.417.467 TEU (+2,4 %). Valencia 2.822.376 TEU (+0,3 %) y Algeciras 2.380.131 TEU (+3,5 %). Fuente: https://www.elestrechodigital.com/en/imprimir/spanish-ports-move-942-million-teus-in-the-first-semester-and-grow-24
- 2026-07-24: Entran en vigor aranceles del 10 % de EE. UU. a importaciones de la UE (investigación sobre trabajo forzoso, Sección 301), que sustituyen al arancel global temporal del mismo porcentaje. Afecta a agroalimentación, maquinaria y moda. Situación posterior a julio sin confirmar. Fuente: https://www.que.es/2026/07/24/aranceles-trump-ue-2026/
- 2026-09-29: IATA publica los datos de carga aérea de agosto: demanda mundial +4,4 % (CTK) con capacidad -0,1 %. Aerolíneas europeas: demanda +4,1 % y capacidad -3,5 %. Fuente: https://www.iata.org/contentassets/0db8687e56fe4c29962c9b3af483cd1e/2026-09-29-01-sp.pdf
- 2026-10-16: Canarias intensificaría los controles fitosanitarios (NIMF 15 en embalajes y estibas de madera). VERIFICAR la fecha y el alcance en la fuente oficial: la noticia de origen no tiene fecha clara. Fuente: https://www.amcargo.es/blog/page/7/
