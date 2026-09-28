#!/usr/bin/env python3
"""Monta o vídeo CURTO (Reels/Shorts) do Grana e Finanças a partir de WORKDIR/spec.json. Custo zero.

Uso: python3 make_gf.py WORKDIR

Regras de retenção (pesquisa de 27/09/2026) que este motor segue:
- Gancho visual e falado no 1º segundo (número grande já no primeiro quadro).
- Troca de imagem a cada 2–4s: o `timeline` pode cortar no meio de uma frase ("frac").
- Legendas grandes queimadas no vídeo; títulos de capítulo ("1. O CARTÃO") no topo dos clipes.
- 30–45s no total; final pede para ENVIAR o vídeo a alguém (envios pesam mais que curtidas no Instagram).
- Sem aviso de "não é recomendação de investimento" (isso é só do TikTok de trading e da Prime Win).

spec.json:
{
  "segs": [["hook","..."], ...],            # frases na ordem da fala (a seção é livre, só para referência)
  "voice": {"engine":"piper","model":"/tmp/clipes/clipes/pt_BR-jeff-medium.onnx","length_scale":0.85},
  "target": [32, 45],
  "timeline": [                             # o que aparece na tela, em ordem. "seg" = índice da frase onde começa;
    {"seg":0, "tipo":"estatistica", "cena":{...}, "frase_seg":1},     # "frac" (0–0.9) = ponto dentro da frase
    {"seg":2, "tipo":"lista", "titulo":"...", "itens":[...], "itens_seg":[3,5,7]},
    {"seg":3, "tipo":"clipe", "src":"a.mp4", "capitulo":"1. O CARTÃO", "offset":1},
    {"seg":3, "frac":0.5, "tipo":"clipe", "src":"b.mp4", "capitulo":"1. O CARTÃO"},
    {"seg":10, "tipo":"final", "src":"dinheiro.mp4", "linhas":[...]}  # textos sobre clipe REAL de dinheiro
  ],
  "keywords_gold": [...], "keywords_coral": [...],
  "output": "video.mp4"
}
"""
import json, os, re, subprocess as sp, sys, wave
W = sys.argv[1]; os.chdir(W); S = json.load(open("spec.json"))
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
from cenas import cena_estatistica, cena_lista, cena_final_sobre_clipe
FPS = 30; FONTS = os.path.abspath(os.path.join(HERE, "..", "fonts"))
def run(a): sp.run(a, check=True, capture_output=True)
def dur(f): return float(sp.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))

txt_all = " ".join(t for _, t in S["segs"])
if re.search(r"\brob[oô]s?\b", txt_all, flags=re.I): sys.exit('ERRO: palavra "robô" é proibida.')
if re.search(r"recomenda[çc][ãa]o de investimento", txt_all, flags=re.I):
    sys.exit("ERRO: este canal não usa o aviso de recomendação de investimento.")

# 1) Narração — padrão: Piper "jeff" (escolhida pelo usuário para o Grana e Finanças)
V = S.get("voice", {"engine": "piper", "model": "/tmp/clipes/clipes/pt_BR-jeff-medium.onnx", "length_scale": 0.85})
TARGET = tuple(S.get("target", [32, 45])); GAP = 0.12; TAIL = 2.2
PRON = S.get("pronuncia", {})
def falado(t):
    for a, b in PRON.items(): t = re.sub(rf"\b{re.escape(a)}\b", b, t, flags=re.I)
    return t
def wav_dur(f):
    with wave.open(f) as w: return w.getnframes() / w.getframerate()
def synth(rate):
    T = []; t = 0.0; files = []
    for i, (sec, txt) in enumerate(S["segs"]):
        f = f"_seg{i:02d}.wav"
        if V["engine"] == "piper":
            sp.run([sys.executable, "-m", "piper", "-m", V["model"], "-f", f, "--length-scale", f"{rate:.3f}",
                    "--sentence-silence", "0"], input=falado(txt).encode(), check=True, capture_output=True)
            # corta silêncio de início/fim para a fala ficar colada
            run(["ffmpeg", "-y", "-i", f, "-af", "silenceremove=start_periods=1:start_threshold=-45dB,areverse,"
                 "silenceremove=start_periods=1:start_threshold=-45dB,areverse", "_tmp.wav"]); os.replace("_tmp.wav", f)
        else:
            from kokoro_onnx import Kokoro; import soundfile as sf
            KK = Kokoro("/tmp/kokoro/kokoro-v1.0.onnx", "/tmp/kokoro/voices-v1.0.bin")
            a, sr = KK.create(falado(txt), voice=V.get("name", "pm_santa"), speed=1 / rate, lang="pt-br"); sf.write(f, a, sr)
        d = wav_dur(f); T.append({"sec": sec, "text": txt, "start": t, "end": t + d}); files.append(f); t += d + GAP
    return T, files
rate = float(V.get("length_scale", 0.85)); T, files = synth(rate)
mid = sum(TARGET) / 2
for _ in range(3):
    total = T[-1]["end"] + TAIL
    if TARGET[0] <= total <= TARGET[1]: break
    rate = max(0.72, min(1.0, rate * (mid / total))); T, files = synth(rate)
END = T[-1]["end"] + TAIL
if not (TARGET[0] <= END <= TARGET[1]):
    sys.exit(f"ERRO: {END:.1f}s fora da faixa {TARGET} (length_scale {rate:.2f}). Ajuste o tamanho do roteiro.")
print(f"voz={V['engine']} rate={rate:.2f} duração={END:.1f}s", file=sys.stderr)
sr0 = wave.open(files[0]).getframerate()
run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r={sr0}:cl=mono", "-t", str(GAP), "_gap.wav"])
with open("_list.txt", "w") as L:
    for j, f in enumerate(files):
        L.write(f"file '{f}'\n")
        if j < len(files) - 1: L.write("file '_gap.wav'\n")
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_list.txt", "-ar", "44100", "-ac", "1",
     "-af", "loudnorm=I=-15:TP=-1.5:LRA=9", "_narracao.wav"])

# 2) Trilha (gerada por código) com ducking
if S.get("music_mood", "dark") == "dark":   # padrão do canal: trilha dark (credibilidade)
    from musica_dark import gerar as gerar_dark
    gerar_dark("_musica.wav", END, seed=S.get("music_seed", 0))
else:
    from musica import gerar
    gerar("_musica.wav", END, mood=S["music_mood"], seed=S.get("music_seed", 0))
run(["ffmpeg", "-y", "-i", "_narracao.wav", "-i", "_musica.wav", "-filter_complex",
     "[0:a]aresample=44100,apad,asplit=2[v][sc];[1:a]volume=0.28[m];[m][sc]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[md];[v][md]amix=inputs=2:duration=shortest:normalize=0,alimiter=limit=0.95[a]",
     "-map", "[a]", "-ac", "1", "_mix.wav"])

# 3) Linha do tempo visual
def at(seg, frac=0.0):
    x = T[seg]; return 0.0 if seg == 0 and frac == 0 else x["start"] + frac * (x["end"] - x["start"])
TL = S["timeline"]
starts = [at(e["seg"], e.get("frac", 0.0)) for e in TL]
cuts = [(e, a, (starts[i + 1] if i + 1 < len(TL) else END)) for i, (e, a) in enumerate(zip(TL, starts))]

CLIP_FILTER = ("[0:v]fps=30,split[a][b];"
               "[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:2,"
               "drawbox=x=0:y=0:w=iw:h=ih:color=0x04342C@0.55:t=fill[bg];"
               "[b]scale=-2:1180,crop='min(iw,1080)':1180[fg];"
               "[bg][fg]overlay=(W-w)/2:(H-h)/2-140,drawbox=x=0:y=(ih/2)-140-590-6:w=iw:h=6:color=0xE8B84A@0.9:t=fill,"
               "drawbox=x=0:y=(ih/2)-140+590:w=iw:h=6:color=0xE8B84A@0.9:t=fill,setsar=1[v]")
parts = []
for k, (e, a, b) in enumerate(cuts):
    d = round(b - a, 3); o = f"_part{k}.mp4"; tipo = e["tipo"]
    if tipo == "estatistica":
        fs = e.get("frase_seg"); tf = (T[fs]["start"] - a) if fs is not None else 99
        cena_estatistica(d, 99, tf, o, "_est.png", **e.get("cena", {}))
    elif tipo == "lista":
        tempos = e.get("tempos") or [T[s]["start"] - a for s in e["itens_seg"]]
        cena_lista(d, e["titulo"], e["itens"], tempos, o, "_lista.png", destaque=e.get("destaque"))
    elif tipo == "clipe":
        run(["ffmpeg", "-y", "-stream_loop", "-1", "-ss", str(e.get("offset", 1.0)), "-i", e["src"], "-filter_complex",
             CLIP_FILTER, "-map", "[v]", "-an", "-t", str(d), "-r", str(FPS), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", o])
    elif tipo == "final":
        # clipe REAL de dinheiro em tela cheia (levemente escurecido/esverdeado) + textos animados por cima
        cena_final_sobre_clipe(d, "_final_txt.mov", e["linhas"])
        run(["ffmpeg", "-y", "-stream_loop", "-1", "-ss", str(e.get("offset", 1.0)), "-i", e["src"], "-i", "_final_txt.mov",
             "-filter_complex",
             "[0:v]fps=30,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
             "zoompan=z='1.0+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1080x1920:fps=30,"
             "eq=brightness=-0.02:saturation=1.15:contrast=1.05,drawbox=x=0:y=0:w=iw:h=ih:color=0x04342C@0.25:t=fill[bg];"
             "[1:v]scale=1080:1920,format=rgba[tx];[bg][tx]overlay=0:0:format=auto,setsar=1[v]",
             "-map", "[v]", "-an", "-t", str(d), "-r", str(FPS), "-pix_fmt", "yuv420p", "-c:v", "libx264", "-crf", "20", o])
    parts.append(o)
open("_parts.txt", "w").write("".join(f"file '{p}'\n" for p in parts))
run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", "_parts.txt", "-c", "copy", "_video.mp4"])

# 4) Legendas (ASS): falas + títulos de capítulo + selo da marca nos clipes
def ts(x): return f"{int(x // 3600)}:{int(x % 3600 // 60):02d}:{x % 60:05.2f}"
head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat Thin ExtraBold,72,&H00FFFFFF,&H00FFFFFF,&H00221A04,&H96000000,0,0,0,0,100,100,0,0,1,7,2,2,70,70,250,1
Style: Brand,Montserrat Thin ExtraBold,34,&H004AB8E8,&H004AB8E8,&H00221A04,&H00000000,0,0,0,0,100,100,3,0,1,3,0,8,40,40,70,1
Style: Cap2,Anton,96,&H004AB8E8,&H004AB8E8,&H00221A04,&H00000000,0,0,0,0,100,100,1,0,1,8,3,8,40,40,150,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
GOLD, CORAL = "&H4AB8E8&", "&H5C76E8&"
kg = "|".join(map(re.escape, sorted(S.get("keywords_gold", []), key=len, reverse=True)))
kc = "|".join(map(re.escape, sorted(S.get("keywords_coral", []), key=len, reverse=True)))
B = r"(?<![A-ZÀ-Ý0-9])"; E = r"(?![A-ZÀ-Ý0-9])"
L = []
for e, a, b in cuts:
    if e["tipo"] == "clipe":
        L.append(f"Dialogue: 1,{ts(a)},{ts(b)},Brand,,0,0,0,,GRANA E FINANÇAS")
        if e.get("capitulo"): L.append(f"Dialogue: 2,{ts(a)},{ts(b)},Cap2,,0,0,0,,{{\\fad(80,0)}}{e['capitulo']}")
for s in T:
    ch = []; cur = []
    for wd in s["text"].split():
        cur.append(wd)
        if len(cur) >= 3 or (re.search(r"[,.:?!]$", wd) and len(cur) >= 2): ch.append(" ".join(cur)); cur = []
    if cur:
        if ch and len(cur) == 1: ch[-1] += " " + cur[0]
        else: ch.append(" ".join(cur))
    tot = sum(len(c) for c in ch); t0 = s["start"]; span = s["end"] - s["start"]
    for c in ch:
        d = span * len(c) / tot; x = c.upper()
        if kg: x = re.sub(f"{B}({kg}){E}", r"{\\c" + GOLD + r"}\1{\\c&HFFFFFF&}", x)
        if kc: x = re.sub(f"{B}({kc}){E}", r"{\\c" + CORAL + r"}\1{\\c&HFFFFFF&}", x)
        L.append(f"Dialogue: 0,{ts(t0)},{ts(t0 + d)},Cap,,0,0,0,,{{\\fad(50,0)\\t(0,90,\\fscx108\\fscy108)\\t(90,180,\\fscx100\\fscy100)}}{x}"); t0 += d
open("_legendas.ass", "w").write(head + "\n".join(L) + "\n")
out = S.get("output", "video.mp4")
run(["ffmpeg", "-y", "-i", "_video.mp4", "-i", "_mix.wav", "-vf", f"ass=_legendas.ass:fontsdir={FONTS}",
     "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "21", "-preset", "medium", "-pix_fmt", "yuv420p",
     "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", out])
json.dump([{"i": i, "start": round(x["start"], 2), "end": round(x["end"], 2), "text": x["text"]} for i, x in enumerate(T)],
          open("_tempos.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps({"output": out, "duration": dur(out), "size_mb": round(os.path.getsize(out) / 1e6, 1), "rate": round(rate, 2)}))
