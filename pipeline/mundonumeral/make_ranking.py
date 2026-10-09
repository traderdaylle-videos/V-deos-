#!/usr/bin/env python3
"""Vídeo de ranking animado do @rankingcuriosos (TikTok 9:16, custo zero).

Uso: python3 make_ranking.py WORKDIR   (lê WORKDIR/spec.json)
spec.json:
{
 "titulo": "BIG MAC MAIS CARO",           # faixa pequena no topo (o tema)
 "subtitulo": "preço em dólares",
 "unidade": "US$ ", "decimais": 2,
 "destaque": "Brasil",                      # item destacado em verde (identificação do público)
 "fonte": "Fonte: The Economist, 2025",
 "intro": ["frase do gancho", "..."],       # falas antes do ranking (a tela mostra o suspense)
 "itens": [ {"pos":10,"nome":"Japão","valor":3.11,"fala":"Em décimo lugar, Japão: três dólares e onze."}, ... até pos 1 ],
 "outro": ["pergunta para comentar", "segue pra mais rankings"],
 "output": "video.mp4"
}
Contagem regressiva do 10º ao 1º (suspense até o fim). Voz: pm_santa mais grave (pitch -10%).
Duração alvo 61–72 s."""
import json, math, os, re, subprocess as sp, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__)); FONTS = os.path.join(HERE, "..", "fonts")
NAVY, NAVY2, GOLD, GOLD2, CREAM, GREEN = (8, 12, 30), (22, 20, 48), (245, 184, 61), (255, 215, 120), (240, 236, 225), (60, 200, 120)
WD = sys.argv[1]; os.chdir(WD); S = json.load(open("spec.json"))
def run(a): sp.run(a, check=True, capture_output=True)
def dur(f): return float(sp.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
F = lambda n, s: ImageFont.truetype(os.path.join(FONTS, n), s)

# ---------- 1) narração (Santa mais grave) ----------
from kokoro_onnx import Kokoro
import soundfile as sf
KK = Kokoro("/tmp/kokoro/kokoro-v1.0.onnx", "/tmp/kokoro/voices-v1.0.bin")
falas = [("intro", t, None) for t in S["intro"]] + [("item", it["fala"], k) for k, it in enumerate(S["itens"])] + [("outro", t, None) for t in S["outro"]]
PITCH = float(S.get("pitch", 0.90)); GAP = 0.25
import re
def fonemas(txt):
    """Corrige vícios do espeak pt-BR que soam como 'vírgula no meio da palavra':
    - vogal fantasma após R antes de consoante (quar-ə-to, Ar-ə-gentina, ter-ə-ceiro);
    - acento secundário (ˌ), que faz o modelo alongar/quebrar sílabas no meio da frase."""
    p = KK.tokenizer.phonemize(txt, "pt-br")
    p = re.sub(r"ɾə(?=[^\saeiouɐɛɔæʊyɪ.,;:!?])", "ɾ", p)
    return p.replace("ˌ", "")
def synth(speed):
    T, t = [], 0.0
    for i, (kind, txt, k) in enumerate(falas):
        a, sr = KK.create(fonemas(txt), voice="pm_santa", speed=speed, is_phonemes=True); sf.write(f"_r{i:02d}.wav", a, sr)
        # voz mais grave com rubberband (mesmo timbre do asetrate, sem os 'engasgos' do atempo)
        run(["ffmpeg", "-y", "-i", f"_r{i:02d}.wav", "-af", f"rubberband=pitch={PITCH},equalizer=f=120:t=q:w=1:g=3", f"_s{i:02d}.wav"])
        d = dur(f"_s{i:02d}.wav"); T.append((t, t + d)); t += d + GAP
    return T
speed = float(S.get("speed", 1.28)); T = synth(speed)
for _ in range(3):
    tot = T[-1][1] + 1.2
    print(f"  speed={speed:.2f} -> {tot:.1f}s", file=sys.stderr)
    if 61 <= tot <= 72: break
    speed = max(1.18, min(1.32, speed * tot / 66)); T = synth(speed)  # acima de ~1.33 o Kokoro engole sílabas
tot = T[-1][1] + 1.2
if not 61 <= tot <= 72: sys.exit(f"ERRO: {tot:.1f}s (speed {speed:.2f}); ajuste o roteiro")
print(f"voz santa-grave speed={speed:.2f} duração={tot:.1f}s", file=sys.stderr)
run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(GAP), "_gap.wav"])
with open("_l.txt", "w") as L:
    for i in range(len(T)):
        L.write(f"file '_s{i:02d}.wav'\n")
        if i < len(T) - 1: L.write("file '_gap.wav'\n")
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_l.txt", "-af", "apad=pad_dur=1.2", "-ar", "44100", "-ac", "1", "_voz.wav"])
sys.path.insert(0, os.path.join(HERE, "..")); from musica import gerar
gerar("_mus.wav", tot, mood=S.get("music_mood", "alegre"))
# "whoosh"/tique a cada revelação (efeito sonoro gerado)
sr = 44100; fx = np.zeros(int(tot * sr))
for i, (kind, _, k) in enumerate(falas):
    if kind == "item":
        s0 = int(T[i][0] * sr); n = int(0.35 * sr); tt = np.arange(n) / sr
        fx[s0:s0 + n] += 0.25 * np.sin(2 * np.pi * (300 + 900 * tt) * tt) * np.exp(-tt * 9)
sf.write("_fx.wav", fx.astype(np.float32), sr)
run(["ffmpeg", "-y", "-i", "_voz.wav", "-i", "_mus.wav", "-i", "_fx.wav", "-filter_complex",
     "[0:a]asplit=2[v][sc];[1:a]volume=0.34[m];[m][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[md];[v][md][2:a]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.95[a]",
     "-map", "[a]", "-ac", "1", "_mix.wav"])

# ---------- 2) quadros ----------
itens = S["itens"]; n = len(itens); vmax = max(i["valor"] for i in itens)
item_t = {k: T[i][0] for i, (kind, _, k) in enumerate(falas) if kind == "item"}
t_outro = T[len(S["intro"]) + n][0]
U = S.get("unidade", ""); DEC = S.get("decimais", 0)
def fmt(v): return (U + f"{v:,.{DEC}f}").replace(",", "X").replace(".", ",").replace("X", ".")

# fundo: degradê navy + "luzes de cidade" (pontos dourados) estáticos
rng = np.random.default_rng(3)
bg = Image.new("RGB", (W, H)); arr = np.zeros((H, W, 3), np.float32)
for y in range(H):
    k = y / H; arr[y] = np.array(NAVY) * (1 - k) + np.array(NAVY2) * k
bg = Image.fromarray(arr.astype(np.uint8)); d = ImageDraw.Draw(bg)
for _ in range(900):
    x, y = rng.integers(0, W), rng.integers(0, H); r = rng.choice([1, 1, 2])
    d.ellipse([x - r, y - r, x + r, y + r], fill=(255, 200, 110, 255) if rng.random() < .6 else (120, 170, 255))
bg = bg.filter(ImageFilter.GaussianBlur(1.2))
glow = Image.new("RGB", (W, H), (0, 0, 0)); ImageDraw.Draw(glow).ellipse([-200, 300, W + 200, 1500], fill=(60, 45, 20))
bg = Image.blend(bg, Image.blend(bg, glow.filter(ImageFilter.GaussianBlur(160)), .5), .6)

fT, fS, fNome, fVal, fPos, fBig, fBigV, fSm = F("Anton-Regular.ttf", 92), F("Montserrat-SemiBold.ttf", 34), F("Montserrat-ExtraBold.ttf", 32), F("Montserrat-ExtraBold.ttf", 30), F("Montserrat-ExtraBold.ttf", 32), F("Anton-Regular.ttf", 150), F("Anton-Regular.ttf", 110), F("Montserrat-SemiBold.ttf", 24)
TOP, ROWH = 1000, 62   # lista compacta abaixo do painel de vídeo real
PX, PY, PW, PH = 60, 290, 960, 620   # painel com clipe real (bandeira/cidade/comida)
BARX, BARW = 330, 560
def ease(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3

HOLE = Image.new("L", (W, H), 255); ImageDraw.Draw(HOLE).rounded_rectangle([PX, PY, PX + PW, PY + PH], 40, fill=0)
BGA = bg.convert("RGBA"); BGA.putalpha(HOLE)
if S.get("bg_clip"):   # fundo com CLIPE em movimento ligado ao tema: só um véu leve para dar leitura
    sc = np.zeros((H, W, 4), np.uint8); sc[..., :3] = NAVY
    ys = np.arange(H)[:, None]
    al = np.where(ys < 270, 130, np.where(ys < TOP - 30, 50, 150)).astype(np.uint8)   # título, painel, lista+legenda
    sc[..., 3] = np.broadcast_to(al, (H, W))
    BGA = Image.fromarray(sc, "RGBA"); BGA.putalpha(Image.fromarray(np.minimum(np.array(BGA.getchannel("A")), np.array(HOLE))))
def frame(t):
    im = BGA.copy(); d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle([PX - 4, PY - 4, PX + PW + 4, PY + PH + 4], 44, outline=GOLD + (255,), width=5)
    # título
    d.text((W / 2, 130), S["titulo"], font=fT, fill=GOLD, anchor="mm")
    d.text((W / 2, 220), S.get("subtitulo", ""), font=fS, fill=CREAM, anchor="mm")
    # linhas do ranking
    for k, it in enumerate(itens):
        pos = it["pos"]; y = TOP + (pos - 1) * ROWH
        t0 = item_t[k]; a = ease((t - t0) / 0.6) if t >= t0 else 0
        hi = it["nome"] == S.get("destaque")
        if a == 0:  # ainda escondido: placeholder "?"
            d.rounded_rectangle([60, y, W - 60, y + ROWH - 14], 18, fill=(255, 255, 255, 18))
            d.text((110, y + (ROWH - 14) / 2), f"{pos}º", font=fPos, fill=(255, 255, 255, 90), anchor="lm")
            d.text((W / 2 + 60, y + (ROWH - 14) / 2), "?", font=fPos, fill=(255, 255, 255, 70), anchor="mm")
            continue
        col = GREEN if hi else (GOLD if pos == 1 else (90, 150, 255))
        d.rounded_rectangle([60, y, W - 60, y + ROWH - 14], 18, fill=(255, 255, 255, 28) if not hi else (60, 200, 120, 45))
        d.text((110, y + (ROWH - 14) / 2), f"{pos}º", font=fPos, fill=GOLD2 if pos <= 3 else CREAM, anchor="lm")
        d.text((190, y + (ROWH - 14) / 2), it["nome"], font=fNome, fill=CREAM, anchor="lm")
        bw = BARW * (it["valor"] / vmax) * a * 0.50
        d.rounded_rectangle([BARX + 150, y + 16, BARX + 150 + max(bw, 6), y + ROWH - 30], 12, fill=col + (255,))
        d.text((W - 80, y + (ROWH - 14) / 2), fmt(it["valor"] * a), font=fVal, fill=CREAM, anchor="rm")
    # cartão grande do item atual (em cima da lista)
    cur = [k for k in range(n) if item_t[k] <= t < (item_t[k + 1] if k + 1 < n else t_outro)]
    if cur and t < t_outro:
        k = cur[0]; it = itens[k]; a = ease((t - item_t[k]) / 0.45); hi = it["nome"] == S.get("destaque")
        sc = 0.85 + 0.15 * a; cy = PY + PH - 110
        card = Image.new("RGBA", (900, 230), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
        cd.rounded_rectangle([0, 0, 899, 229], 36, fill=(GREEN if hi else GOLD) + (245,))
        cd.text((60, 115), f"{it['pos']}", font=fBig, fill=NAVY, anchor="lm")
        nx = 60 + cd.textlength(str(it['pos']), font=fBig) + 4
        cd.text((nx, 60), "º", font=F("Montserrat-ExtraBold.ttf", 64), fill=NAVY, anchor="lt")
        cd.text((560, 78), it["nome"].upper(), font=F("Anton-Regular.ttf", 72), fill=NAVY, anchor="mm")
        cd.text((560, 165), fmt(it["valor"] * a), font=F("Anton-Regular.ttf", 76), fill=NAVY, anchor="mm")
        card = card.resize((int(900 * sc), int(230 * sc)), Image.LANCZOS)
        card.putalpha(card.getchannel("A").point(lambda v: int(v * a)))
        im.paste(card, (int(W / 2 - card.width / 2), int(cy - card.height / 2)), card)
    elif t < (item_t[0] if n else 0):  # suspense do gancho
        pul = 0.5 + 0.5 * abs(math.sin(t * 3))
        d.rounded_rectangle([PX + 90, PY + PH - 170, PX + PW - 90, PY + PH - 50], 30, fill=NAVY + (200,))
        d.text((W / 2, PY + PH - 110), "QUEM FICA EM 1º?", font=F("Montserrat-ExtraBold.ttf", 72), fill=GOLD2 + (int(150 + 105 * pul),), anchor="mm")
    if t >= t_outro:  # final: pergunta + seguir
        a = ease((t - t_outro) / 0.5)
        d.rounded_rectangle([PX + 30, PY + PH - 210, PX + PW - 30, PY + PH - 30], 36, fill=GOLD + (int(240 * a),))
        d.text((W / 2, PY + PH - 150), "COMENTA", font=F("Anton-Regular.ttf", 64), fill=NAVY + (int(255 * a),), anchor="mm")
        d.text((W / 2, PY + PH - 75), "qual ranking você quer ver amanhã?", font=F("Montserrat-ExtraBold.ttf", 38), fill=NAVY + (int(255 * a),), anchor="mm")
    d.text((W / 2, H - 45), S.get("fonte", ""), font=fSm, fill=(200, 200, 215, 200), anchor="mm")
    d.text((W / 2, H - 80), "@rankingcuriosos", font=F("Montserrat-ExtraBold.ttf", 30), fill=GOLD2 + (220,), anchor="mm")
    return im

# trilha do painel: clipes reais por trecho (intro -> comida/cidade, cada item -> bandeira/cidade do país, final -> clipe final)
segs = []
intro_clips = S.get("clips_intro", []); t_first = item_t[0] if n else t_outro
for j, c in enumerate(intro_clips):
    a0 = t_first * j / len(intro_clips); segs.append((c, a0, t_first * (j + 1) / len(intro_clips)))
for k, it in enumerate(itens):
    segs.append((it["clip"], item_t[k], item_t[k + 1] if k + 1 < n else t_outro))
segs.append((S.get("clip_final", itens[-1]["clip"]), t_outro, tot))
pp = []
for j, (c, a0, b0) in enumerate(segs):
    o = f"_pn{j:02d}.mp4"; dd = round(b0 - a0, 3)
    run(["ffmpeg", "-y", "-stream_loop", "-1", "-ss", "1", "-i", c, "-vf",
         f"fps={FPS},scale={PW}:{PH}:force_original_aspect_ratio=increase,crop={PW}:{PH},eq=saturation=1.1:contrast=1.05,setsar=1",
         "-an", "-t", str(dd), "-r", str(FPS), "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", o])
    pp.append(o)
open("_pn.txt", "w").write("".join(f"file '{x}'\n" for x in pp))
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_pn.txt", "-c", "copy", "_panel.mp4"])
base = (["-stream_loop", "-1", "-i", S["bg_clip"]] if S.get("bg_clip") else ["-f", "lavfi", "-i", f"color=c=0x080C1E:s={W}x{H}:r={FPS}:d={tot:.2f}"])
BGF = (f"[0:v]fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=6:1,eq=brightness=-0.08:saturation=1.05,trim=duration={tot:.2f},setsar=1[bg0];" if S.get("bg_clip") else "[0:v]null[bg0];")
p = sp.Popen(["ffmpeg", "-y", "-loglevel", "error", *base, "-i", "_panel.mp4",
              "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
              "-filter_complex", BGF + f"[bg0][1:v]overlay={PX}:{PY}:shortest=1[b];[b][2:v]overlay=0:0:shortest=1,format=yuv420p[v]",
              "-map", "[v]", "-c:v", "libx264", "-crf", "20", "_video.mp4"], stdin=sp.PIPE)
for i in range(int(math.ceil(tot * FPS))):
    p.stdin.write(frame(i / FPS).tobytes())
p.stdin.close(); p.wait()

# ---------- 3) legendas (sempre) ----------
def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat,64,&H00FFFFFF,&H00FFFFFF,&H001E0C08,&H96000000,-1,0,0,0,100,100,0,0,1,6,2,2,70,70,150,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
L = []
for (a, b), (kind, txt, k) in zip(T, falas):
    w = txt.split(); ch = [" ".join(w[j:j + 3]) for j in range(0, len(w), 3)]
    if len(ch) > 1 and len(ch[-1].split()) == 1: ch[-2] += " " + ch.pop()
    tt = sum(len(c) for c in ch); t0 = a
    for c in ch:
        dd = (b - a) * len(c) / tt; x = c.upper()
        x = re.sub(r"(BRASIL)", r"{\\c&H78C83C&}\1{\\c&HFFFFFF&}", x)
        L.append(f"Dialogue: 0,{ts(t0)},{ts(t0 + dd)},Cap,,0,0,0,,{x}"); t0 += dd
open("_leg.ass", "w").write(head + "\n".join(L) + "\n")
out = S.get("output", "video.mp4")
run(["ffmpeg", "-y", "-i", "_video.mp4", "-i", "_mix.wav", "-vf", f"ass=_leg.ass:fontsdir={FONTS}", "-map", "0:v", "-map", "1:a",
     "-c:v", "libx264", "-crf", "22", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out])
print(json.dumps({"output": out, "duration": dur(out), "size_mb": round(os.path.getsize(out) / 1e6, 1)}))
