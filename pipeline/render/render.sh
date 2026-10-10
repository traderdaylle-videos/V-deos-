#!/usr/bin/env bash
# Renderiza um vídeo fora do Claude (GitHub Actions). Uso: render.sh <pipeline/fila/NOME.json> <pasta_saida>
# Chaves do spec usadas aqui (além das que os scripts já usam):
#   "motor": "gf" (make_gf_cine.py) | "video" (make_video.py) | "ranking" (make_ranking.py)
#   "explainer_args": lista de argumentos para explainer_primewin.py (gera explicativo_anim.mp4 e explicativo_final.png)
set -euo pipefail
SPEC="$1"; OUT="$2"
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
NAME="$(basename "$SPEC" .json)"
W="/tmp/w/$NAME"; rm -rf "$W"; mkdir -p "$W" "$OUT"
cp "$SPEC" "$W/spec.json"

# ativos: clipes reais (branch clipes), fotos e relatórios do repositório
cp /tmp/clipes/clipes/*.mp4 "$W"/ 2>/dev/null || true
cp "$ROOT"/pipeline/fotos/* "$W"/ 2>/dev/null || true
cp "$ROOT"/pipeline/primewin/magneto/* "$W"/ 2>/dev/null || true

MOTOR=$(python3 -c "import json,sys;print(json.load(open('$W/spec.json')).get('motor','video'))")
cd "$W"
if python3 -c "import json,sys;sys.exit(0 if json.load(open('spec.json')).get('explainer_args') else 1)"; then
  python3 - <<'PY' > _explainer_args.txt
import json; print("\n".join(json.load(open("spec.json"))["explainer_args"]))
PY
  mapfile -t ARGS < _explainer_args.txt
  python3 "$ROOT/pipeline/primewin/explainer_primewin.py" "${ARGS[@]}"
fi

# explicativo próprio (TikTok): "explainer_script" = caminho (a partir da raiz do repo) de um script que gera explicativo_anim.mp4 e explicativo_final.png
EXS=$(python3 -c "import json;print(json.load(open('$W/spec.json')).get('explainer_script',''))")
[ -n "$EXS" ] && (cd "$W" && python3 "$ROOT/$EXS")

case "$MOTOR" in
  gf)      python3 "$ROOT/pipeline/granaefinancas/make_gf_cine.py" "$W" ;;
  ranking) python3 "$ROOT/pipeline/mundonumeral/make_ranking.py" "$W" ;;
  *)       python3 "$ROOT/pipeline/make_video.py" "$W" ;;
esac

OUTFILE=$(python3 -c "import json;print(json.load(open('spec.json')).get('output','video.mp4'))")
[ -s "$OUTFILE" ] || { echo "ERRO: vídeo não gerado: $OUTFILE" >&2; exit 1; }
TAM=$(stat -c %s "$OUTFILE")
[ "$TAM" -lt 95000000 ] || { echo "ERRO: $OUTFILE tem $((TAM/1000000)) MB; o GitHub recusa arquivos acima de 100 MB." >&2; exit 1; }
cp "$OUTFILE" "$OUT/$NAME.mp4"
for c in "${OUTFILE%.mp4}_capa.jpg" "capa.jpg"; do [ -s "$c" ] && cp "$c" "$OUT/$NAME-capa.jpg" && break; done || true
echo "OK: $OUT/$NAME.mp4"
