# visualtrans-linkedin

Sistema de contenido LinkedIn de Visual Trans / Visual MS. Lee `README.md` primero: explica
la estructura (`input/` lo que lee la IA, `output/AAAA-MM/` lo que genera) y las formas de
ejecución (automática y manual).

- Comando del pipeline mensual: `/pipeline-mensual [mes] [año]` (`.claude/commands/pipeline-mensual.md`).
- Subagentes: `.claude/agents/` (archivista, investigador, calendario, redactor, presentacion, validador).
- Rutas siempre relativas a la raíz de este repo (`input/voces/Voz_Ceci.txt`, `output/2026-10/...`).
- Información nueva del usuario: se escribe en `input/inbox/INBOX.md` con fecha delante; el
  archivista la clasifica en la siguiente ejecución.
- Git: commit y push a `main` tras cada fase, sin `--force` ni `--no-verify`.
- Gráficas: `/generar-graficas` (`.claude/commands/generar-graficas.md`) con los subagentes `subagente-noticias` y `subagente-pains`; prompts de estilo en `input/graficas/`; detalle en `docs/graficas.md`. Nunca inventes enlaces de imagen ni marques `OK` sin imagen real.
  **Las gráficas de un mes aprobado se generan con la rutina `agente-graficas` (cuenta de Claude de un compañero, con el conector de Magnific y sus créditos), disparada por `.github/workflows/lanzar-graficas.yml`, no con los créditos de esta sesión.** Si `account_balance` de esta sesión da 0, no es un bloqueo: usa el workflow (`workflow_dispatch` con `mes`, o push a `main` de `output/AAAA-MM/posts-para-graficas.txt`). El workflow solo lee ese nombre exacto de archivo y escribe `graficas.csv`; para posts extra, añádelos a ese TXT con IDs nuevos, nunca en un archivo aparte. Antes de disparar, confirma con el usuario (el push a `main` y los créditos son de otra persona).
- Metricool: `/programar-metricool AAAA-MM` (`.claude/commands/programar-metricool.md`) programa los posts aprobados con su imagen, solo tras un "ok" explícito y siempre en Metricool, nunca en HubSpot.
- Posts sueltos: `/post-suelto [perfil] [tema]` (`.claude/commands/post-suelto.md`): texto con la voz del perfil e imagen en Magnific, confirmando antes de generar la imagen (gasta créditos). Salida en `output/sueltos/`. La imagen siempre la genera la rutina `agente-graficas` (nunca los créditos de la sesión): el propio comando añade el bloque al `posts-para-graficas.txt` del mes y hace push (tras el "sí" del usuario) para que la rutina genere la imagen: el usuario no toca el TXT. Lo programa el usuario a mano salvo que pida Metricool.
