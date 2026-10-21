import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
BG="#0d1117"
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Canal\nde Baixa",ha="center",va="center",fontsize=42,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.835,"Duas linhas paralelas inclinadas\npara baixo contêm o preço",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.775,"■ Linha de topos (cima)",ha="center",fontsize=20,color="#f85149",fontweight="bold")
fig.text(0.5,0.75,"■ Linha de fundos (baixo)",ha="center",fontsize=20,color="#3fb950",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(0,10); ax.set_ylim(0,20); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
X=np.array([0.5,1.8,3.1,4.4,5.7,7.0,8.3,9.5]); Y=np.array([17,13.2,15.2,10.8,12.8,8.4,10.4,6.2])
top=lambda x:17.5-1.15*(x-0.5)+ (0); bot=lambda x:13.0-1.15*(x-0.5)-0.0
# topos nos pontos pares (0,2,4,6), fundos nos ímpares
tx=[X[i] for i in (0,2,4,6)]; ty=[Y[i] for i in (0,2,4,6)]
bx=[X[i] for i in (1,3,5,7)]; by=[Y[i] for i in (1,3,5,7)]
pt=np.polyfit(tx,ty,1); pb=np.polyfit(bx,by,1); sl=(pt[0]+pb[0])/2
pt=[sl,np.mean(np.array(ty)-sl*np.array(tx))]; pb=[sl,np.mean(np.array(by)-sl*np.array(bx))]
xs=np.array([0.2,9.8])
l1=ax.plot(xs,np.polyval(pt,xs),color="#f85149",lw=3.5,ls="--",alpha=0)[0]
l2=ax.plot(xs,np.polyval(pb,xs),color="#3fb950",lw=3.5,ls="--",alpha=0)[0]
price=ax.plot([],[],color="white",lw=3.5)[0]
tt=ax.text(5,19,"TOPOS MAIS BAIXOS",fontsize=19,fontweight="bold",color="#f85149",ha="center",alpha=0)
tb=ax.text(5,0.6,"FUNDOS MAIS BAIXOS",fontsize=19,fontweight="bold",color="#3fb950",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Atenção ao rompimento",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; PER=24; HOLD=2*FPS
def up(f):
    seg=f/PER; k=int(min(seg,len(X)-1)); fr=min(seg-k,1) if seg<len(X)-1 else 0
    xs_=list(X[:k+1]); ys_=list(Y[:k+1])
    if k<len(X)-1: xs_.append(X[k]+(X[k+1]-X[k])*fr); ys_.append(Y[k]+(Y[k+1]-Y[k])*fr)
    price.set_data(xs_,ys_)
    if f>=(len(X)-1)*PER:
        al=min(1,(f-(len(X)-1)*PER)/FPS)
        for a in (l1,l2,tt,tb,foot): a.set_alpha(al)
tot=(len(X)-1)*PER+FPS+HOLD
anim=FuncAnimation(fig,up,frames=tot,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(tot); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
