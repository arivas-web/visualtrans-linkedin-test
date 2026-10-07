# visualtrans-linkedin

Sistema de contenido LinkedIn de Visual Trans / Visual MS. Lee `README.md` primero: explica
la estructura (`input/` lo que lee la IA, `output/AAAA-MM/` lo que genera) y las formas de
ejecución (automática y manual).

- Forma de hablar con el usuario: como un compañero de trabajo en un chat, natural y variado
  (no siempre las mismas frases). Nunca cuentes lo que haces por dentro ni nombres herramientas,
  commits, push, ramas, archivos, workflows o conectores ("voy a pushear", "compruebo el repo",
  "lanzo el workflow"...): eso no le interesa. Ejemplo de post suelto:
  - Pide un post → "Vale, me pongo con ello". Si falta algo (p. ej. el perfil), pregúntalo sin más:
    "¿Para qué perfil es?".
  - Le pasas el post → "¿Qué te parece? ¿Cambiamos algo?".
  - Le gusta → "¿Te preparo la gráfica y te lo programo?".
  - Responde → "Ok, me pongo con ello", y luego le pasas el resultado (post y enlace a la imagen).
  Solo si hay un error o un problema se explica, y entonces sí con todo el detalle técnico necesario.
- Comando del pipeline mensual: `/pipeline-mensual [mes] [año]` (`.claude/commands/pipeline-mensual.md`).
- Subagentes: `.claude/agents/` (archivista, investigador, calendario, redactor, presentacion, validador).
- Rutas siempre relativas a la raíz de este repo (`input/voces/Voz_Ceci.txt`, `output/2026-10/...`).
- Información nueva del usuario: se escribe en `input/inbox/INBOX.md` con fecha delante; el
  archivista la clasifica en la siguiente ejecución.
- Git: commit y push a `main` tras cada fase, sin `--force` ni `--no-verify`.
- Gráficas: `/generar-graficas` (`.claude/commands/generar-graficas.md`) con los subagentes `subagente-noticias` y `subagente-pains`; prompts de estilo en `input/graficas/`; detalle en `docs/graficas.md`. Nunca inventes enlaces de imagen ni marques `OK` sin imagen real.
  **Las gráficas de un mes aprobado se generan con la rutina `agente-graficas` (cuenta de Claude de un compañero, con el conector de Magnific y sus créditos), disparada por `.github/workflows/lanzar-graficas.yml`, no con los créditos de esta sesión.** Si `account_balance` de esta sesión da 0, no es un bloqueo: usa el workflow (`workflow_dispatch` con `mes`, o push a `main` de `output/AAAA-MM/posts-para-graficas.txt`). El workflow solo lee ese nombre exacto de archivo y escribe `graficas.csv`; para posts extra, añádelos a ese TXT con IDs nuevos, nunca en un archivo aparte. Antes de disparar, confirma con el usuario (el push a `main` y los créditos son de otra persona).
- Metricool: `/programar-metricool AAAA-MM` (`.claude/commands/programar-metricool.md`) programa los posts aprobados con su imagen, solo tras un "ok" explícito y siempre en Metricool, nunca en HubSpot.
- Posts sueltos: `/post-suelto [perfil] [tema]` (`.claude/commands/post-suelto.md`): se redacta el texto y se pega en el chat; cuando el usuario lo valida, se le pregunta si quiere la gráfica y que se programe en Metricool (puede decir que no a una o a las dos). La gráfica siempre con la rutina del compañero (bloque nuevo en `posts-para-graficas.txt` del mes + push a `main`), nunca con el Magnific de esta sesión. Salida en `output/sueltos/`.
- Calendario mensual: se genera solo en la fecha programada o cuando el usuario lo pide (si pide algo concreto, se hace eso).
- Entrega siempre en el chat, sea un post suelto o el calendario: el texto de los posts y el enlace a cada imagen, no solo rutas de archivo.
