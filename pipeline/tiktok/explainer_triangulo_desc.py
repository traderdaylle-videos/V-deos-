import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
rng=np.random.default_rng(5)
n=80; t=np.arange(n)
kp=[(0,112),(8,100),(16,109),(24,100),(32,106),(40,100),(48,103),(54,100),(60,101),(66,100),(72,93),(79,88)]
kx,ky=zip(*kp); price=np.interp(t,kx,ky)+rng.normal(0,0.25,n)
BG="#0d1117"
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Triângulo\nDescendente",ha="center",va="center",fontsize=42,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.835,"Suporte reto embaixo e\ntopos cada vez mais baixos",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.775,"━━ Suporte (piso)",ha="center",fontsize=20,color="#58a6ff",fontweight="bold")
fig.text(0.5,0.75,"━━ Topos descendentes",ha="center",fontsize=20,color="#f85149",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(-2,n+1); ax.set_ylim(84,116); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.plot([0,66],[100,100],color="#58a6ff",lw=5,ls="--")
ax.plot([0,66],[112,100.5],color="#f85149",lw=5,ls="--")
lp,=ax.plot([],[],color="white",lw=3.5)
ax.text(33,97,"SUPORTE",fontsize=19,fontweight="bold",color="#58a6ff",ha="center")
tx=ax.text(66,91,"ROMPIMENTO",fontsize=22,fontweight="bold",color="#f85149",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Rompimento não é garantia",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; DRAW=6*FPS; POP=FPS; HOLD=2*FPS
def up(f):
    k=min(n,int(n*f/DRAW)+1); lp.set_data(t[:k],price[:k])
    if f>=DRAW:
        al=min(1,(f-DRAW)/POP); tx.set_alpha(al); foot.set_alpha(al)
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
