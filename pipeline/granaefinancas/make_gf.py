#!/usr/bin/env python3
"""Monta o vídeo CURTO (Reels/Shorts) do Grana e Finanças a partir de WORKDIR/spec.json. Custo zero.

Uso: python3 make_gf.py WORKDIR
spec.json:
{
  "segs": [["intro","..."], ...],        # seções, em ordem: intro, meio, recap, final
  "target": [45, 60],                    # faixa de duração em segundos (ajusta a velocidade da voz)
  "intro_scene": {"pct":82, "texto_pct":"...", "badge":"...", "frase":"...", "fonte":"..."},
  "recap_scene": {"titulo":"3 HÁBITOS\\nQUE MUDAM O JOGO", "itens":["...","...","..."], "destaque":"..."},
  "clips_meio": ["a.mp4","b.mp4", ...],  # clipes reais (um por frase do meio, na ordem); .png também serve
  "clip_offset": {"a.mp4": 2},
  "keywords_gold": [...], "keywords_coral": [...],
  "output": "video.mp4"
}
Cenas: intro = estatística animada (sincronizada com a narração), meio = clipes reais com fundo desfocado
esverdeado, recap = lista animada item a item, final = cartão @granaefinancas. Legendas Montserrat, palavras-chave
em dourado/coral. Selo "GRANA E FINANÇAS" no topo dos clipes.
"""
import json, os, re, subprocess as sp, sys
W = sys.argv[1]; os.chdir(W); S = json.load(open("spec.json"))
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
from cenas import cena_estatistica, cena_lista, cena_final
FPS = 30; FONTS = os.path.abspath(os.path.join(HERE, "..", "fonts"))
def run(a): sp.run(a, check=True, capture_output=True)
def dur(f): return float(sp.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))

txt_all = " ".join(t for _, t in S["segs"])
if re.search(r"\brob[oô]s?\b", txt_all, flags=re.I): sys.exit('ERRO: palavra "robô" é proibida.')

# 1) Narração (Kokoro pm_santa, acelerada) com ajuste automático para a faixa alvo
from kokoro_onnx import Kokoro
import soundfile as sf
KK = Kokoro("/tmp/kokoro/kokoro-v1.0.onnx", "/tmp/kokoro/voices-v1.0.bin")
VOICE = S.get("voice", "pm_santa"); TARGET = tuple(S.get("target", [45, 60])); GAP = 0.18; TAIL = 1.6
PRON = S.get("pronuncia", {})
def falado(t):
    for a, b in PRON.items(): t = re.sub(rf"\b{re.escape(a)}\b", b, t, flags=re.I)
    return t
def synth(speed):
    T = []; t = 0.0; files = []
    for i, (sec, txt) in enumerate(S["segs"]):
        f = f"_seg{i:02d}.wav"
        a, sr = KK.create(falado(txt), voice=VOICE, speed=speed, lang="pt-br"); sf.write(f, a, sr)
        d = len(a) / sr; T.append({"sec": sec, "text": txt, "start": t, "end": t + d}); files.append(f); t += d + GAP
    return T, files
speed = float(S.get("speed", 1.1)); T, files = synth(speed)
mid = sum(TARGET) / 2
for _ in range(3):
    total = T[-1]["end"] + TAIL
    if TARGET[0] <= total <= TARGET[1]: break
    speed = max(1.05, min(1.35, speed * (total / mid))); T, files = synth(speed)
END = T[-1]["end"] + TAIL
if not (TARGET[0] <= END <= TARGET[1]):
    sys.exit(f"ERRO: {END:.1f}s fora da faixa {TARGET} (velocidade {speed:.2f}). Ajuste o tamanho do roteiro.")
print(f"voz={VOICE} speed={speed:.2f} duração={END:.1f}s", file=sys.stderr)
run(["ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=24000:cl=mono", "-t", str(GAP), "_gap.wav"])
with open("_list.txt", "w") as L:
    for j, f in enumerate(files):
        L.write(f"file '{f}'\n")
        if j < len(files) - 1: L.write("file '_gap.wav'\n")
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_list.txt", "-ar", "44100", "-ac", "1", "_narracao.wav"])

# 2) Trilha (gerada por código) com ducking
from musica import gerar
gerar("_musica.wav", END, mood=S.get("music_mood", "alegre"), seed=S.get("music_seed", 0))
run(["ffmpeg", "-y", "-i", "_narracao.wav", "-i", "_musica.wav", "-filter_complex",
     "[0:a]aresample=44100,apad,asplit=2[v][sc];[1:a]volume=0.30[m];[m][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[md];[v][md]amix=inputs=2:duration=shortest:normalize=0,alimiter=limit=0.95[a]",
     "-map", "[a]", "-ac", "1", "_mix.wav"])

# 3) Cortes por seção
sec = lambda s: [x for x in T if x["sec"] == s]
I, M, R, F = sec("intro"), sec("meio"), sec("recap"), sec("final")
cuts = []  # (tipo, início, fim, extra)
cuts.append(("intro", 0.0, M[0]["start"], None))
clips = S["clips_meio"]
groups = [[] for _ in clips]
for i, x in enumerate(M): groups[min(len(clips) - 1, i * len(clips) // len(M))].append(x)
for c, g in zip(clips, groups):
    if g: cuts.append(("clip", g[0]["start"], None, c))
cuts.append(("recap", R[0]["start"], None, None)); cuts.append(("final", F[0]["start"], None, None))
cuts = [(k, a, (cuts[i + 1][1] if i + 1 < len(cuts) else END), e) for i, (k, a, _, e) in enumerate(cuts)]

parts = []
for k, (kind, a, b, extra) in enumerate(cuts):
    d = round(b - a, 3); o = f"_part{k}.mp4"
    if kind == "intro":
        sc = S.get("intro_scene", {})
        tb = I[1]["start"] if len(I) > 1 else 2.0; tf = I[2]["start"] if len(I) > 2 else tb + 2
        cena_estatistica(d, tb, tf, o, "_intro_final.png", **sc)
    elif kind == "recap":
        sc = S["recap_scene"]; n = len(sc["itens"])
        starts = [x["start"] - a for x in R][-n:] if len(R) >= n else [0.8 + 2.2 * i for i in range(n)]
        cena_lista(d, sc["titulo"], sc["itens"], starts, o, "_recap_final.png", destaque=sc.get("destaque"))
    elif kind == "final":
        cena_final(d, o, **S.get("final_scene", {}))
    elif extra.lower().endswith((".mp4", ".mov", ".webm")):
        off = str(S.get("clip_offset", {}).get(extra, 1.0))
        run(["ffmpeg", "-y", "-stream_loop", "-1", "-ss", off, "-i", extra, "-filter_complex",
             f"[0:v]fps={FPS},split[a][b];"
             "[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:2,"
             "drawbox=x=0:y=0:w=iw:h=ih:color=0x04342C@0.55:t=fill[bg];"
             "[b]scale=-2:1180,crop='min(iw,1080)':1180,zoompan=z='1.0+0.0006*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1180:fps=30[fg];"
             "[bg][fg]overlay=(W-w)/2:(H-h)/2-140,drawbox=x=0:y=(ih/2)-140-590-6:w=iw:h=6:color=0xE8B84A@0.9:t=fill,"
             "drawbox=x=0:y=(ih/2)-140+590:w=iw:h=6:color=0xE8B84A@0.9:t=fill,setsar=1[v]",
             "-map", "[v]", "-an", "-t", str(d), "-r", str(FPS), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", o])
    else:
        n = int(round(d * FPS))
        run(["ffmpeg", "-y", "-loop", "1", "-i", extra, "-vf",
             f"scale=2160:3840:force_original_aspect_ratio=increase,crop=2160:3840,zoompan=z='1.0+0.0012*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS}",
             "-t", str(d), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", o])
    parts.append(o)
open("_parts.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_parts.txt", "-c", "copy", "_video.mp4"])

# 4) Legendas (ASS) + selo da marca no topo dos clipes
def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat Thin ExtraBold,70,&H00FFFFFF,&H00FFFFFF,&H00221A04,&H96000000,0,0,0,0,100,100,0,0,1,7,2,2,70,70,250,1
Style: Brand,Montserrat Thin ExtraBold,36,&H004AB8E8,&H004AB8E8,&H00221A04,&H00000000,0,0,0,0,100,100,3,0,1,3,0,8,40,40,90,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
GOLD, CORAL = "&H4AB8E8&", "&H5C76E8&"
kg = "|".join(map(re.escape, sorted(S.get("keywords_gold", []), key=len, reverse=True)))
kc = "|".join(map(re.escape, sorted(S.get("keywords_coral", []), key=len, reverse=True)))
B = r"(?<![A-ZÀ-Ý0-9])"; E = r"(?![A-ZÀ-Ý0-9])"
L = []
for kind, a, b, _ in cuts:
    if kind == "clip": L.append(f"Dialogue: 1,{ts(a)},{ts(b)},Brand,,0,0,0,,GRANA E FINANÇAS")
for s in T:
    ch = []; cur = []
    for wd in s["text"].split():
        cur.append(wd)
        if len(cur) >= 4 or (re.search(r"[,.:?!]$", wd) and len(cur) >= 2): ch.append(" ".join(cur)); cur = []
    if cur:
        if ch and len(cur) == 1: ch[-1] += " " + cur[0]
        else: ch.append(" ".join(cur))
    tot = sum(len(c) for c in ch); t0 = s["start"]; span = s["end"] - s["start"]
    for c in ch:
        d = span * len(c) / tot; x = c.upper()
        if kg: x = re.sub(f"{B}({kg}){E}", r"{\\c" + GOLD + r"}\1{\\c&HFFFFFF&}", x)
        if kc: x = re.sub(f"{B}({kc}){E}", r"{\\c" + CORAL + r"}\1{\\c&HFFFFFF&}", x)
        L.append(f"Dialogue: 0,{ts(t0)},{ts(t0 + d)},Cap,,0,0,0,,{{\\fad(60,0)}}{x}"); t0 += d
open("_legendas.ass", "w").write(head + "\n".join(L) + "\n")
out = S.get("output", "video.mp4")
run(["ffmpeg", "-y", "-i", "_video.mp4", "-i", "_mix.wav", "-vf", f"ass=_legendas.ass:fontsdir={FONTS}",
     "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "22", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out])
json.dump([{"sec": x["sec"], "start": round(x["start"], 2), "end": round(x["end"], 2), "text": x["text"]} for x in T],
          open("_tempos.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({"output": out, "duration": dur(out), "size_mb": round(os.path.getsize(out) / 1e6, 1), "speed": round(speed, 2)}))
