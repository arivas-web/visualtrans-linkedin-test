---
description: Redacta un post suelto de LinkedIn (fuera del calendario mensual) para un perfil y genera su gráfica con la rutina agente-graficas, pidiendo confirmación antes de lanzarla. Uso: /post-suelto [perfil] [tema] [fecha opcional]
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
La imagen **siempre** la genera la rutina `agente-graficas` (cuenta de Claude de su compañero,
con su conector de Magnific y sus créditos), nunca esta sesión: no consultes `account_balance` ni
invoques a `subagente-noticias`/`subagente-pains` para esto.

Antes de lanzarla dile al usuario que implica un **push a `main`** y gastar **créditos de otra
persona**, y **pregunta si la lanzas**. Sin un "sí" claro no hagas push.

## 7. Generar la imagen (rutina `agente-graficas`)

El usuario **no** debe crear ni editar ningún TXT: lo haces tú, tras su "sí" del paso 6.
1. Añade **al final** de `output/AAAA-MM/posts-para-graficas.txt` (AAAA-MM = mes de hoy; si no
   existe, créalo) un bloque nuevo con el formato de `docs/graficas.md`, ID
   `SUELTO-AAAA-MM-DD-tema`, `FECHA:` la del post o `sin fecha`, el `PERFIL`, el `PILAR` ya
   deducido y el texto tal cual. **No toques los bloques existentes ni `graficas.csv`.**
   Si ya hay una fila con ese ID en `OK`, usa otro ID (p. ej. añade `-v2`).
2. Commit y push a `main` (sin `--force` ni `--no-verify`). Ese push dispara
   `.github/workflows/lanzar-graficas.yml`, que llama a la rutina. Si el push a `main` está
   bloqueado, dilo y para: no lo rodees.
3. Comprueba con las herramientas de GitHub que el workflow termina en `success` y díselo al
   usuario. La rutina solo procesa los bloques del TXT cuya fila no esté en `OK` en
   `graficas.csv`: solo se generará la imagen nueva.
4. La rutina tarda unos minutos y escribe el resultado en la fila de ese ID de
   `output/AAAA-MM/graficas.csv` (puede llegar en una rama `claude/...`). Cuando el usuario
   lo pida, mira el CSV: con `OK` y enlace, enséñale la imagen; con `error`, dile el motivo.
   Nunca inventes el enlace ni lo des por hecho.

Si no le gusta la imagen, puede pedir otra: cada nueva generación vuelve a gastar créditos, así
que pide confirmación de nuevo (con un ID nuevo `-v2`).

## 8. Dejarlo guardado

Guarda en la misma carpeta `imagen.md` con el enlace de la imagen (o el ID del bloque y
el estado "pendiente de la rutina"), el prompt usado y el estado. Salvo el commit y push del bloque
del TXT, **no hagas commit ni push** de nada más a menos que el usuario lo pida.

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
- No generes la imagen, no hagas push a `main` ni programes nada sin la confirmación explícita correspondiente.
- No mezcles estos posts con el calendario del mes. Solo añades bloques al final del TXT; `graficas.csv` lo escribe la rutina, nunca tú.
