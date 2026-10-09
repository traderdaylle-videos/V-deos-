import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
rng=np.random.default_rng(8)
n=90; t=np.arange(n)
kp=[(0,112),(10,100),(18,110),(28,100),(36,108),(46,88),(58,100),(66,86),(74,93),(89,80)]
kx,ky=zip(*kp); price=np.interp(t,kx,ky)+rng.normal(0,0.7,n)
LV=100; BG="#0d1117"
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"SUPORTE QUE VIRA\nRESISTÊNCIA",ha="center",va="center",fontsize=36,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.845,"Quando o preço perde o suporte,\no nível costuma virar teto",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.785,"━━ Preço",ha="center",fontsize=21,color="#f0883e",fontweight="bold")
fig.text(0.5,0.757,"━━ Nível de preço",ha="center",fontsize=21,color="#58a6ff",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.45]); ax.set_facecolor(BG)
ax.set_xlim(-2,n+1); ax.set_ylim(price.min()-4,price.max()+4); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.axhline(LV,color="#58a6ff",lw=4,ls="--",alpha=0.9)
lp,=ax.plot([],[],color="#f0883e",lw=5)
tsup=ax.text(14,LV-6,"SUPORTE",fontsize=24,fontweight="bold",color="#3fb950",ha="center",va="center",alpha=0)
dot=ax.scatter([58],[price[58]],s=1100,color="#f85149",edgecolor="white",lw=4,zorder=5); dot.set_alpha(0)
lab=ax.text(70,LV+9,"AGORA É\nRESISTÊNCIA",fontsize=24,fontweight="bold",color="#f85149",ha="center",va="center",alpha=0)
foot=fig.text(0.5,0.245,"Reteste por baixo costuma ser observado",ha="center",fontsize=20,color="#f85149",fontweight="bold",alpha=0)
FPS=30; DRAW=int(6*FPS); POP=int(1*FPS); HOLD=int(2*FPS)
def up(f):
    k=min(n,int(n*f/DRAW)+1); lp.set_data(t[:k],price[:k])
    if k>20: tsup.set_alpha(min(1,(k-20)/6))
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP); dot.set_alpha(a); lab.set_alpha(a); foot.set_alpha(a)
    return lp,
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD)
fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
