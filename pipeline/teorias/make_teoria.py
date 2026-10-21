#!/usr/bin/env python3
"""Motor 'teoria': vídeo vertical 1080x1920 para a página de teorias (entretenimento).

Uso: python3 make_teoria.py WORKDIR   (WORKDIR/spec.json)
spec.json:
{
  "titulo": "VIVEMOS NUMA MATRIX?",
  "segs": ["frase 1", "frase 2", ...],    # narração e legenda, uma por frase
  "fotos": ["a.jpg", "b.jpg", ...],       # fotos 9:16 ou maiores (baixadas pelo runner em "fotos_url")
  "voice": "pm_santa", "speed": 1.0,      # voz Kokoro local (grátis)
  "output": "teoria.mp4"
}
Paleta fixa da página: fundo #050A07, verde #00C853, dourado #E8B84A, texto #EDEDED.
"""
import json, os, sys, subprocess as sp, textwrap
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # pipeline/musica.py
import musica

W = sys.argv[1]
os.chdir(W)
S = json.load(open("spec.json"))
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FPS = 30
GAP = 0.35  # pausa entre frases, em segundos
# Paleta da página (azul-noite, mais suave aos olhos)
COR_FUNDO = "0x0B1220"     # faixa das legendas
COR_TITULO = "0x5EEAD4"    # ciano-água
COR_SELO = "0xF6C177"      # dourado suave
COR_TEXTO = "0xF1F5F9"     # branco-gelo
SR_MUSICA = 24000


def run(a):
    sp.run(a, check=True, capture_output=True)


# 1) Narração frase a frase (Kokoro, local)
KK = Kokoro("/tmp/kokoro/kokoro-v1.0.onnx", "/tmp/kokoro/voices-v1.0.bin")
VOICE = S.get("voice", "pm_santa")
SPEED = float(S.get("speed", 1.0))
partes, caps, t, sr_ref = [], [], 0.0, None
for txt in S["segs"]:
    a, sr = KK.create(txt, voice=VOICE, speed=SPEED, lang="pt-br")
    a = np.asarray(a, dtype=np.float32)
    sr_ref = sr
    d = len(a) / sr
    caps.append((t, t + d, txt))
    partes += [a, np.zeros(int(GAP * sr), dtype=np.float32)]
    t += d + GAP
total = t
sf.write("narracao.wav", np.concatenate(partes), sr_ref)

# 2) Fotos com zoom lento, uma por bloco de tempo igual
fotos = S["fotos"]
por_foto = total / len(fotos)
clipes = []
for i, f in enumerate(fotos):
    n = max(1, int(por_foto * FPS))
    vf = ("scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,"
          f"zoompan=z='min(zoom+0.0009,1.15)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={n}:s=1080x1920:fps={FPS}")
    out = f"foto{i}.mp4"
    run(["ffmpeg", "-y", "-i", f, "-vf", vf, "-frames:v", str(n), "-r", str(FPS),
         "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", out])
    clipes.append(out)
open("lista.txt", "w").write("".join(f"file '{c}'\n" for c in clipes))
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "lista.txt", "-c", "copy", "base.mp4"])

# 3) Título, selo e legendas (cada frase na sua janela de tempo)
open("titulo.txt", "w").write(S.get("titulo", "TEORIA DA CONSPIRAÇÃO"))
open("selo.txt", "w").write("TEORIA DE ENTRETENIMENTO")
# Gancho: o título aparece desde o primeiro quadro, com faixa escura para leitura
F = [
    f"drawbox=x=0:y=ih*0.56:w=iw:h=ih*0.30:color={COR_FUNDO}@0.78:t=fill",
    f"drawtext=fontfile={FONT}:textfile=titulo.txt:fontsize=72:fontcolor={COR_TITULO}"
    f":x=(w-text_w)/2:y=170:box=1:boxcolor={COR_FUNDO}@0.65:boxborderw=20",
    f"drawtext=fontfile={FONT}:textfile=selo.txt:fontsize=34:fontcolor={COR_SELO}"
    ":x=(w-text_w)/2:y=290",
]
for i, (a, b, txt) in enumerate(caps):
    open(f"cap{i}.txt", "w").write(textwrap.fill(txt, 24))
    F.append(f"drawtext=fontfile={FONT}:textfile=cap{i}.txt:fontsize=58:fontcolor={COR_TEXTO}"
             f":line_spacing=10:x=(w-text_w)/2:y=h*0.62"
             f":enable=between(t\\,{a:.2f}\\,{b:.2f})")

# 4) Trilha de suspense (gerada por código, sem direitos autorais) + "impacto" no primeiro segundo
import musica
musica.gerar("_trilha.wav", total + 0.5, sr=SR_MUSICA, mood=S.get("trilha", "misterio"))
trilha, _ = sf.read("_trilha.wav", dtype="float32")
n_imp = int(0.9 * SR_MUSICA)
tt = np.arange(n_imp) / SR_MUSICA
impacto = (np.sin(2 * np.pi * (60 + 40 * np.exp(-tt * 12)) * tt) * np.exp(-tt * 5) * 0.7).astype(np.float32)
trilha[:n_imp] += impacto[:len(trilha[:n_imp])]
sf.write("trilha_final.wav", trilha, SR_MUSICA)

saida = S.get("output", "teoria.mp4")
filtro = (f"[0:v]{','.join(F)}[v];"
          "[1:a]volume=1.0[fala];[2:a]volume=0.16[musica];"
          "[fala][musica]amix=inputs=2:duration=first:dropout_transition=0[a]")
run(["ffmpeg", "-y", "-i", "base.mp4", "-i", "narracao.wav", "-i", "trilha_final.wav",
     "-filter_complex", filtro, "-map", "[v]", "-map", "[a]", "-shortest",
     "-c:v", "libx264", "-preset", "veryfast", "-crf", "23", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "128k", saida])
print("ok", saida, round(total, 1), "s")
