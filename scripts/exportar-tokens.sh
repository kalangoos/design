#!/bin/sh
# Export FigCraft variables to tokens/_variables.json (raw).
# The GTK CSS files (tokens-dark.css / tokens-light.css) and tokens.json used by
# the KalangoOS monorepo are curated exports — after changing colour/layout/motion
# variables, update tokens/ and open a sync PR on kalangoos/kalangoos (design/tokens/).
set -e
cd "$(dirname "$0")/.."
FILE=KalangoOS-DesignSystem.figcraft
CLI="${FIGCRAFT_CLI:-figcraft-cli}"
OUT=tokens/_variables.json

command -v "$CLI" >/dev/null || {
  echo "figcraft-cli not found. Install FigCraft or set FIGCRAFT_CLI." >&2
  exit 1
}
[ -f "$FILE" ] || { echo "missing $FILE" >&2; exit 1; }

tmp=$(mktemp)
trap "rm -f \"$tmp\" \"$tmp.in\"" EXIT
printf "%s\n" "[{\"command\":\"variable.export\",\"params\":{\"format\":\"json\",\"path\":\"$OUT\"}}]" > "$tmp.in"
# run needs --in the document
"$CLI" run "$tmp.in" --in "$FILE"
echo "Wrote $OUT (if the command succeeded)."
echo "Next: refresh tokens.json / tokens-*.css to match, then sync the monorepo."
