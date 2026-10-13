import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
BG="#0d1117"
x=np.arange(0,40)
y=np.concatenate([np.linspace(120,100,12),
    100+ np.linspace(0,6,16)+1.2*np.sin(np.linspace(0,6*np.pi,16)),
    np.linspace(106,86,12)])
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Bandeira\nde Baixa",ha="center",va="center",fontsize=42,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.835,"Queda forte (mastro), pausa inclinada\npra cima (bandeira) e rompimento",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.775,"■ Mastro e rompimento",ha="center",fontsize=20,color="#f85149",fontweight="bold")
fig.text(0.5,0.75,"■ Bandeira (pausa)",ha="center",fontsize=20,color="#e3b341",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(0,40); ax.set_ylim(82,124); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
FPS=30; N=len(x); PER=4; HOLD=2*FPS
l1,=ax.plot([],[],color="#f85149",lw=4); l2,=ax.plot([],[],color="#e3b341",lw=4); l3,=ax.plot([],[],color="#f85149",lw=4)
tx=ax.text(20,119,"BANDEIRA DE BAIXA",fontsize=20,fontweight="bold",color="#e3b341",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Rompe o fundo da bandeira",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
def up(f):
    k=min(N,f//PER+1)
    l1.set_data(x[:min(k,13)],y[:min(k,13)])
    if k>12: l2.set_data(x[12:min(k,28)],y[12:min(k,28)])
    if k>27: l3.set_data(x[27:k],y[27:k])
    if f>=N*PER:
        al=min(1,(f-N*PER)/FPS); tx.set_alpha(al); foot.set_alpha(al)
tot=N*PER+FPS+HOLD
anim=FuncAnimation(fig,up,frames=tot,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(tot); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
