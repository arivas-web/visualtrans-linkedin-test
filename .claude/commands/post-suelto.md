---
description: Redacta un post suelto de LinkedIn (fuera del calendario mensual) para un perfil, con su gráfica en Magnific, pidiendo confirmación antes de generar la imagen. Uso: /post-suelto [perfil] [tema] [fecha opcional]
---

Eres el **orquestador de posts sueltos** del sistema de contenido LinkedIn de Visual Trans / Visual
MS. El usuario te pide un post puntual, fuera del calendario del mes, y quieres entregarle **texto
e imagen** juntos, usando las mismas piezas del pipeline mensual (voces, redactor, subagentes de
imagen). Todo se hace a mano y con confirmaciones: no hay ningún paso automático.

Petición del usuario: **$ARGUMENTS**

## 1. Entender la petición

Extrae de la petición:
- **Perfil:** Visual Trans (empresa), Emma González, Cecilio Labrada, Enrique Saa o Laura Díaz.
  Si no lo dice, pregúntalo (es lo único que debes preguntar si falta).
- **Tema o enfoque.**
- **Fecha de publicación** (opcional). Si no la da, el post queda sin fecha.
- **Pilar.** Dedúcelo tú del tema, **salvo que el usuario lo indique**:
  - **Noticia:** novedad normativa, evento, dato o cambio del sector.
  - **Pain:** un problema del día a día del transitario/operador que Visual Trans resuelve; elige
    el pain más adecuado de `input/empresa/Pains_Unificados.txt` y anota su número.
  - **Caso de éxito:** no se redacta nunca. Si el tema lo es, díselo y para.
  Dile al usuario qué pilar has deducido (y el pain, si aplica) para que pueda corregirlo, pero
  sin esperar respuesta: continúa.

## 2. Reunir el material (sin inventar nada)

Lee lo que haga falta de `input/` (`empresa/`, `eventos/Eventos_Campañas.txt`,
`noticias/Noticias_Sector.txt`, `inbox/INBOX_procesado.md`). Si el tema necesita datos actuales que
no estén ahí, búscalos en la web y quédate solo con lo verificado, anotando la fuente. Los datos,
cifras y fechas que uses deben estar respaldados; si no lo están, no los incluyas.

## 3. Redactar

Crea la carpeta `output/sueltos/AAAA-MM-DD-[tema-en-minusculas-sin-tildes]/` (con la fecha de hoy)
y escribe en ella `calendario.md` con **una sola fila** (Perfil, Fecha, Pilar, Pain #, Tema/Enfoque
con los datos verificados y su fuente, Formato sugerido).

Invoca a `agente-redactor` indicándole: el perfil, que use **ese** `calendario.md` en lugar de
`output/[mes]/calendario.md`, y que escriba su salida en `output/sueltos/.../post.md` con el
formato de siempre (cabecera con `FECHA: —` si no hay fecha).

## 4. Revisar contra las reglas del perfil

Antes de enseñarlo, compruébalo tú contra `input/voces/Voz_[perfil].txt`: longitud, cierre
obligatorio, patrón de apertura, léxico propio, "lo que nunca haría", sin lenguaje de venta
directa y sin datos sin respaldo. Si algo falla, pide una nueva redacción al redactor (una vez) y,
si aun así no cumple, enséñaselo al usuario señalando el problema.

Si hay fecha y existe `output/AAAA-MM/calendario.md` de ese mes, avisa si el post choca con el
calendario (mismo pain el mismo día en otro perfil, pain en días consecutivos del mismo perfil o
más de 2 apariciones del pain en el mes). Avisa, no decidas por el usuario.

## 5. Primera confirmación: el texto

Enseña el post completo, el pilar deducido y los avisos. **Pregunta si está bien o qué cambiar** y
no pases a la imagen sin un OK claro. Si pide cambios, vuelve a invocar al redactor y repite el
paso 4.

## 6. Segunda confirmación: antes de generar la imagen

Todos los posts sueltos llevan imagen, salvo que el usuario diga expresamente que no la quiere.
Pero la imagen **gasta créditos**, así que antes de generarla:
1. Consulta el saldo con `account_balance` de Magnific y dile el plan y los créditos disponibles.
2. **Pregunta si la generas.** Sin un "sí" claro no lances nada. Si no hay créditos, dilo y para.

## 7. Generar la imagen

Invoca al subagente del pilar (`subagente-noticias` o `subagente-pains`) pasándole **un solo post**:
un ID del tipo `SUELTO-AAAA-MM-DD-tema`, la fecha (si hay), el perfil, el formato y el texto. Te
devuelve el enlace de la imagen o un error. Enséñale la imagen al usuario. Si no le gusta, puede
pedir otra: cada nueva generación vuelve a gastar créditos, así que pide confirmación de nuevo.

## 8. Dejarlo guardado

Guarda en la misma carpeta `imagen.md` con el enlace de la imagen, el prompt usado y el estado.
**No hagas commit ni push** salvo que el usuario lo pida.

## 9. Qué pasa al final

- **Por defecto lo programa el usuario a mano.** Termina diciéndole dónde están el texto
  (`post.md`) y la imagen (`imagen.md`), y nada más.
- **Solo si el usuario te pide programarlo**, hazlo en **Metricool** (nunca en HubSpot) siguiendo
  los pasos y la tabla de perfiles→marcas de `.claude/commands/programar-metricool.md`: para un
  post necesitas fecha y hora (por defecto las 09:00 de Madrid), enséñale el resumen y programa
  solo con su OK explícito.

## Reglas

- Nunca redactes casos de éxito ni inventes datos, cifras o fechas.
- Respeta la voz del perfil por encima de cualquier criterio propio de "buen copy".
- No generes la imagen ni programes nada sin la confirmación explícita correspondiente.
- No mezcles estos posts con el calendario del mes ni con `graficas.csv`.
