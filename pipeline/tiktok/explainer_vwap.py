import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
rng=np.random.default_rng(21)
n=90; t=np.arange(n)
kp=[(0,100),(10,106),(20,98),(30,108),(40,112),(50,104),(60,96),(70,101),(80,110),(89,107)]
kx,ky=zip(*kp); price=np.interp(t,kx,ky)+rng.normal(0,0.8,n)
vol=rng.uniform(0.5,1.5,n); vw=np.cumsum(price*vol)/np.cumsum(vol)
BG="#0d1117"
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"VWAP",ha="center",va="center",fontsize=44,fontweight="bold",color="white")
fig.text(0.5,0.845,"Preço médio do dia,\nponderado pelo volume",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.785,"━━ Preço",ha="center",fontsize=21,color="#f0883e",fontweight="bold")
fig.text(0.5,0.757,"━━ VWAP",ha="center",fontsize=21,color="#e3b341",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.45]); ax.set_facecolor(BG)
ax.set_xlim(-2,n+1); ax.set_ylim(price.min()-4,price.max()+4); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
lp,=ax.plot([],[],color="#f0883e",lw=5); lv,=ax.plot([],[],color="#e3b341",lw=5)
ta=ax.text(40,price.max()+1.5,"ACIMA: COMPRADORES",fontsize=20,fontweight="bold",color="#3fb950",ha="center",alpha=0)
tb=ax.text(60,price.min()-1.5,"ABAIXO: VENDEDORES",fontsize=20,fontweight="bold",color="#f85149",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"VWAP: referência, não garantia",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; DRAW=6*FPS; POP=FPS; HOLD=2*FPS
def up(f):
    k=min(n,int(n*f/DRAW)+1); lp.set_data(t[:k],price[:k]); lv.set_data(t[:k],vw[:k])
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP); ta.set_alpha(a); tb.set_alpha(a); foot.set_alpha(a)
    return lp,
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
