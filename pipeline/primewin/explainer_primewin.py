"""Clipe explicativo Prime Win: operações sendo executadas sozinhas (abstrato, simulação ilustrativa).
Gera explicativo_anim.mp4 (8s, 1080x1920) e explicativo_final.png no diretório atual.
Uso: python3 explainer_primewin.py [titulo_linha1] [titulo_linha2]"""
import sys, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
T1=sys.argv[1] if len(sys.argv)>1 else "OPERAÇÕES"
T2=sys.argv[2] if len(sys.argv)>2 else "NO AUTOMÁTICO"
CY="#3fe0ff"; YE="#ffd23f"; PU="#8b5cf6"; BG="#0a0f2e"
rng=np.random.default_rng(11); n=120; t=np.arange(n)
price=100+0.09*t+4*np.sin(2*np.pi*(t-20)/40)+rng.normal(0,0.35,n)
buys=[10,50,90]; sells=[30,70,110]   # entradas nos fundos, saídas nos topos
fig=plt.figure(figsize=(7.2,12.8),dpi=150)
# fundo em degradê navy -> roxo
bgax=fig.add_axes([0,0,1,1]); bgax.axis("off")
g=np.linspace(0,1,256)[:,None]; bgax.imshow(g,aspect="auto",cmap=matplotlib.colors.LinearSegmentedColormap.from_list("b",[BG,"#1c0d45"]),extent=[0,1,0,1])
fig.text(0.5,0.935,T1,ha="center",va="center",fontsize=40,fontweight="bold",color="white")
fig.text(0.5,0.88,T2,ha="center",va="center",fontsize=40,fontweight="bold",color=YE)
status=fig.text(0.5,0.815,"ROBÔ EXECUTANDO A ESTRATÉGIA",ha="center",fontsize=17,color=CY,fontweight="bold")
ax=fig.add_axes([0.06,0.33,0.88,0.44]); ax.set_facecolor("none")
ax.set_xlim(-2,n+2); ax.set_ylim(price.min()-3,price.max()+4); ax.axis("off")
for y in np.linspace(price.min(),price.max(),6): ax.axhline(y,color=PU,alpha=0.18,lw=1)
line,=ax.plot([],[],color=CY,lw=4)
glow,=ax.plot([],[],color=CY,lw=12,alpha=0.15)
marks=[]
for b in buys:
    m1=ax.scatter([b],[price[b]-1.2],marker="^",s=520,color=CY,edgecolor="white",lw=2,zorder=5,alpha=0)
    l1=ax.text(b,price[b]-3.2,"COMPRA\nAUTOMÁTICA",ha="center",va="top",fontsize=11,color=CY,fontweight="bold",alpha=0)
    marks.append((b,m1,l1))
for s_ in sells:
    m2=ax.scatter([s_],[price[s_]+1.2],marker="v",s=520,color=YE,edgecolor="white",lw=2,zorder=5,alpha=0)
    l2=ax.text(s_,price[s_]+2.4,"SAÍDA\nAUTOMÁTICA",ha="center",va="bottom",fontsize=11,color=YE,fontweight="bold",alpha=0)
    marks.append((s_,m2,l2))
pnl=fig.text(0.5,0.285,"",ha="center",fontsize=30,fontweight="bold",color=YE)
fig.text(0.5,0.255,"sem clicar em comprar ou vender",ha="center",fontsize=15,color="#c9c3ff")
fig.text(0.5,0.235,"Simulação ilustrativa",ha="center",fontsize=10,color="#8f89b8")
FPS=30; FR=8*FPS; DRAW=int(6.5*FPS)
def up(f):
    k=min(n,int(n*f/DRAW)+1)
    line.set_data(t[:k],price[:k]); glow.set_data(t[:k],price[:k])
    for x,m,l in marks:
        a=1.0 if k>x else 0.0; m.set_alpha(a); l.set_alpha(a)
    done=[s_ for s_ in sells if k>s_]
    gain=sum(price[s_]-price[b] for b,s_ in zip(buys,sells) if s_ in done)
    pnl.set_text(f"{gain*25:+.0f} pontos" if done else "aguardando sinal...")
    status.set_alpha(0.55+0.45*abs(np.sin(f/6)))
    return []
anim=FuncAnimation(fig,up,frames=FR)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(FR-1); fig.savefig("explicativo_final.png")
print("ok")
