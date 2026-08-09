#!/bin/bash
# Owl -> Telegram notifier (Human Architect's chat 813848257)
# Usage: telegram_notify.sh "message text"
MSG="$1"
[ -z "$MSG" ] && exit 1
BOT=$(grep '^TELEGRAM_BOT_TOKEN=' /root/.hermes/.env 2>/dev/null | cut -d= -f2-)
CHAT=813848257
[ -z "$BOT" ] && { echo "NO_TOKEN"; exit 2; }
curl -s --max-time 10 -X POST "https://api.telegram.org/bot$BOT/sendMessage" \
  --data-urlencode "chat_id=$CHAT" \
  --data-urlencode "text=$MSG" >/dev/null 2>&1
echo "sent"
