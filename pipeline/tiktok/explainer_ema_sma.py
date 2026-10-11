import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
rng=np.random.default_rng(11)
n=90; t=np.arange(n)
kp=[(0,100),(25,101),(40,100),(50,112),(70,114),(89,113)]
kx,ky=zip(*kp); price=np.interp(t,kx,ky)+rng.normal(0,0.3,n)
N=15
sma=np.array([price[max(0,i-N+1):i+1].mean() for i in range(n)])
a=2/(N+1); ema=np.zeros(n); ema[0]=price[0]
for i in range(1,n): ema[i]=a*price[i]+(1-a)*ema[i-1]
BG="#0d1117"
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"EMA x SMA",ha="center",va="center",fontsize=44,fontweight="bold",color="white")
fig.text(0.5,0.845,"Duas médias móveis:\numa reage mais rápido",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.797,"━━ Preço",ha="center",fontsize=20,color="#8b949e",fontweight="bold")
fig.text(0.5,0.772,"━━ EMA (exponencial)",ha="center",fontsize=20,color="#3fb950",fontweight="bold")
fig.text(0.5,0.747,"━━ SMA (simples)",ha="center",fontsize=20,color="#58a6ff",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(-2,n+1); ax.set_ylim(97,117); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
lp,=ax.plot([],[],color="#8b949e",lw=3); le,=ax.plot([],[],color="#3fb950",lw=5); ls,=ax.plot([],[],color="#58a6ff",lw=5)
tx=ax.text(27,107,"A EMA REAGE PRIMEIRO",fontsize=21,fontweight="bold",color="#3fb950",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Mais rápida não é mais certa",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; DRAW=6*FPS; POP=FPS; HOLD=2*FPS
def up(f):
    k=min(n,int(n*f/DRAW)+1)
    lp.set_data(t[:k],price[:k]); le.set_data(t[:k],ema[:k]); ls.set_data(t[:k],sma[:k])
    if f>=DRAW:
        al=min(1,(f-DRAW)/POP); tx.set_alpha(al); foot.set_alpha(al)
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
