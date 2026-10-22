#!/usr/bin/env python3
"""Motor 'teoria': vídeo vertical 1080x1920 para a página de teorias (entretenimento).

Uso: python3 make_teoria.py WORKDIR   (WORKDIR/spec.json)
spec.json:
{
  "titulo": "VIVEMOS NUMA MATRIX?",
  "segs": ["frase 1", "frase 2", ...],    # narração e legenda, uma por frase
  "midias": [["a.mp4", "b.jpg", "abstrato-codigo"], [...], ...],  # uma lista por frase; o tempo da frase é dividido entre as mídias
  "voice": "pm_santa", "speed": 1.0,      # voz Kokoro local (grátis)
  "trilha": "sombrio",
  "output": "teoria.mp4"
}
Mídias: .mp4 (clipes reais do branch clipes), .jpg/.png (fotos, baixadas pelo runner em "fotos_url") e abstratos gerados
por código: "abstrato-codigo", "abstrato-fractal", "abstrato-vida". (Compatível com o formato antigo: "fotos": [...]).
Paleta fixa da página: fundo #040507, vermelho #D64545, dourado #C9A227, texto #E6E6E6.
"""
import json, os, sys, subprocess as sp, textwrap
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))  # pipeline/musica.py
import musica

# Fonte de impacto (Inter Black, licença OFL), versionada em pipeline/teorias/fonts
FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "Inter-Black.otf")
W = sys.argv[1]
os.chdir(W)
S = json.load(open("spec.json"))
FPS = 30
GAP = 0.35  # pausa entre frases, em segundos
# Paleta da página (suspense: quase preto, vermelho-sangue, dourado escuro)
COR_FUNDO = "0x040507"
COR_TITULO = "0xD64545"
COR_SELO = "0xC9A227"
COR_TEXTO = "0xE6E6E6"
SR_MUSICA = 24000
# Clima escuro e granulado aplicado a toda mídia de vídeo/foto
TOM = "eq=contrast=1.12:brightness=-0.07:saturation=0.7,colorbalance=rs=0.06:bs=0.05"
ENC = ["-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-r", str(FPS)]


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

# 2) Linha do tempo de mídias: cada frase tem a sua lista, o tempo é dividido igualmente
if S.get("midias"):
    fatias = []
    for i, lista in enumerate(S["midias"]):
        ini = caps[i][0]
        fim = caps[i + 1][0] if i + 1 < len(caps) else total
        for m in lista:
            fatias.append((m, (fim - ini) / len(lista)))
else:
    fatias = [(f, total / len(S["fotos"])) for f in S["fotos"]]

ABSTRATOS = {
    "abstrato-codigo": ("cellauto=rule=110:random_fill_ratio=0.18:scroll=1:s=270x480:rate=30",
                        "format=rgb24,colorchannelmixer=rr=0.84:gg=0.27:bb=0.27,scale=1080:1920:flags=neighbor"),
    "abstrato-fractal": ("mandelbrot=s=540x960:rate=30:start_scale=3:end_scale=0.02:maxiter=300",
                         "format=gray,format=rgb24,colorchannelmixer=rr=0.84:gg=0.27:bb=0.27,scale=1080:1920"),
    "abstrato-vida": ("life=s=270x480:rate=30:ratio=0.1:mold=25:life_color=#D64545:death_color=#0a0a0a:mold_color=#3a0d0d",
                      "scale=1080:1920:flags=neighbor"),
}
COVER = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1"
clipes = []
for i, (src, dur) in enumerate(fatias):
    n = max(1, int(dur * FPS))
    out = f"s{i}.mp4"
    if src in ABSTRATOS:
        gen, vf = ABSTRATOS[src]
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", gen, "-vf", f"{vf},{TOM}", "-frames:v", str(n), *ENC, out])
    elif src.lower().endswith((".mp4", ".mov")):
        run(["ffmpeg", "-y", "-stream_loop", "-1", "-ss", "1", "-i", src, "-vf", f"fps={FPS},{COVER},{TOM}",
             "-frames:v", str(n), "-an", *ENC, out])
    else:
        vf = (f"{COVER},zoompan=z='min(zoom+0.0012,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":d={n}:s=1080x1920:fps={FPS},{TOM}")
        run(["ffmpeg", "-y", "-i", src, "-vf", vf, "-frames:v", str(n), *ENC, out])
    clipes.append(out)
open("lista.txt", "w").write("".join(f"file '{c}'\n" for c in clipes))
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "lista.txt", "-c", "copy", "base.mp4"])

# 3) Título, selo e legendas animadas (entram deslizando de baixo e com fade-in)
open("titulo.txt", "w").write(textwrap.fill(S.get("titulo", "TEORIA DA CONSPIRAÇÃO").upper(), 13))
open("selo.txt", "w").write("TEORIA DE ENTRETENIMENTO")
CONTORNO = "borderw=8:bordercolor=0x000000:shadowx=4:shadowy=4:shadowcolor=0x000000@0.85"
# vinheta e grão de filme para o clima de suspense; o título "treme" no primeiro segundo (gancho)
F = [
    "vignette=angle=PI/3.5",
    "noise=alls=9:allf=t",
    f"drawbox=x=0:y=ih*0.60:w=iw:h=ih*0.28:color={COR_FUNDO}@0.55:t=fill",
    f"drawtext=fontfile={FONT}:textfile=titulo.txt:fontsize=112:fontcolor={COR_TITULO}"
    f":x=(w-text_w)/2+sin(t*70)*max(0\\,0.5-t)*26:y=120:line_spacing=6:{CONTORNO}",
    f"drawtext=fontfile={FONT}:textfile=selo.txt:fontsize=40:fontcolor={COR_SELO}"
    f":x=(w-text_w)/2:y=h*0.50:borderw=5:bordercolor=0x000000",
]
for i, (a, b, txt) in enumerate(caps):
    n_ch = len(txt)   # frases longas usam letra menor para caber na faixa de legenda
    tam, larg = (76, 18) if n_ch <= 100 else (66, 21) if n_ch <= 135 else (56, 25)
    open(f"cap{i}.txt", "w").write(textwrap.fill(txt.upper(), larg))
    F.append(f"drawtext=fontfile={FONT}:textfile=cap{i}.txt:fontsize={tam}:fontcolor={COR_TEXTO}"
             f":line_spacing=8:{CONTORNO}:x=(w-text_w)/2"
             f":y=h*0.58+max(0\\,{a:.2f}+0.25-t)*160:alpha=min(1\\,(t-{a:.2f})/0.2)"
             f":enable=between(t\\,{a:.2f}\\,{b:.2f})")

# 4) Trilha de suspense (gerada por código, sem direitos autorais) + "impacto" no primeiro segundo
musica.gerar("_trilha.wav", total + 0.5, sr=SR_MUSICA, mood=S.get("trilha", "sombrio"))
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
print("ok", saida, round(total, 1), "s", len(fatias), "mídias")
