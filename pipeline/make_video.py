#!/usr/bin/env python3
"""Monta o vídeo TikTok completo a partir de um spec.json (custo zero).

Uso: python3 make_video.py WORKDIR
WORKDIR/spec.json:
{
  "segs": [["intro","frase"], ...],   # seções: intro, meio, recap, final_5pi, final_fim
  "photos_meio": ["a.png","b.png","c.png"],  # fotos (1080x1920 ou 9:16) para o bloco "meio", em ordem
  "photo_5pi": "dinheiro.png",                 # foto durante o anúncio da 5PI
  "explainer_anim": "explicativo_anim.mp4",    # animação 1080x1920 (~8s) do conceito
  "explainer_final": "explicativo_final.png",  # último quadro da animação (1080x1920)
  "keywords_green": ["COMPRA","ALTA"], "keywords_orange": ["VENDA","BAIXA"],
  "output": "video.mp4"
}
Caminhos relativos são relativos ao WORKDIR. Requer ./setup.sh antes.
"""
import json, os, re, subprocess as sp, sys, wave
import numpy as np
W=sys.argv[1]; os.chdir(W); S=json.load(open("spec.json"))
PIPER="/tmp/piper"; FPS=30
HERE=os.path.dirname(os.path.abspath(__file__))
def run(a): sp.run(a,check=True,capture_output=True)
def dur(f): return float(sp.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f]))

# 1) Narração frase a frase (tempos exatos). Fala acelerada e duração ajustada para "1 min e pouco" (61-72s).
TARGET=(61.0,72.0); GAP=0.2
def synth(scale):
    T=[]; t=0.0; files=[]
    for i,(sec,txt) in enumerate(S["segs"]):
        f=f"_seg{i:02d}.wav"
        sp.run([f"{PIPER}/piper/piper","--model",f"{PIPER}/pt-br-edresson-low.onnx","--length_scale",f"{scale:.3f}","--output_file",f],input=txt.encode(),check=True,capture_output=True)
        d=dur(f); T.append({"sec":sec,"text":txt,"start":t,"end":t+d}); files.append(f); t+=d+GAP
    return T,files
scale=float(S.get("length_scale",0.85))
T,files=synth(scale)
for _ in range(3):
    total=T[-1]["end"]+0.8
    if TARGET[0]<=total<=TARGET[1]: break
    scale=max(0.72,min(1.1,scale*(66.0/total)))
    T,files=synth(scale)
total=T[-1]["end"]+0.8
if not (TARGET[0]<=total<=TARGET[1]):
    sys.exit(f"ERRO: narração com {total:.1f}s mesmo com velocidade {scale:.2f}. Ajuste o tamanho do roteiro (~150-175 palavras) e rode de novo.")
print(f"velocidade length_scale={scale:.2f} duração={total:.1f}s", file=sys.stderr)
run(["ffmpeg","-y","-f","lavfi","-i","anullsrc=r=16000:cl=mono","-t",str(GAP),"_gap.wav"])
with open("_list.txt","w") as L:
    for j,f in enumerate(files):
        L.write(f"file '{f}'\n")
        if j<len(files)-1: L.write("file '_gap.wav'\n")
run(["ffmpeg","-y","-f","concat","-safe","0","-i","_list.txt","-ar","44100","-ac","1","_narracao.wav"])
END=T[-1]["end"]+0.8

# 2) Trilha ambiente gerada (sem direitos autorais), bem baixa
sr=44100; tt=np.arange(int(sr*END))/sr; out=np.zeros_like(tt)
chords=[[220,261.63,329.63],[174.61,220,261.63],[130.81,196,261.63],[196,246.94,293.66]]
for k in range(int(END//8)+1):
    c=chords[k%4]; a=k*8; m=(tt>=a)&(tt<a+10); x=tt[m]-a
    env=np.clip(x/2,0,1)*np.clip((10-x)/2,0,1)
    for fr in c: out[m]+=env*(np.sin(2*np.pi*fr*x)+0.3*np.sin(4*np.pi*fr*x))*0.2
out=out/np.abs(out).max()*0.09
w=wave.open("_musica.wav","wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
run(["ffmpeg","-y","-i","_narracao.wav","-i","_musica.wav","-filter_complex","[0:a]aresample=44100,apad[v];[v][1:a]amix=inputs=2:duration=shortest:normalize=0,alimiter=limit=0.95[a]","-map","[a]","-ac","1","_mix.wav"])

# 3) Cortes visuais por seção
def first(sec): return min(x["start"] for x in T if x["sec"]==sec)
def last_end(sec): return max(x["end"] for x in T if x["sec"]==sec)
cuts=[("anim",0,first("meio"))]
meio=[x for x in T if x["sec"]=="meio"]; ph=S["photos_meio"]
# distribui as frases do meio entre as fotos (grupos contíguos)
groups=[[] for _ in ph]
for i,x in enumerate(meio): groups[min(len(ph)-1,i*len(ph)//len(meio))].append(x)
for p,g in zip(ph,groups):
    if g: cuts.append((p,g[0]["start"],None))
cuts.append(("anim",first("recap"),None)); cuts.append((S["photo_5pi"],first("final_5pi"),None)); cuts.append(("endcard",first("final_fim"),None))
cuts=[(s,a,(cuts[i+1][1] if i+1<len(cuts) else END)) for i,(s,a,_) in enumerate(cuts)]

# cartão final
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor("#0d1117")
fig.text(0.5,0.86,"GOSTOU?",ha="center",fontsize=46,fontweight="bold",color="white")
fig.text(0.5,0.79,"Segue pra mais dicas\nde análise técnica",ha="center",va="top",fontsize=26,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.62,S.get("handle","@traderdaylle"),ha="center",fontsize=40,fontweight="bold",color="#3fb950")
fig.text(0.5,0.52,"Link da 5PI na descrição",ha="center",fontsize=24,color="#f0883e",fontweight="bold")
fig.text(0.5,0.075,"Conteúdo educacional. Não é recomendação de investimento.",ha="center",fontsize=13,color="#8b949e")
fig.savefig("_endcard.png",facecolor=fig.get_facecolor()); plt.close(fig)

parts=[]
for k,(src,a,b) in enumerate(cuts):
    d=round(b-a,3); o=f"_part{k}.mp4"; n=int(round(d*FPS))
    if src=="anim":
        ad=dur(S["explainer_anim"]); hold=max(0.1,d-ad)
        run(["ffmpeg","-y","-i",S["explainer_anim"],"-loop","1","-t",str(hold+0.2),"-i",S["explainer_final"],"-filter_complex",
             f"[1:v]scale=1080:1920,zoompan=z='min(1+0.0002*on,1.05)':x='iw/2-(iw/zoom/2)':y='ih*0.55-(ih/zoom*0.55)':d={int(hold*FPS)+3}:s=1080x1920:fps={FPS}[h];[0:v]scale=1080:1920,fps={FPS}[a];[a][h]concat=n=2:v=1[v]",
             "-map","[v]","-t",str(d),"-r",str(FPS),"-pix_fmt","yuv420p","-c:v","libx264","-crf","20",o])
    elif src=="endcard":
        run(["ffmpeg","-y","-loop","1","-i","_endcard.png","-vf",f"scale=1080:1920,zoompan=z='min(1+0.0004*on,1.08)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS}","-t",str(d),"-pix_fmt","yuv420p","-c:v","libx264","-crf","20",o])
    else:
        run(["ffmpeg","-y","-loop","1","-i",src,"-vf",f"scale=2160:3840:force_original_aspect_ratio=increase:flags=lanczos,crop=2160:3840,unsharp=5:5:0.8,zoompan=z='1.0+0.0012*on':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps={FPS},eq=brightness=-0.04","-t",str(d),"-pix_fmt","yuv420p","-c:v","libx264","-crf","20",o])
    parts.append(o)
open("_parts.txt","w").write("".join(f"file '{p}'\n" for p in parts))
run(["ffmpeg","-y","-f","concat","-safe","0","-i","_parts.txt","-c","copy","_video.mp4"])

# 4) Legendas sincronizadas (ASS), palavras-chave coloridas
def ts(x): return f"{int(x//3600)}:{int(x%3600//60):02d}:{x%60:05.2f}"
head="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,DejaVu Sans,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,1,7,3,2,70,70,260,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
G="|".join(map(re.escape,S.get("keywords_green",["COMPRA","ALTA","5PI"]))); O="|".join(map(re.escape,S.get("keywords_orange",["VENDA","BAIXA"])))
L=[]
for s in T:
    ch=[]; cur=[]
    for wd in s["text"].split():
        cur.append(wd)
        if len(cur)>=4 or (re.search(r"[,.:?!]$",wd) and len(cur)>=2): ch.append(" ".join(cur)); cur=[]
    if cur:
        if ch and len(cur)==1: ch[-1]+=" "+cur[0]
        else: ch.append(" ".join(cur))
    tot=sum(len(c) for c in ch); t0=s["start"]; span=s["end"]-s["start"]
    for c in ch:
        d=span*len(c)/tot; x=c.upper()
        if G: x=re.sub(f"({G})",r"{\\c&H50B93F&}\1{\\c&HFFFFFF&}",x)
        if O: x=re.sub(f"({O})",r"{\\c&H3E88F0&}\1{\\c&HFFFFFF&}",x)
        L.append(f"Dialogue: 0,{ts(t0)},{ts(t0+d)},Cap,,0,0,0,,{x}"); t0+=d
open("_legendas.ass","w").write(head+"\n".join(L)+"\n")
out=S.get("output","video.mp4")
run(["ffmpeg","-y","-i","_video.mp4","-i","_mix.wav","-vf","ass=_legendas.ass","-map","0:v","-map","1:a","-c:v","libx264","-crf","23","-preset","medium","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-shortest","-movflags","+faststart",out])
print(json.dumps({"output":out,"duration":dur(out),"size_mb":round(os.path.getsize(out)/1e6,1)}))
