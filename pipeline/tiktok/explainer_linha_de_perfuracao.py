import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt, numpy as np
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation, FFMpegWriter
BG="#0d1117"
C=[(112,113,109,110),(110,111,107,108),(108,109,105,106),(106,107,103,104),(104,105,99,100),
   (99,106,98,105.5)]
fig=plt.figure(figsize=(7.2,12.8),dpi=150); fig.patch.set_facecolor(BG)
fig.text(0.5,0.93,"Linha de\nPerfuração",ha="center",va="center",fontsize=42,fontweight="bold",color="white",linespacing=1.1)
fig.text(0.5,0.835,"Candle verde fecha acima da metade\ndo candle vermelho anterior",ha="center",va="center",fontsize=21,color="#c9d1d9",linespacing=1.3)
fig.text(0.5,0.775,"■ Candles de baixa",ha="center",fontsize=20,color="#f85149",fontweight="bold")
fig.text(0.5,0.75,"■ Candle de reação",ha="center",fontsize=20,color="#3fb950",fontweight="bold")
ax=fig.add_axes([0.05,0.285,0.9,0.44]); ax.set_facecolor(BG)
ax.set_xlim(-1,7.5); ax.set_ylim(95,114); ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
FPS=30; PER=26; HOLD=2*FPS
mid=ax.plot([3.6,6.2],[102,102],color="#e3b341",lw=3,ls="--",alpha=0)[0]
tx=ax.text(5.6,108.5,"FECHA ACIMA\nDO MEIO",fontsize=19,fontweight="bold",color="#e3b341",ha="center",alpha=0)
foot=fig.text(0.5,0.245,"Espere a confirmação",ha="center",fontsize=20,color="#e3b341",fontweight="bold",alpha=0)
def draw(i):
    o,h,l,c=C[i]; col="#3fb950" if c>=o else "#f85149"
    ax.plot([i,i],[l,h],color=col,lw=3)
    ax.add_patch(Rectangle((i-0.3,min(o,c)),0.6,max(abs(c-o),0.4),color=col))
drawn=set()
def up(f):
    for i in range(len(C)):
        if f>=i*PER and i not in drawn: draw(i); drawn.add(i)
    if f>=len(C)*PER:
        al=min(1,(f-len(C)*PER)/FPS); tx.set_alpha(al); foot.set_alpha(al); mid.set_alpha(al)
tot=len(C)*PER+FPS+HOLD
anim=FuncAnimation(fig,up,frames=tot,blit=False)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(tot); fig.savefig("explicativo_final.png",facecolor=BG); print("ok")
