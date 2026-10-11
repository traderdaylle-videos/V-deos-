import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
rng=np.random.default_rng(7)
n=80; t=np.arange(n)
kp=[(0,108),(6,111),(12,104),(20,107),(26,100),(34,103),(40,95),(48,98),(54,91),(62,93),(66,86),(72,92),(79,99)]
kx,ky=zip(*kp); price=np.interp(t,kx,ky)+rng.normal(0,0.25,n)
tops=[(6,111),(20,107),(34,103),(48,98),(62,93)]
sl=(93-111)/(62-6); line=lambda x:111+sl*(x-6)
BG="#0d1117"
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"LINHA DE\nTENDÊNCIA DE BAIXA",ha="center",va="center",fontsize=34,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.845,"Liga os topos cada vez\nmais baixos do preço",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.785,"━━ Preço",ha="center",fontsize=21,color="#f0883e",fontweight="bold")
fig.text(0.5,0.757,"╌╌ LTB",ha="center",fontsize=21,color="#f85149",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.45]); ax.set_facecolor(BG)
ax.set_xlim(-2,n+6); ax.set_ylim(82,116); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
lp,=ax.plot([],[],color="#f0883e",lw=5)
xs=np.array([4,76]); ll,=ax.plot(xs,line(xs),color="#f85149",lw=4,ls="--",alpha=0)
dots=[ax.plot(x,y,"o",color="#f85149",ms=16,alpha=0)[0] for x,y in tops]
lab=ax.text(34,113,"TOPOS CADA VEZ MAIS BAIXOS",fontsize=19,fontweight="bold",color="white",ha="center",alpha=0)
rom=ax.text(70,103.5,"ROMPIMENTO",fontsize=22,fontweight="bold",color="#3fb950",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Referência de análise, não garantia",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; DRAW=5*FPS; POP=FPS; HOLD=2*FPS
def up(f):
    k=min(n,int(n*f/DRAW)+1); lp.set_data(t[:k],price[:k])
    for d,(x,y) in zip(dots,tops): d.set_alpha(1 if k>x else 0)
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP); ll.set_alpha(a); lab.set_alpha(a); rom.set_alpha(a); foot.set_alpha(a)
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
