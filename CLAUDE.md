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
