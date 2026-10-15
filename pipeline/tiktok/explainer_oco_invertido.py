import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
BG="#0d1117"
t=np.arange(0,61)
kp=[(0,106),(10,96),(16,102),(28,88),(40,102),(48,96),(60,110)]
kx,ky=zip(*kp); price=np.interp(t,kx,ky)
lows=[(10,96),(28,88),(48,96)]; names=["OMBRO","CABEÇA","OMBRO"]
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Ombro-Cabeça-Ombro\nInvertido",ha="center",va="center",fontsize=38,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.835,"Três fundos: o do meio é o mais baixo",ha="center",va="center",fontsize=21,color="#c9d1d9")
fig.text(0.5,0.78,"● Fundos (ombros e cabeça)",ha="center",fontsize=20,color="#58a6ff",fontweight="bold")
fig.text(0.5,0.752,"-- Linha de pescoço",ha="center",fontsize=20,color="#e3b341",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(-2,66); ax.set_ylim(82,114); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
lp,=ax.plot([],[],color="white",lw=5)
dots=[ax.plot([x],[y],"o",ms=18,color="#58a6ff",alpha=0)[0] for x,y in lows]
labs=[ax.text(x,y-3.2,n,fontsize=18,fontweight="bold",color="#58a6ff",ha="center",alpha=0) for (x,y),n in zip(lows,names)]
nl,=ax.plot([14,56],[102,102],color="#e3b341",lw=3,ls="--",alpha=0)
nt=ax.text(30,104.2,"LINHA DE PESCOÇO",fontsize=19,fontweight="bold",color="#e3b341",ha="center",alpha=0)
rt=ax.text(46,108,"ROMPE",fontsize=19,fontweight="bold",color="#3fb950",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Rompeu com volume? Fique atento",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; DRAW=6*FPS; POP=FPS; HOLD=2*FPS
def up(f):
    k=min(len(t),int(len(t)*f/DRAW)+1); lp.set_data(t[:k],price[:k])
    for d,l,(x,y) in zip(dots,labs,lows):
        if k>x: d.set_alpha(1); l.set_alpha(1)
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP); nl.set_alpha(a); nt.set_alpha(a); rt.set_alpha(a); foot.set_alpha(a)
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
