import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import Rectangle
BG="#0d1117"
# preço oscilando entre suporte (100) e resistência (112), depois rompe pra cima
y=np.array([104,108,111.5,107,102,100.5,105,109,112,108,103,100.2,104,109,111.8,115,119,123,126])
x=np.arange(len(y))
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Retângulo",ha="center",va="center",fontsize=42,fontweight="bold",color="white")
fig.text(0.5,0.855,"Preço lateral entre suporte\ne resistência, até romper",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.80,"━ Resistência",ha="center",fontsize=20,color="#f85149",fontweight="bold")
fig.text(0.5,0.772,"━ Suporte",ha="center",fontsize=20,color="#3fb950",fontweight="bold")
fig.text(0.5,0.744,"━ Preço",ha="center",fontsize=20,color="#58a6ff",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.43]); ax.set_facecolor(BG)
ax.set_xlim(-0.5,len(y)); ax.set_ylim(95,130); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
res,=ax.plot([0,14.5],[112,112],color="#f85149",lw=4,alpha=0)
sup,=ax.plot([0,14.5],[100,100],color="#3fb950",lw=4,alpha=0)
rl=ax.text(0.2,113.5,"RESISTÊNCIA",fontsize=17,fontweight="bold",color="#f85149",alpha=0)
sl=ax.text(0.2,96.5,"SUPORTE",fontsize=17,fontweight="bold",color="#3fb950",alpha=0)
line,=ax.plot([],[],color="#58a6ff",lw=4)
rom=ax.text(13,126.5,"ROMPIMENTO",fontsize=21,fontweight="bold",color="#e3b341",ha="center",alpha=0)
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
