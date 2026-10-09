import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
rng=np.random.default_rng(5)
n=80; t=np.arange(n)
kp=[(0,120),(14,100),(26,112),(40,90),(52,98),(62,88),(79,112)]   # preço: fundo em 14, fundo em 40 (mais baixo)
kx,ky=zip(*kp); price=np.interp(t,kx,ky)+rng.normal(0,0.7,n)
kr=[(0,55),(14,22),(26,50),(40,38),(52,48),(62,34),(79,66)]       # IFR ilustrativo: 2º fundo MAIS ALTO
rx,ry=zip(*kr); rsi=np.interp(t,rx,ry)+rng.normal(0,0.8,n)
i1,i2=14,40
p1,p2=price[i1],price[i2]; r1,r2=rsi[i1],rsi[i2]
BG="#0d1117"
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"DIVERGÊNCIA\nNO IFR (RSI)",ha="center",va="center",fontsize=38,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.845,"O preço faz fundo mais baixo,\nmas o IFR faz fundo mais alto",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.785,"━━ Preço",ha="center",fontsize=21,color="#f0883e",fontweight="bold")
fig.text(0.5,0.757,"━━ IFR",ha="center",fontsize=21,color="#58a6ff",fontweight="bold")
a1=fig.add_axes([0.06,0.46,0.88,0.28]); a2=fig.add_axes([0.06,0.285,0.88,0.15])
for a,yl in ((a1,(price.min()-5,price.max()+5)),(a2,(5,85))):
    a.set_facecolor(BG); a.set_xlim(-2,n+1); a.set_ylim(*yl); a.set_xticks([]); a.set_yticks([])
    for s in a.spines.values(): s.set_visible(False)
a2.axhline(30,color="#8b949e",lw=1.5,ls="--",alpha=0.6); a2.text(n,31,"30",color="#8b949e",fontsize=14,ha="right",va="bottom")
lp,=a1.plot([],[],color="#f0883e",lw=5); lr,=a2.plot([],[],color="#58a6ff",lw=5)
d1=a1.scatter([i1,i2],[p1,p2],s=900,color="#f85149",edgecolor="white",lw=4,zorder=5); d1.set_alpha(0)
d2=a2.scatter([i1,i2],[r1,r2],s=900,color="#3fb950",edgecolor="white",lw=4,zorder=5); d2.set_alpha(0)
l1,=a1.plot([i1,i2],[p1,p2],color="#f85149",lw=4,ls="--",alpha=0)
l2,=a2.plot([i1,i2],[r1,r2],color="#3fb950",lw=4,ls="--",alpha=0)
t1=a1.text(24,p2-3,"FUNDO MAIS\nBAIXO",fontsize=22,fontweight="bold",color="#f85149",ha="center",va="center",alpha=0)
t2=a2.text(24,70,"FUNDO MAIS\nALTO",fontsize=22,fontweight="bold",color="#3fb950",ha="center",va="center",alpha=0)
foot=fig.text(0.5,0.245,"Pode indicar perda de força da queda",ha="center",fontsize=20,color="#3fb950",fontweight="bold",alpha=0)
FPS=30; DRAW=int(5*FPS); POP=int(1*FPS); HOLD=int(2*FPS)
def up(f):
    k=min(n,int(n*f/DRAW)+1)
    lp.set_data(t[:k],price[:k]); lr.set_data(t[:k],rsi[:k])
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP)
        for o in (d1,d2): o.set_alpha(a)
        for o in (t1,t2,foot): o.set_alpha(a)
        l1.set_alpha(a); l2.set_alpha(a)
    return lp,lr
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD)
fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
