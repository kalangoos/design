#!/bin/sh
# Export PNG frames from the Design System for PR review and the site gallery.
# Needs figcraft-cli on PATH (https://github.com/storytold/figcraft/releases).
set -e
cd "$(dirname "$0")/.."
FILE=KalangoOS-DesignSystem.figcraft
OUT=exports/vitrine
SCALE="${SCALE:-1}"
CLI="${FIGCRAFT_CLI:-figcraft-cli}"

command -v "$CLI" >/dev/null || {
  echo "figcraft-cli not found. Install FigCraft or set FIGCRAFT_CLI." >&2
  exit 1
}
[ -f "$FILE" ] || { echo "missing $FILE" >&2; exit 1; }

# Default showcase pages (override with: PAGES="01 · Fundamentos" ./scripts/exportar-telas.sh)
if [ -n "$PAGES" ]; then
  set -- $PAGES
else
  set -- \
    "00 · Capa" \
    "01 · Fundamentos" \
    "23 · Marca (KalangoOS)" \
    "Site · Landing page"
fi

safe_name() {
  echo "$1" | sed "s/ · /-/g; s/ /_/g; s/(//g; s/)//g"
}

mkdir -p "$OUT"
for page in "$@"; do
  dir="$OUT/$(safe_name "$page")"
  mkdir -p "$dir"
  echo "→ $page"
  "$CLI" export "$FILE" -o "$dir" --format png --scale "$SCALE" --page "$page" || true
done

python3 scripts/escrever-manifesto.py
echo "Done. See $OUT and exports/manifest.json"
