#!/usr/bin/env python3
"""Monta um vídeo de receita da @delíciadajoanna (TikTok 9:16, custo zero).

Uso: python3 make_joanna.py WORKDIR     (lê WORKDIR/spec.json)
spec.json:
{
 "titulo": "Rösti de batata com queijo",          # aparece só no início, pequeno e elegante
 "pronuncia": {"Rösti": "Rôsti"},                 # troca só na voz (opcional)
 "segs": [                                         # 1 frase por item, na ordem da narração
   {"texto": "...", "visual": "rosti-pronto.png"},            # foto (Ken Burns suave)
   {"texto": "...", "visual": "clip.mp4", "offset": 2},       # clipe real (fundo desfocado + vídeo no centro)
   {"texto": "...", "visual": "batata.png", "chip": "2 batatas grandes"},   # ingrediente: etiqueta curta
   {"texto": "...", "visual": "clip.mp4", "passo": 1},        # passo numerado
   {"texto": "...", "visual": "rosti-pronto.png", "final": true}  # cartão final (Salva + Segue)
 ],
 "destaques": ["CROCANTE", "QUEIJO"],            # palavras da legenda em rosa (opcional)
 "output": "video.mp4"
}
Regras de estilo: paleta suave (creme, rosa-blush, sálvia), pouquíssimo texto na tela, legenda SEMPRE.
Duração ajustada para 61–72 s (voz Kokoro pf_dora, suave)."""
import json, os, re, subprocess as sp, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__)); FONTS = os.path.join(HERE, "..", "fonts")
CREAM, BLUSH, SAGE, COCOA = (255, 248, 240), (244, 199, 195), (168, 191, 163), (90, 64, 56)
WD = sys.argv[1]; os.chdir(WD); S = json.load(open("spec.json"))
def run(a): sp.run(a, check=True, capture_output=True)
def dur(f): return float(sp.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
def font(name, size): return ImageFont.truetype(os.path.join(FONTS, name), size)

# 1) narração (pf_dora, suave) com duração 61–72 s
from kokoro_onnx import Kokoro
import soundfile as sf
KK = Kokoro("/tmp/kokoro/kokoro-v1.0.onnx", "/tmp/kokoro/voices-v1.0.bin")
PRON = S.get("pronuncia", {}); GAP = 0.35
def falado(t):
    for a, b in PRON.items(): t = re.sub(rf"\b{re.escape(a)}\b", b, t)
    return t
def synth(speed):
    T, t = [], 0.0
    for i, s in enumerate(S["segs"]):
        a, sr = KK.create(falado(s["texto"]), voice="pf_dora", speed=speed, lang="pt-br"); sf.write(f"_v{i:02d}.wav", a, sr)
        d = len(a) / sr; T.append((t, t + d)); t += d + GAP
    return T
speed = float(S.get("speed", 0.95)); T = synth(speed)
for _ in range(3):
    tot = T[-1][1] + 1.5
    if 61 <= tot <= 72: break
    speed = max(0.85, min(1.15, speed * tot / 66)); T = synth(speed)
tot = T[-1][1] + 1.5
if not 61 <= tot <= 72: sys.exit(f"ERRO: {tot:.1f}s com speed {speed:.2f}; ajuste o roteiro (~150–175 palavras)")
print(f"voz pf_dora speed={speed:.2f} duração={tot:.1f}s", file=sys.stderr)
run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(GAP), "_gap.wav"])
with open("_l.txt", "w") as L:
    for i in range(len(T)):
        L.write(f"file '_v{i:02d}.wav'\n")
        if i < len(T) - 1: L.write("file '_gap.wav'\n")
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_l.txt", "-af", "apad=pad_dur=1.5", "-ar", "44100", "-ac", "1", "_voz.wav"])
sys.path.insert(0, HERE); from musica_suave import gerar
gerar("_mus.wav", tot, seed=S.get("seed", 0))
run(["ffmpeg", "-y", "-i", "_voz.wav", "-i", "_mus.wav", "-filter_complex",
     "[0:a]asplit=2[v][sc];[1:a]volume=0.30[m];[m][sc]sidechaincompress=threshold=0.03:ratio=3:attack=30:release=400[md];[v][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]",
     "-map", "[a]", "-ac", "1", "_mix.wav"])

# 2) camadas de texto mínimas (PNG transparentes)
def pill(d, cx, cy, text, f, fg=COCOA, bg=CREAM + (235,), padx=46, pady=22):
    w = d.textlength(text, font=f); bb = f.getbbox(text); h = bb[3] - bb[1]
    d.rounded_rectangle([cx - w / 2 - padx, cy - h / 2 - pady, cx + w / 2 + padx, cy + h / 2 + pady + 6], 60, fill=bg)
    d.text((cx, cy + 3), text, font=f, fill=fg, anchor="mm")
def overlay(i, s):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if i == 0 and S.get("titulo"):
        pill(d, W / 2, 250, S["titulo"], font("PlayfairDisplay-BoldItalic.ttf", 58))
    if s.get("chip"):
        pill(d, W / 2, 250, s["chip"], font("Montserrat-SemiBold.ttf", 52))
    if s.get("passo"):
        d.ellipse([W / 2 - 78, 172, W / 2 + 78, 328], fill=CREAM + (240,), outline=BLUSH + (255,), width=8)
        d.text((W / 2, 252), str(s["passo"]), font=font("PlayfairDisplay-BoldItalic.ttf", 96), fill=COCOA, anchor="mm")
    if s.get("final"):
        d.rounded_rectangle([110, 520, W - 110, 1030], 60, fill=CREAM + (232,))
        d.text((W / 2, 640), "Delícia da Joanna", font=font("DancingScript-Bold.ttf", 110), fill=COCOA, anchor="mm")
        d.text((W / 2, 790), "Salva pra fazer depois", font=font("Montserrat-SemiBold.ttf", 50), fill=COCOA, anchor="mm")
        d.text((W / 2, 880), "e segue pra mais receitas", font=font("Montserrat-SemiBold.ttf", 42), fill=(150, 120, 110), anchor="mm")
        hx, hy, r = W / 2, 960, 22   # coraçãozinho desenhado
        d.ellipse([hx - 2 * r, hy - r, hx, hy + r], fill=BLUSH); d.ellipse([hx, hy - r, hx + 2 * r, hy + r], fill=BLUSH)
        d.polygon([(hx - 2 * r + 2, hy + 6), (hx + 2 * r - 2, hy + 6), (hx, hy + 2.4 * r)], fill=BLUSH)
    im.save(f"_o{i:02d}.png")

# 3) cenas
parts = []
for i, s in enumerate(S["segs"]):
    a = T[i][0]; b = T[i + 1][0] if i + 1 < len(T) else tot
    d = round(b - a, 3); n = int(round(d * FPS)); o = f"_p{i:02d}.mp4"; overlay(i, s); v = s["visual"]
    if v.lower().endswith((".mp4", ".mov")):
        vf = (f"[0:v]fps={FPS},split[x][y];[x]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=20:2,eq=brightness=0.04:saturation=0.8[bg];"
              f"[y]scale=-2:1180,crop='min(iw,{W})':1180,eq=saturation=0.92:brightness=0.03[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2-60[base];")
        inp = ["-stream_loop", "-1", "-ss", str(s.get("offset", 1)), "-i", v]
    else:
        z = "1.0+0.0009*on" if i % 2 == 0 else "1.08-0.0009*on"
        vf = (f"[0:v]scale=2160:3840:force_original_aspect_ratio=increase:flags=lanczos,crop=2160:3840,unsharp=5:5:0.6,"
              f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n + 2}:s={W}x{H}:fps={FPS},eq=saturation=0.95:brightness=0.02[base];")
        inp = ["-loop", "1", "-i", v]
    vf += "[1:v]format=rgba,fade=t=in:st=0:d=0.35:alpha=1[ov];[base][ov]overlay=0:0,format=yuv420p[v]"
    run(["ffmpeg", "-y", *inp, "-loop", "1", "-i", f"_o{i:02d}.png", "-filter_complex", vf, "-map", "[v]", "-an",
         "-t", str(d), "-r", str(FPS), "-c:v", "libx264", "-crf", "20", o])
    parts.append(o)
open("_parts.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_parts.txt", "-c", "copy", "_video.mp4"])

# 4) legendas SEMPRE (suaves), destaques em rosa
def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat,66,&H00FFFFFF,&H00FFFFFF,&H00384050,&H64384050,-1,0,0,0,100,100,0,0,1,5,2,2,80,80,330,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
DS = "|".join(map(re.escape, sorted(S.get("destaques", []), key=len, reverse=True)))
L = []
for (a, b), s in zip(T, S["segs"]):
    words = s["texto"].split(); ch = [" ".join(words[k:k + 3]) for k in range(0, len(words), 3)]
    if len(ch) > 1 and len(ch[-1].split()) == 1: ch[-2] += " " + ch.pop()
    tt = sum(len(c) for c in ch); t0 = a
    for c in ch:
        dd = (b - a) * len(c) / tt; x = c.upper()
        if DS: x = re.sub(rf"(?<![A-ZÀ-Ý])({DS})(?![A-ZÀ-Ý])", r"{\\c&HC3C7F4&}\1{\\c&HFFFFFF&}", x)
        L.append(f"Dialogue: 0,{ts(t0)},{ts(t0 + dd)},Cap,,0,0,0,,{{\\fad(80,60)}}{x}"); t0 += dd
open("_leg.ass", "w").write(head + "\n".join(L) + "\n")
out = S.get("output", "video.mp4")
# barra de progresso fina no topo (retenção) + legendas
run(["ffmpeg", "-y", "-i", "_video.mp4", "-i", "_mix.wav", "-filter_complex",
     f"[0:v]drawbox=x=0:y=0:w=iw:h=10:color=0xFFF8F0@0.55:t=fill,drawbox=x=0:y=0:w='iw*t/{tot:.2f}':h=10:color=0xF4C7C3@1:t=fill,"
     f"ass=_leg.ass:fontsdir={FONTS}[v]", "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-crf", "22", "-preset", "medium",
     "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out])
print(json.dumps({"output": out, "duration": dur(out), "size_mb": round(os.path.getsize(out) / 1e6, 1)}))
