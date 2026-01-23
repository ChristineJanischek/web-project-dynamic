#!/usr/bin/env bash
set -euo pipefail
FILE="version3/aufgabe/phase2-implementation/index-starter.html"
if [ ! -f "$FILE" ]; then
  echo "Fehlt: $FILE" >&2
  exit 1
fi
npx pa11y "file://$PWD/$FILE" --reporter markdown || true
