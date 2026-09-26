import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
np.random.seed(3)
n=90; t=np.arange(n)
trend=np.concatenate([np.linspace(120,100,40),np.linspace(100,130,50)])
price=trend+np.random.normal(0,0.8,n)
def sma(s,w):
    o=np.full(len(s),np.nan)
    for i in range(w-1,len(s)): o[i]=s[i-w+1:i+1].mean()
    return o
fast,slow=sma(price,7),sma(price,20)
d=fast-slow
ci=[i+1 for i in range(n-1) if not np.isnan(d[i]) and d[i]<=0 and d[i+1]>0][-1]
fig=plt.figure(figsize=(7.2,12.8),dpi=150)  # 1080x1920
fig.patch.set_facecolor("#0d1117")
fig.text(0.5,0.93,"CRUZAMENTO DE\nMÉDIAS MÓVEIS",ha="center",va="center",fontsize=38,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.845,"A média rápida cruza a lenta\nde baixo pra cima",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.785,"━━ Média rápida (7)",ha="center",fontsize=21,color="#3fb950",fontweight="bold")
fig.text(0.5,0.755,"━━ Média lenta (20)",ha="center",fontsize=21,color="#f0883e",fontweight="bold")
ax=fig.add_axes([0.05,0.27,0.9,0.47]); ax.set_facecolor("#0d1117")
ax.set_xlim(-2,n+1); ax.set_ylim(np.nanmin(price)-3,np.nanmax(price)+3)
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
lp,=ax.plot([],[],color="#8b949e",lw=1.3,alpha=0.5)
lf,=ax.plot([],[],color="#3fb950",lw=5)
ls,=ax.plot([],[],color="#f0883e",lw=5)
dot=ax.scatter([ci],[fast[ci]],s=1100,color="#3fb950",edgecolor="white",lw=4,zorder=5); dot.set_alpha(0)
lab=ax.text(ci+24,fast[ci]+1,"CRUZAMENTO\nDE ALTA",fontsize=25,fontweight="bold",color="white",ha="center",va="center",alpha=0)
foot=fig.text(0.5,0.235,"Sinal de possível força compradora",ha="center",fontsize=20,color="#3fb950",fontweight="bold",alpha=0)
FPS=30; DRAW=int(5*FPS); POP=int(1*FPS); HOLD=int(2*FPS)
def up(f):
    k=min(n,int(n*f/DRAW)+1)
    lp.set_data(t[:k],price[:k]); lf.set_data(t[:k],fast[:k]); ls.set_data(t[:k],slow[:k])
    if f>=DRAW:
        a=min(1,(f-DRAW)/POP); dot.set_alpha(a); lab.set_alpha(a); foot.set_alpha(a)
        pulse=1100*(1+0.25*np.sin((f-DRAW)/4)) if f<DRAW+POP*2 else 1100
        dot.set_sizes([pulse])
    return lp,lf,ls,dot,lab,foot
anim=FuncAnimation(fig,up,frames=DRAW+POP+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
fig.savefig("explicativo_final.png",facecolor=fig.get_facecolor())
print("ok")
