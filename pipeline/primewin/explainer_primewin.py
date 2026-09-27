"""Clipe explicativo Prime Win: operações sendo executadas sozinhas (abstrato, simulação ilustrativa).
Gera explicativo_anim.mp4 (1080x1920, padrão 13s) e explicativo_final.png no diretório atual.

Uso:
  python3 explainer_primewin.py [--estilo linha|candles] [--cenario ondas|tendencia_alta|tendencia_baixa]
                                [--dur 13] [--seed 11] [TITULO1] [TITULO2]
Cenários (alterne entre os vídeos; o CLIPE mostra o exemplo, a narração NÃO comenta a operação do gráfico):
  ondas                  -> compra nos fundos e sai nos topos (3 operações maiores)
  tendencia_alta/_baixa  -> VÁRIAS entradas curtas num mesmo movimento, cada uma ganhando poucos pontos
  longo_alta/_baixa      -> UMA entrada que pega um movimento longo, do início ao fim
  fibo_alta/_baixa       -> impulso, retração até 61,8% de Fibonacci (níveis desenhados), entrada e alvo em 161,8%
A parte de baixo (~25%) fica livre para as legendas. Nunca usar a palavra "robô" em nenhum texto."""
import argparse, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.animation import FuncAnimation, FFMpegWriter

ap=argparse.ArgumentParser()
ap.add_argument("--estilo",default="linha",choices=["linha","candles"])
ap.add_argument("--cenario",default="ondas",choices=["ondas","tendencia_alta","tendencia_baixa","longo_alta","longo_baixa","fibo_alta","fibo_baixa"])
ap.add_argument("--dur",type=float,default=13.0)
ap.add_argument("--seed",type=int,default=11)
ap.add_argument("titulos",nargs="*")
A=ap.parse_args()
T1=A.titulos[0] if len(A.titulos)>0 else "OPERAÇÕES"
T2=A.titulos[1] if len(A.titulos)>1 else "NO AUTOMÁTICO"
CY="#3fe0ff"; YE="#ffd23f"; PU="#8b5cf6"; BG="#0a0f2e"; RD="#ff5c8a"
rng=np.random.default_rng(A.seed); n=60; t=np.arange(n); PTS=10  # 1 unidade de preço = 10 pontos

# ---- séries e operações (entrada, saída, lado) ----
fib=None
sgn=-1 if A.cenario.endswith("_baixa") else 1
if A.cenario=="ondas":
    close=100+0.12*t+3.2*np.sin(2*np.pi*(t-5)/20)+rng.normal(0,0.18,n)
    trades=[]
    for c in (0,20,40):
        b=c+int(np.argmin(close[c:c+11])); s_=b+2+int(np.argmax(close[b+2:min(n,b+13)])); trades.append((b,s_,"C"))
    status_txt="AUTOMAÇÃO EXECUTANDO A ESTRATÉGIA"
elif A.cenario.startswith("tendencia"):
    close=100+sgn*0.32*t+0.9*np.sin(2*np.pi*t/8)*sgn*-1+rng.normal(0,0.12,n)
    trades=[]
    for c in range(3,n-6,8):   # entra em cada correção a favor da tendência, sai 3 candles depois
        e=c+(int(np.argmin(close[c:c+4])) if sgn>0 else int(np.argmax(close[c:c+4])))
        trades.append((e,min(n-1,e+3),"C" if sgn>0 else "V"))
    status_txt="VÁRIAS ENTRADAS NO MESMO MOVIMENTO"
elif A.cenario.startswith("longo"):
    base=0.3*t+0.8*np.sin(t/3.5)+rng.normal(0,0.15,n)
    close=100+sgn*base
    e=3+int(np.argmin(sgn*close[3:11])); s_=48+int(np.argmax(sgn*close[48:n]))
    trades=[(e,s_,"C" if sgn>0 else "V")]
    status_txt="UM MOVIMENTO LONGO, DO INÍCIO AO FIM"
else:  # fibo
    L,H=0.0,12.0; r618=H-0.618*(H-L); alvo=L+1.618*(H-L)
    path=np.interp(t,[0,6,24,35,58,59],[0.5,L,H,r618,alvo+0.4,alvo])
    up_=path+rng.normal(0,0.15,n); up_[6]=L-0.1; up_[24]=H+0.1; up_[35]=r618
    close=100+sgn*up_
    e=33+int(np.argmin(sgn*close[33:38]))
    s_=next((i for i in range(e+1,n) if sgn*(close[i]-100)>=alvo-0.3), n-1)
    trades=[(e,s_,"C" if sgn>0 else "V")]
    fib=[(lab,100+sgn*(H-f*(H-L))) for lab,f in (("0%",0),("38,2%",0.382),("50%",0.5),("61,8%",0.618),("100%",1.0),("161,8%",-0.618))]
    status_txt="ENTRADA NA RETRAÇÃO DE FIBONACCI"
def ganho(tr): e,s,l=tr; return (close[s]-close[e])*(1 if l=="C" else -1)*PTS
opn=np.r_[close[0],close[:-1]]+rng.normal(0,0.08,n)
hi=np.maximum(opn,close)+np.abs(rng.normal(0.35,0.15,n)); lo=np.minimum(opn,close)-np.abs(rng.normal(0.35,0.15,n))

fig=plt.figure(figsize=(7.2,12.8),dpi=150)
bgax=fig.add_axes([0,0,1,1]); bgax.axis("off")
g=np.linspace(0,1,256)[:,None]; bgax.imshow(g,aspect="auto",cmap=matplotlib.colors.LinearSegmentedColormap.from_list("b",[BG,"#1c0d45"]),extent=[0,1,0,1])
fig.text(0.5,0.935,T1,ha="center",va="center",fontsize=40,fontweight="bold",color="white")
fig.text(0.5,0.88,T2,ha="center",va="center",fontsize=40,fontweight="bold",color=YE)
status=fig.text(0.5,0.815,status_txt,ha="center",fontsize=17,color=CY,fontweight="bold")
ax=fig.add_axes([0.06,0.33,0.88,0.44]); ax.set_facecolor("none")
ax.set_xlim(-5,n+(10 if fib else 3)); ax.set_ylim(lo.min()-3,hi.max()+3.5); ax.axis("off")
for y in np.linspace(lo.min(),hi.max(),6): ax.axhline(y,color=PU,alpha=0.18,lw=1)

# ---- desenho do preço ----
if A.estilo=="linha":
    line,=ax.plot([],[],color=CY,lw=4); glow,=ax.plot([],[],color=CY,lw=12,alpha=0.15)
    def draw_price(k): line.set_data(t[:k],close[:k]); glow.set_data(t[:k],close[:k])
else:
    bodies=[]; wicks=[]
    for i in range(n):
        up=close[i]>=opn[i]; col=CY if up else RD
        w,=ax.plot([i,i],[lo[i],hi[i]],color=col,lw=1.6,alpha=0)
        r=Rectangle((i-0.33,min(opn[i],close[i])),0.66,max(abs(close[i]-opn[i]),0.08),color=col,alpha=0); ax.add_patch(r)
        wicks.append(w); bodies.append(r)
    def draw_price(k):
        for i in range(n): a=1.0 if i<k else 0.0; wicks[i].set_alpha(a); bodies[i].set_alpha(a)

# ---- níveis de Fibonacci (aparecem depois do impulso) ----
fibart=[]
if fib:
    for lab,y in fib:
        cor=YE if lab in ("61,8%","161,8%") else "#c9c3ff"
        l1=ax.plot([6,n],[y,y],color=cor,lw=1.6 if cor==YE else 1.0,ls=":",alpha=0)[0]
        l2=ax.text(n+0.8,y,lab,color=cor,fontsize=12,fontweight="bold",va="center",alpha=0)
        fibart+= [l1,l2]

# ---- marcadores das operações ----
big=not A.cenario.startswith("tendencia"); marks=[]
for tr in trades:
    e,s,l=tr; ent_up=(l=="C")
    ye=(lo[e]-0.6) if ent_up else (hi[e]+0.6); ys=(hi[s]+0.6) if ent_up else (lo[s]-0.6)
    me=ax.scatter([e],[ye],marker="^" if ent_up else "v",s=520 if big else 300,color=CY if ent_up else RD,edgecolor="white",lw=2,zorder=6,alpha=0)
    ms=ax.scatter([s],[ys],marker="v" if ent_up else "^",s=520 if big else 300,color=YE,edgecolor="white",lw=2,zorder=6,alpha=0)
    seg,=ax.plot([e,s],[close[e],close[s]],color=YE,lw=2,ls="--",alpha=0,zorder=4)
    if big:
        d=1 if ent_up else -1
        le=ax.text(e,ye-1.4*d,"COMPRA\nAUTOMÁTICA" if ent_up else "VENDA\nAUTOMÁTICA",ha="center",va="top" if ent_up else "bottom",fontsize=11,color=CY if ent_up else RD,fontweight="bold",alpha=0)
        ls=ax.text(s,ys+1.2*d,"SAÍDA\nAUTOMÁTICA",ha="center",va="bottom" if ent_up else "top",fontsize=11,color=YE,fontweight="bold",alpha=0)
    else:
        le=ax.text(e,ye+(-1.0 if ent_up else 1.0),"C" if ent_up else "V",ha="center",va="top" if ent_up else "bottom",fontsize=12,color=CY if ent_up else RD,fontweight="bold",alpha=0)
        ls=ax.text(s,ys+(1.0 if ent_up else -1.0),f"+{ganho(tr):.0f}",ha="center",va="bottom" if ent_up else "top",fontsize=14,color=YE,fontweight="bold",alpha=0)
    marks.append((tr,me,ms,seg,le,ls))
if not big:
    lab="COMPRA AUTOMÁTICA  →  SAÍDA" if trades[0][2]=="C" else "VENDA AUTOMÁTICA  →  SAÍDA"
    fig.text(0.5,0.785,lab,ha="center",fontsize=13,color="#c9c3ff")

pnl=fig.text(0.5,0.285,"",ha="center",fontsize=30,fontweight="bold",color=YE)
fig.text(0.5,0.255,"sem clicar em comprar ou vender",ha="center",fontsize=15,color="#c9c3ff")
fig.text(0.5,0.235,"Simulação ilustrativa",ha="center",fontsize=10,color="#8f89b8")

FPS=30; FR=int(A.dur*FPS); DRAW=int((A.dur-1.8)*FPS)
def up(f):
    k=min(n,int(n*f/DRAW)+1)
    draw_price(k)
    for (e,s,l),me,ms,seg,le,ls in marks:
        a1=1.0 if k>e else 0.0; a2=1.0 if k>s else 0.0
        me.set_alpha(a1); le.set_alpha(a1); ms.set_alpha(a2); ls.set_alpha(a2); seg.set_alpha(0.8*a2)
    for a in fibart: a.set_alpha(0.9 if k>25 else 0.0)
    done=[tr for tr in trades if k>tr[1]]
    g=sum(ganho(tr) for tr in done)
    if not done: pnl.set_text("aguardando sinal...")
    elif big: pnl.set_text(f"{g:+.0f} pontos")
    else: pnl.set_text(f"{len(done)} {'operação' if len(done)==1 else 'operações'}  {g:+.0f} pontos")
    status.set_alpha(0.55+0.45*abs(np.sin(f/6)))
    return []
assert all(ganho(tr)>0 for tr in trades), "cenário gerou operação negativa; troque --seed"
anim=FuncAnimation(fig,up,frames=FR)
anim.save("explicativo_anim.mp4",writer=FFMpegWriter(fps=FPS,codec="libx264",extra_args=["-pix_fmt","yuv420p"]))
up(FR-1); fig.savefig("explicativo_final.png")
print("ok", A.estilo, A.cenario, [round(ganho(tr)) for tr in trades])
