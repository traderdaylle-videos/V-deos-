import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
rng=np.random.default_rng(5)
BG="#0d1117"
n=80; t=np.arange(n)
# queda em zigue-zague que se estreita, rompimento para cima no fim
top=lambda x:120-0.40*x; bot=lambda x:100-0.18*x
kx=[0,8,16,24,32,40,48,56,62]
ky=[top(0),bot(8),top(16),bot(24),top(32),bot(40),top(48),bot(56),top(62)]
price=np.interp(t,kx,ky)+rng.normal(0,0.5,n)
price[62:]=np.interp(t[62:],[62,79],[ky[-1]-0.5,ky[-1]+17])+rng.normal(0,0.5,n-62)
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"CUNHA\nDESCENDENTE",ha="center",va="center",fontsize=40,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.845,"Queda que perde força:\nas linhas se fecham",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.785,"━━ Preço",ha="center",fontsize=21,color="#f0883e",fontweight="bold")
fig.text(0.5,0.757,"━━ Linhas da cunha",ha="center",fontsize=21,color="#e3b341",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.45]); ax.set_facecolor(BG)
ax.set_xlim(-2,n+2); ax.set_ylim(price.min()-4,price.max()+4); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
xs=np.array([0,66]); l1,=ax.plot([],[],color="#e3b341",lw=4); l2,=ax.plot([],[],color="#e3b341",lw=4)
lp,=ax.plot([],[],color="#f0883e",lw=5)
dot=ax.scatter([64],[ky[-1]],s=1100,color="#3fb950",edgecolor="white",lw=4,zorder=5); dot.set_alpha(0)
lab=ax.text(52,ky[-1]+13,"ROMPIMENTO\nPRA CIMA",fontsize=24,fontweight="bold",color="white",ha="center",va="center",alpha=0)
foot=fig.text(0.5,0.245,"Possível reversão, com confirmação",ha="center",fontsize=20,color="#3fb950",fontweight="bold",alpha=0)
FPS=30; DRAW=6*FPS; POP=FPS; HOLD=2*FPS
def up(f):
    k=min(n,int(n*f/DRAW)+1); lp.set_data(t[:k],price[:k])
    a=min(1,f/(2*FPS)); xe=xs[0]+(xs[1]-xs[0])*a
    l1.set_data([0,xe],[top(0),top(xe)]); l2.set_data([0,xe],[bot(0),bot(xe)])
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP); dot.set_alpha(a); lab.set_alpha(a); foot.set_alpha(a)
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+POP+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
