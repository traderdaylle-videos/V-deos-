import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
BG="#0d1117"
t=np.arange(0,61)
kp=[(0,100),(4,110),(11,90),(18,106),(25,94),(32,102),(38,96),(44,99),(50,97.5),(60,108)]
kx,ky=zip(*kp); price=np.interp(t,kx,ky)
tops=[(4,110),(18,106),(32,102),(44,99)]; bots=[(11,90),(25,94),(38,96),(50,97.5)]
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Triângulo\nSimétrico",ha="center",va="center",fontsize=42,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.835,"Topos descem, fundos sobem: compressão",ha="center",va="center",fontsize=21,color="#c9d1d9")
fig.text(0.5,0.78,"● Topos mais baixos",ha="center",fontsize=20,color="#f0883e",fontweight="bold")
fig.text(0.5,0.752,"● Fundos mais altos",ha="center",fontsize=20,color="#58a6ff",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(-2,66); ax.set_ylim(86,114); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
lp,=ax.plot([],[],color="white",lw=5)
dots=[ax.plot([x],[y],"o",ms=18,color="#f0883e",alpha=0)[0] for x,y in tops]+[ax.plot([x],[y],"o",ms=18,color="#58a6ff",alpha=0)[0] for x,y in bots]
u,=ax.plot([4,52],[110,98.5],color="#f0883e",lw=3,ls="--",alpha=0)
l,=ax.plot([11,52],[90,97.8],color="#58a6ff",lw=3,ls="--",alpha=0)
tx=ax.text(24,111,"COMPRESSÃO",fontsize=19,fontweight="bold",color="#e3b341",ha="center",alpha=0)
rt=ax.text(56,111,"ROMPE",fontsize=19,fontweight="bold",color="#3fb950",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Rompimento pode ser falso: cuidado",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; DRAW=6*FPS; POP=FPS; HOLD=2*FPS
def up(f):
    k=min(len(t),int(len(t)*f/DRAW)+1); lp.set_data(t[:k],price[:k])
    for d,(x,y) in zip(dots,tops+bots):
        if k>x: d.set_alpha(1)
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP)
        for o in (u,l,tx,rt,foot): o.set_alpha(a)
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
