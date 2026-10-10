import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import Rectangle
BG="#0d1117"; G="#3fb950"; R="#f85149"
# (open, close, high, low) — candles comuns com sombras e um marubozu de alta no fim
C=[(100,103,106,98),(103,101,105,99),(101,104,107,100),(104,102,106,100),(102,105,108,101),(105,103,107,101),(103,104,106,101),(104,102,105,100)]
C.append((102,114,114,102))  # marubozu: sem sombras
n=len(C)
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"CANDLE\nMARUBOZU",ha="center",va="center",fontsize=40,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.845,"Corpo cheio, sem sombras:\num lado dominou o pregão",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.785,"■ Candle de alta",ha="center",fontsize=21,color=G,fontweight="bold")
fig.text(0.5,0.757,"■ Candle de baixa",ha="center",fontsize=21,color=R,fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.45]); ax.set_facecolor(BG)
ax.set_xlim(-1,n+3.5); ax.set_ylim(94,118); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
parts=[]
for i,(o,c,h,l) in enumerate(C):
    col=G if c>=o else R
    w,=ax.plot([i,i],[l,h],color=col,lw=4,alpha=0)
    b=Rectangle((i-0.32,min(o,c)),0.64,abs(c-o),color=col,alpha=0); ax.add_patch(b); parts.append((w,b))
lab=ax.text(n-1-0.2,116.5,"SEM SOMBRAS",fontsize=24,fontweight="bold",color="white",ha="right",alpha=0)
ar=ax.annotate("",xy=(n-1,114.2),xytext=(n-2.2,116),arrowprops=dict(color="white",lw=3),alpha=0)
foot=fig.text(0.5,0.245,"Força de um lado, não garantia",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; PER=18; DRAW=PER*n; POP=FPS; HOLD=2*FPS
def up(f):
    for i,(w,b) in enumerate(parts):
        a=1 if f>=i*PER+4 else 0; w.set_alpha(a); b.set_alpha(a)
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP); lab.set_alpha(a); ar.set_alpha(a); foot.set_alpha(a)
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
