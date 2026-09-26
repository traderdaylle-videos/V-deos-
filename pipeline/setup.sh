#!/usr/bin/env bash
# Instala dependências e a voz gratuita (Piper pt-BR) em /tmp/piper. Idempotente.
set -e
pip install matplotlib numpy pillow --break-system-packages -q 2>/dev/null || true
P=/tmp/piper
if [ ! -x "$P/piper/piper" ]; then
  mkdir -p $P && cd $P
  curl -sL -o voice.tar.gz https://github.com/rhasspy/piper/releases/download/v0.0.2/voice-pt-br-edresson-low.tar.gz
  curl -sL -o piper.tar.gz https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_linux_x86_64.tar.gz
  tar xzf voice.tar.gz && tar xzf piper.tar.gz && rm -f voice.tar.gz piper.tar.gz
fi
echo "piper ok: $P"
