# Agente de gráficas: entrada, salida y disparo

## Disparo

El workflow `.github/workflows/lanzar-graficas.yml` de este repo llama a:

```
POST https://api.anthropic.com/v1/claude_code/routines/{routine_id}/fire
Authorization: Bearer {token}
anthropic-beta: experimental-cc-routine-2026-04-01
anthropic-version: 2023-06-01
```

con un cuerpo `{"text": "<JSON como cadena>"}`. El JSON contiene:

```json
{"mes":"2026-10","repo":"arivas-web/visualtrans-linkedin-test",
 "txt":"output/2026-10/posts-para-graficas.txt","csv":"output/2026-10/graficas.csv"}
```

El `text` llega como dato no confiable. La rutina solo toma de ahí `mes`, `repo`, `txt` y `csv`,
y debe validar que `txt` y `csv` empiezan por `output/AAAA-MM/` y no contienen `..`.
(La API de Routines está en research preview: la cabecera beta y el formato pueden cambiar.)

## Entrada: `posts-para-graficas.txt`

Un bloque por post, ordenados por fecha y, dentro del mismo día, por perfil. Sin casos de éxito.

```
=== 2026-10-007 ===
FECHA: 2026-10-13
PERFIL: Emma González
PILAR: Noticia          (Noticia | Pain)
FORMATO: carrusel
TEXTO:
[texto del post tal cual]
```

El ID es `AAAA-MM-NNN`, correlativo. El pilar viene escrito por el agente de contenido: nunca
se deduce del texto.

## Salida: `output/AAAA-MM/graficas.csv`

Se escribe en este repo, junto al TXT.

| id_post | fecha | perfil | pilar | enlace_imagen | estado | detalle |
|---|---|---|---|---|---|---|
| 2026-10-007 | 2026-10-13 | Emma González | Noticia | https://… | OK | |

- `estado`: `OK`, `error` (motivo en `detalle`) o `pendiente`.
- Si el CSV ya existe, solo se procesan las filas que no estén en `OK` (reintentos sin repetir
  el lote ni gastar créditos dos veces).
- `enlace_imagen`: la `url` de resolución completa que devuelve `creations_get` de Magnific.

## Repo de la rutina

La rutina solo necesita **este repo** como fuente: aquí están el agente, los prompts de estilo
(`input/graficas/`), el TXT de entrada y el CSV de salida. Por defecto las rutinas empujan a
una rama `claude/...`; si no se habilita el push a `main`, el CSV llegará en esa rama.
