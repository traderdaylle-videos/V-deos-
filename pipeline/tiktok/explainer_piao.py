import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import Rectangle
BG="#0d1117"
# (abertura, fechamento, max, min)
C=[(100,106,107,99),(106,112,113,105),(112,117,118,111),   # alta
   (117,118,124,111),                                      # pião: corpo pequeno, sombras longas
   (117,111,112,109),(111,106,107,104),(106,102,103,100)]
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Candle\nPião",ha="center",va="center",fontsize=42,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.835,"Corpo pequeno e sombras\nnos dois lados = indecisão",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.78,"● Candle de alta",ha="center",fontsize=20,color="#3fb950",fontweight="bold")
fig.text(0.5,0.752,"● Candle de baixa",ha="center",fontsize=20,color="#f85149",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(-0.8,len(C)+0.2); ax.set_ylim(94,130); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
art=[]
for i,(o,cl,h,l) in enumerate(C):
    col="#3fb950" if cl>=o else "#f85149"
    ln,=ax.plot([i,i],[l,h],color=col,lw=3,alpha=0)
    r=Rectangle((i-0.3,min(o,cl)),0.6,max(abs(cl-o),0.6),color=col,alpha=0); ax.add_patch(r); art.append((ln,r))
box=Rectangle((2.55,108),0.9,19,fill=False,ec="#e3b341",lw=4,ls="--",alpha=0); ax.add_patch(box)
lab=ax.text(3,128.5,"PIÃO: INDECISÃO",fontsize=21,fontweight="bold",color="#e3b341",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Sozinho não confirma nada: espere o próximo candle",ha="center",fontsize=17,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; PER=24; HOLD=3*FPS; DRAW=PER*len(C)
def up(f):
    for i,(ln,r) in enumerate(art):
        if f>=i*PER: ln.set_alpha(1); r.set_alpha(1)
    if f>=DRAW:
        a=min(1,(f-DRAW)/FPS)
        for o in (box,lab,foot): o.set_alpha(a)
anim=FuncAnimation(fig,up,frames=DRAW+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
