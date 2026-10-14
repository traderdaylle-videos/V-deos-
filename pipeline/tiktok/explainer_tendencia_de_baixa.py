import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
BG="#0d1117"
t=np.arange(0,61)
kp=[(0,110),(8,104),(14,108),(24,98),(30,103),(42,92),(48,97),(60,86)]
kx,ky=zip(*kp); price=np.interp(t,kx,ky)
tops=[(14,108),(30,103),(48,97)]; bots=[(24,98),(42,92),(60,86)]
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Tendência\nde Baixa",ha="center",va="center",fontsize=42,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.835,"Topos e fundos cada vez mais baixos",ha="center",va="center",fontsize=21,color="#c9d1d9")
fig.text(0.5,0.78,"● Topos mais baixos",ha="center",fontsize=20,color="#f0883e",fontweight="bold")
fig.text(0.5,0.752,"● Fundos mais baixos",ha="center",fontsize=20,color="#f85149",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(-2,66); ax.set_ylim(82,113); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
lp,=ax.plot([],[],color="white",lw=5)
dots=[ax.plot([x],[y],"o",ms=18,color="#f0883e",alpha=0)[0] for x,y in tops]+[ax.plot([x],[y],"o",ms=18,color="#f85149",alpha=0)[0] for x,y in bots]
tl,=ax.plot([14,48],[108,97],color="#f0883e",lw=3,ls="--",alpha=0)
tx=ax.text(40,109,"TOPO MAIS BAIXO",fontsize=19,fontweight="bold",color="#f0883e",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Rompeu o último topo? Cuidado",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; DRAW=6*FPS; POP=FPS; HOLD=2*FPS
def up(f):
    k=min(len(t),int(len(t)*f/DRAW)+1); lp.set_data(t[:k],price[:k])
    for d,(x,y) in zip(dots,tops+bots):
        if k>x: d.set_alpha(1)
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP); tl.set_alpha(a); tx.set_alpha(a); foot.set_alpha(a)
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
