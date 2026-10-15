#!/usr/bin/env bash
# Envía un aviso al Telegram del usuario a través del bot del sistema de contenido.
#
# Uso:  scripts/aviso_telegram.sh "texto del aviso"
#       echo "texto largo" | scripts/aviso_telegram.sh
#
# Variables de entorno (se configuran en los ajustes del entorno, nunca en el repo):
#   TELEGRAM_BOT_TOKEN  token que da @BotFather
#
# Los avisos van solo al chat del usuario (CHAT_ID, abajo).
# Telegram corta los mensajes a 4096 caracteres: los textos largos se mandan en varios trozos.
# Sale con error si falta el token o si Telegram rechaza el envío.
set -euo pipefail

CHAT_ID="7693213014"

if [ -z "${TELEGRAM_BOT_TOKEN:-}" ]; then
  echo "Falta TELEGRAM_BOT_TOKEN en el entorno" >&2
  exit 1
fi

if [ $# -gt 0 ]; then
  texto="$*"
else
  texto="$(cat)"
fi

if [ -z "$texto" ]; then
  echo "No hay texto que enviar" >&2
  exit 1
fi

max=4000
while [ -n "$texto" ]; do
  trozo="${texto:0:$max}"
  texto="${texto:$max}"
  respuesta="$(curl -sS -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${CHAT_ID}" \
    --data-urlencode "text=${trozo}" \
    --data-urlencode "disable_web_page_preview=true")"
  if ! printf '%s' "$respuesta" | grep -q '"ok":true'; then
    echo "Telegram rechazó el envío: $respuesta" >&2
    exit 1
  fi
done
