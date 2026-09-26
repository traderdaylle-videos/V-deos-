#!/usr/bin/env bash
# Instala dependências e a voz gratuita Kokoro (pt-BR, voz "pm_santa") em /tmp/kokoro. Idempotente.
set -e
pip install matplotlib numpy pillow kokoro-onnx soundfile --break-system-packages -q 2>/dev/null || true
K=/tmp/kokoro; mkdir -p $K
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "$K/$f" ] || curl -sL -o "$K/$f" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"
done
echo "kokoro ok: $K"
