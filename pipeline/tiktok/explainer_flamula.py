import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import Rectangle
BG="#0d1117"
# preço oscilando entre suporte (100) e resistência (112), depois rompe pra cima
y=np.array([100,104,109,114,119,124,128,122,126,121.5,124.5,122,123.8,122.8,123.3,127,131,135,139])
x=np.arange(len(y))
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Flâmula (pennant)",ha="center",va="center",fontsize=42,fontweight="bold",color="white")
fig.text(0.5,0.855,"Alta forte, pausa em triângulo\ne rompimento",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.80,"━ Linha superior",ha="center",fontsize=20,color="#f85149",fontweight="bold")
fig.text(0.5,0.772,"━ Linha inferior",ha="center",fontsize=20,color="#3fb950",fontweight="bold")
fig.text(0.5,0.744,"━ Preço",ha="center",fontsize=20,color="#58a6ff",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.43]); ax.set_facecolor(BG)
ax.set_xlim(-0.5,len(y)); ax.set_ylim(96,145); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
res,=ax.plot([6,14],[128.5,123.5],color="#f85149",lw=4,alpha=0)
sup,=ax.plot([7,14],[120.5,123],color="#3fb950",lw=4,alpha=0)
rl=ax.text(1.0,122,"MASTRO",fontsize=17,fontweight="bold",color="#58a6ff",alpha=0)
sl=ax.text(8,117.5,"FLÂMULA",fontsize=17,fontweight="bold",color="#3fb950",alpha=0)
line,=ax.plot([],[],color="#58a6ff",lw=4)
rom=ax.text(14,141,"ROMPIMENTO",fontsize=21,fontweight="bold",color="#e3b341",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Rompimento pode ser falso: espere confirmação",ha="center",fontsize=18,color="#e3b341",fontweight="bold",alpha=0)
FPS=30; PER=14; HOLD=3*FPS; DRAW=PER*(len(y)-1)
def up(f):
    if f>=0:
        for o in (res,sup,rl,sl): o.set_alpha(1)
    t=min(f/PER,len(y)-1)
    xs=np.linspace(0,t,max(2,int(t*8)))
    line.set_data(xs,np.interp(xs,x,y))
    if f>=DRAW:
        a=min(1,(f-DRAW)/FPS)
        for o in (rom,foot): o.set_alpha(a)
anim=FuncAnimation(fig,up,frames=DRAW+HOLD,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(DRAW+HOLD); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
