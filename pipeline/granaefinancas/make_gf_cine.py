#!/usr/bin/env python3
"""Vídeo CURTO cinematográfico e escuro do Grana e Finanças (estilo documentário/estoico). Custo zero.

Uso: python3 make_gf_cine.py WORKDIR   (lê WORKDIR/spec.json)

Diferenças para o make_gf.py:
- Narração com a voz Piper FABER dinâmica (aprovada em 30/09): length_scale ~0.84, pausas curtas
  (40% do valor do spec, máx. 0,3 s), presença nos médios e compressão — mais rápida e com som real.
- Imagens reais em TELA CHEIA com tratamento de cinema: contraste, cor fria/esverdeada, vinheta, granulação,
  zoom lento e entrada com "respiro" do preto a cada corte.
- Frases de impacto grandes no meio da tela (ASS), legendas elegantes no terço inferior.
- Trilha cinematográfica escura (musica_cinema.py) com impactos graves nas viradas do roteiro.
- Sem aviso de recomendação de investimento.

spec.json:
{
  "segs": [["texto", pausa_s], ...],
  "voice": {"model": "/tmp/clipes/clipes/pt_BR-jeff-medium.onnx", "length_scale": 1.0,
            "noise_scale": 0.72, "noise_w": 0.9, "pitch_semitons": -1.5},
  "target": [45, 65],
  "clips": [{"seg": 0, "frac": 0.0, "src": "a.mp4", "offset": 1}, ...],   # em ordem; o último vai até o fim
  "overlays": [{"seg": 0, "ate": 1, "linhas": [{"t": "82%", "estilo": "Num", "y": 560}, ...]}],
  "impactos_seg": [0, 3, 9],                                            # "boom" no início dessas frases
  "keywords_gold": [...],
  "output": "video.mp4"
}
Estilos de overlay: Num (número gigante dourado), Tit (frase grande), Sub (texto médio), Handle (@ em caixa dourada).
"""
import json, os, re, subprocess as sp, sys, wave
W = sys.argv[1]; os.chdir(W); S = json.load(open("spec.json"))
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
FPS = 30; FONTS = os.path.abspath(os.path.join(HERE, "..", "fonts"))
HORIZ = S.get("formato", "9:16") == "16:9"          # "16:9" = vídeo longo do YouTube
WW, HH = (1920, 1080) if HORIZ else (1080, 1920)
def run(a): sp.run(a, check=True, capture_output=True)
def dur(f): return float(sp.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))
def wav_dur(f):
    with wave.open(f) as w: return w.getnframes() / w.getframerate()

segs = [(s[0], float(s[1]) if len(s) > 1 else 0.35) for s in S["segs"]]
txt_all = " ".join(t for t, _ in segs)
if re.search(r"\brob[oô]s?\b", txt_all, flags=re.I): sys.exit('ERRO: palavra "robô" é proibida.')
if re.search(r"recomenda[çc][ãa]o de investimento", txt_all, flags=re.I):
    sys.exit("ERRO: este canal não usa o aviso de recomendação de investimento.")

# 1) Narração natural
# Voz aprovada em 30/09: Piper FABER dinâmico (mais rápido, pausas curtas, som presente e real).
# O "voice" dos specs antigos (Jeff lento) é ignorado; use "voz": "custom" no spec para forçar outro "voice".
V = {"model": "/tmp/clipes/clipes/pt_BR-faber-medium.onnx", "length_scale": 0.84, "noise_scale": 0.75,
     "noise_w": 0.85, "pitch_semitons": 0.0, "pausa_fator": 0.4, "pausa_max": 0.3,
     **(S.get("voice", {}) if S.get("voz") == "custom" else {})}
segs = [(t, min(V["pausa_max"], p * V["pausa_fator"])) for t, p in segs]
TARGET = tuple(S.get("target", [45, 65])); TAIL = 3.0
from piper import PiperVoice, SynthesisConfig
PV = PiperVoice.load(V["model"])
def tts(txt, f, ls):
    with wave.open(f, "wb") as w:
        PV.synthesize_wav(txt, w, syn_config=SynthesisConfig(length_scale=ls, noise_scale=V["noise_scale"],
                                                             noise_w_scale=V["noise_w"]))
def synth(ls):
    T = []; t = 0.6; files = []   # 0,6s de respiro antes da 1ª fala
    for i, (txt, pausa) in enumerate(segs):
        f = f"_seg{i:02d}.wav"
        tts(txt, f, ls)
        run(["ffmpeg", "-y", "-i", f, "-af", "silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
             "silenceremove=start_periods=1:start_threshold=-50dB,areverse", "_t.wav"]); os.replace("_t.wav", f)
        d = wav_dur(f); T.append({"text": txt, "start": t, "end": t + d, "pausa": pausa}); files.append(f); t += d + pausa
    return T, files
ls = float(V["length_scale"]); T, files = synth(ls)
for _ in range(2):
    total = T[-1]["end"] + TAIL
    if TARGET[0] <= total <= TARGET[1]: break
    ls = max(0.80, min(0.92, ls * (sum(TARGET) / 2) / total)); T, files = synth(ls)
END = T[-1]["end"] + TAIL
if not (TARGET[0] <= END <= TARGET[1]):
    sys.exit(f"ERRO: {END:.1f}s fora da faixa {TARGET} (length_scale {ls:.2f}). Ajuste o roteiro.")
print(f"length_scale={ls:.2f} duração={END:.1f}s", file=sys.stderr)
sr0 = wave.open(files[0]).getframerate()
with open("_list.txt", "w") as L:
    run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r={sr0}:cl=mono", "-t", "0.6", "_p_ini.wav"])
    L.write("file '_p_ini.wav'\n")
    for j, (f, x) in enumerate(zip(files, T)):
        L.write(f"file '{f}'\n")
        p = f"_p{j:02d}.wav"
        run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r={sr0}:cl=mono", "-t", str(x["pausa"]), p])
        L.write(f"file '{p}'\n")
pitch = 2 ** (V["pitch_semitons"] / 12)
voz_fx = ("aresample=44100," + (f"rubberband=pitch={pitch:.4f}:pitchq=quality," if V["pitch_semitons"] else "") +
          "highpass=f=75,equalizer=f=150:t=q:w=1:g=2,equalizer=f=3000:t=q:w=1.2:g=3,equalizer=f=8000:t=q:w=1:g=1,"
          "acompressor=threshold=-22dB:ratio=4:attack=8:release=150:makeup=3,loudnorm=I=-15:TP=-1.5:LRA=6")
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_list.txt", "-ac", "1", "-af", voz_fx, "_narracao.wav"])

# 2) Trilha cinematográfica escura com impactos nas viradas
from musica_cinema import gerar
imp = [T[i]["start"] - 0.15 for i in S.get("impactos_seg", [0])]
gerar("_musica.wav", END, impactos=imp, seed=S.get("music_seed", 0))
run(["ffmpeg", "-y", "-i", "_narracao.wav", "-i", "_musica.wav", "-filter_complex",
     "[0:a]apad,asplit=2[v][sc];[1:a]volume=0.55[m];[m][sc]sidechaincompress=threshold=0.04:ratio=2.5:attack=40:release=500[md];"
     "[v][md]amix=inputs=2:duration=shortest:normalize=0,alimiter=limit=0.95[a]", "-map", "[a]", "-ac", "2", "_mix.wav"])

# 3) Clipes em tela cheia com tratamento de cinema
def at(seg, frac=0.0):
    x = T[seg]; return 0.0 if seg == 0 and frac == 0 else x["start"] + frac * (x["end"] - x["start"])
C = S["clips"]; st = [at(c["seg"], c.get("frac", 0.0)) for c in C]
cuts = [(c, a, (st[i + 1] if i + 1 < len(C) else END)) for i, (c, a) in enumerate(zip(C, st))]
SW, SH = int(WW * 1.1) // 2 * 2, int(HH * 1.1) // 2 * 2
ZR = S.get("zoom_rate", 0.0007 if not HORIZ else 0.0003)
GRADE = (f"scale={SW}:{SH}:force_original_aspect_ratio=increase,crop={SW}:{SH},"
         f"zoompan=z='min(1.0+{ZR}*on,1.25)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={WW}x{HH}:fps=30,"
         "eq=contrast=1.10:brightness={luz}:saturation=0.65:gamma=1.0,"
         "colorbalance=rs=-0.06:gs=0.03:bs=0.01:rm=-0.04:gm=0.02:bm=0.0:rh=0.02:gh=0.01:bh=-0.03,"
         "vignette=angle=PI/4.2,noise=alls=4:allf=t,"
         "drawbox=x=0:y=0:w=iw:h=ih:color=0x04342C@0.10:t=fill")
parts = []
for k, (c, a, b) in enumerate(cuts):
    d = round(b - a, 3); o = f"_part{k}.mp4"
    fx = GRADE.replace("{luz}", "{luz}").format(luz=-0.03 + c.get("luz", 0.0)) + f",fade=t=in:st=0:d={0.35 if k else 0.8}:color=black"
    if k == len(cuts) - 1: fx += f",fade=t=out:st={max(0, d - 0.8):.2f}:d=0.8:color=black"
    off = float(c.get("offset", 1.0)); sd = dur(c["src"])
    if off > sd - 1.5: off = off % max(1.0, sd - 1.5)   # offset maior que o clipe: dá a volta
    run(["ffmpeg", "-y", "-stream_loop", "-1", "-ss", f"{off:.2f}", "-i", c["src"], "-vf", f"fps=30,{fx},setsar=1",
         "-an", "-t", str(d), "-r", str(FPS), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", o])
    parts.append(o)
open("_parts.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_parts.txt", "-c", "copy", "_video.mp4"])

# 4) Texto: frases de impacto + legendas + selo
def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
FMT_STYLES = {
 False: """Style: Cap,Montserrat Thin ExtraBold,66,&H00FFFFFF,&H00FFFFFF,&H00100C02,&H78000000,0,0,0,0,100,100,1,0,1,5,3,2,80,80,330,1
Style: Brand,Montserrat Thin ExtraBold,30,&H004AB8E8,&H004AB8E8,&H00100C02,&H00000000,0,0,0,0,100,100,6,0,1,2,0,8,40,40,80,1
Style: Num,Anton,330,&H004AB8E8,&H004AB8E8,&H00100C02,&H96000000,0,0,0,0,100,100,2,0,1,6,6,5,40,40,0,1
Style: Tit,Anton,140,&H00FFFFFF,&H00FFFFFF,&H00100C02,&H96000000,0,0,0,0,100,100,2,0,1,6,5,5,60,60,0,1
Style: Sub,Montserrat Thin ExtraBold,66,&H00FFFFFF,&H00FFFFFF,&H00100C02,&H96000000,0,0,0,0,100,100,1,0,1,4,3,5,70,70,0,1
Style: Kick,Montserrat Thin ExtraBold,44,&H004AB8E8,&H004AB8E8,&H00100C02,&H96000000,0,0,0,0,100,100,10,0,1,3,2,5,60,60,0,1
Style: Handle,Montserrat Thin ExtraBold,64,&H002C3404,&H002C3404,&H004AB8E8,&H004AB8E8,0,0,0,0,100,100,1,0,3,22,0,5,60,60,0,1""",
 True: """Style: Cap,Montserrat Thin ExtraBold,52,&H00FFFFFF,&H00FFFFFF,&H00100C02,&H78000000,0,0,0,0,100,100,1,0,1,4,2,2,200,200,90,1
Style: Brand,Montserrat Thin ExtraBold,24,&H004AB8E8,&H004AB8E8,&H00100C02,&H00000000,0,0,0,0,100,100,6,0,1,2,0,8,40,40,40,1
Style: Num,Anton,300,&H004AB8E8,&H004AB8E8,&H00100C02,&H96000000,0,0,0,0,100,100,2,0,1,6,6,5,40,40,0,1
Style: Tit,Anton,130,&H00FFFFFF,&H00FFFFFF,&H00100C02,&H96000000,0,0,0,0,100,100,2,0,1,6,5,5,120,120,0,1
Style: Sub,Montserrat Thin ExtraBold,56,&H00FFFFFF,&H00FFFFFF,&H00100C02,&H96000000,0,0,0,0,100,100,1,0,1,4,3,5,200,200,0,1
Style: Kick,Montserrat Thin ExtraBold,38,&H004AB8E8,&H004AB8E8,&H00100C02,&H96000000,0,0,0,0,100,100,12,0,1,3,2,5,60,60,0,1
Style: Handle,Montserrat Thin ExtraBold,56,&H002C3404,&H002C3404,&H004AB8E8,&H004AB8E8,0,0,0,0,100,100,1,0,3,20,0,5,60,60,0,1"""}
head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {WW}
PlayResY: {HH}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
{FMT_STYLES[HORIZ]}

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
GOLD = "&H4AB8E8&"
kg = "|".join(map(re.escape, sorted(S.get("keywords_gold", []), key=len, reverse=True)))
B = r"(?<![A-ZÀ-Ý0-9])"; E = r"(?![A-ZÀ-Ý0-9])"
def gold(x): return re.sub(f"{B}({kg}){E}", r"{\\c" + GOLD + r"}\1{\\c&HFFFFFF&}", x) if kg else x
L = [f"Dialogue: 0,{ts(0)},{ts(END)},Brand,,0,0,0,,GRANA E FINANÇAS"]
cover = []   # intervalos com frase de impacto na tela (a legenda sobe um pouco para não brigar)
for ov in S.get("overlays", []):
    a = at(ov["seg"], ov.get("frac", 0.0)) if ov["seg"] else 0.0
    b = T[ov.get("ate", ov["seg"])]["end"] + T[ov.get("ate", ov["seg"])]["pausa"] * 0.9
    for i, ln in enumerate(ov["linhas"]):
        est = ln.get("estilo", "Tit"); y = ln.get("y", 760 if not HORIZ else 480); x = ln.get("x", WW // 2)
        ln = {**ln, "t": ln["t"].replace("\n", "\\N")}
        txt = ln["t"] if est in ("Num", "Handle", "Kick") else gold(ln["t"].upper() if est == "Tit" else ln["t"])
        pop = r"\t(0,160,\fscx104\fscy104)\t(160,320,\fscx100\fscy100)" if est in ("Num", "Tit") else ""
        L.append(f"Dialogue: 3,{ts(a + ln.get('t0', 0))},{ts(b)},{est},,0,0,0,,{{\\an5\\pos({x},{y})\\fad(250,200){pop}}}{txt}")
    cover.append((a, b))
for s in T:
    words = s["text"].split(); ch = []; cur = []
    for wd in words:
        cur.append(wd)
        if len(cur) >= 4 or (re.search(r"[,.:?!…]$", wd) and len(cur) >= 2): ch.append(" ".join(cur)); cur = []
    if cur:
        if ch and len(cur) == 1: ch[-1] += " " + cur[0]
        else: ch.append(" ".join(cur))
    tot = sum(len(c) for c in ch); t0 = s["start"]; span = s["end"] - s["start"]
    for c in ch:
        d = span * len(c) / tot
        L.append(f"Dialogue: 1,{ts(t0)},{ts(t0 + d)},Cap,,0,0,0,,{{\\fad(80,60)}}{gold(c.upper())}"); t0 += d
open("_legendas.ass", "w").write(head + "\n".join(L) + "\n")
out = S.get("output", "video.mp4")
run(["ffmpeg", "-y", "-i", "_video.mp4", "-i", "_mix.wav", "-vf", f"ass=_legendas.ass:fontsdir={FONTS}",
     "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "22", "-maxrate", "7M", "-bufsize", "14M", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out])
# 5) CAPA (Reels/Short): quadro do vídeo + título grande na faixa central (aparece inteira no grid 3:4 do perfil)
capa = os.path.splitext(out)[0] + "_capa.jpg"
tc = min(END - 0.5, (cover[0][0] + cover[0][1]) / 2) if cover else min(2.0, END / 2)
run(["ffmpeg", "-y", "-ss", f"{tc:.2f}", "-i", "_video.mp4", "-frames:v", "1", "_capa_bg.png"])
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
im = ImageEnhance.Brightness(Image.open("_capa_bg.png").convert("RGB")).enhance(0.55)
if S.get("capa"):
    d = ImageDraw.Draw(im, "RGBA"); words = S["capa"].upper().split(); lines = []; cur = ""
    fz = 120 if not HORIZ else 110; f = ImageFont.truetype(os.path.join(FONTS, "Anton-Regular.ttf"), fz)
    for wd in words:
        if d.textlength((cur + " " + wd).strip(), font=f) > WW * 0.84: lines.append(cur); cur = wd
        else: cur = (cur + " " + wd).strip()
    lines.append(cur); lh = int(fz * 1.12); y0 = HH // 2 - lh * len(lines) // 2
    d.rectangle([0, y0 - 50, WW, y0 + lh * len(lines) + 40], fill=(4, 52, 44, 200))
    for i, ln in enumerate(lines):
        d.text((WW // 2, y0 + i * lh + lh // 2), ln, font=f, anchor="mm",
               fill=(232, 184, 74) if i == 0 else (255, 255, 255))
    d.text((WW // 2, y0 + lh * len(lines) + 90), "@granaefinancas", anchor="mm",
           font=ImageFont.truetype(os.path.join(FONTS, "Montserrat-ExtraBold.ttf"), 44), fill=(232, 184, 74))
im.save(capa, quality=92)
json.dump([{"i": i, "start": round(x["start"], 2), "end": round(x["end"], 2), "text": x["text"]} for i, x in enumerate(T)],
          open("_tempos.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({"output": out, "capa": capa, "duration": dur(out), "size_mb": round(os.path.getsize(out) / 1e6, 1), "length_scale": round(ls, 2)}))
