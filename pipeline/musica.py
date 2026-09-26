"""Trilha animada gerada por código (sem direitos autorais): batida 118 BPM, bumbo, chimbal, baixo, acordes e arpejo."""
import numpy as np, wave, sys
def gerar(path, dur, sr=44100, bpm=118, seed=0):
    rng=np.random.default_rng(seed); n=int(sr*dur); out=np.zeros(n)
    beat=60/bpm; t=np.arange(n)/sr
    def put(sig,start):
        i=int(start*sr); j=min(n,i+len(sig))
        if i<n: out[i:j]+=sig[:j-i]
    # sons
    kl=int(0.35*sr); kt=np.arange(kl)/sr
    kick=np.sin(2*np.pi*(50+90*np.exp(-kt*30))*kt)*np.exp(-kt*9)*0.9
    hl=int(0.05*sr); hat=rng.normal(0,1,hl)*np.exp(-np.arange(hl)/sr*90)*0.18
    cl=int(0.2*sr); clap=rng.normal(0,1,cl)*np.exp(-np.arange(cl)/sr*25)*0.35
    prog=[[57,60,64],[53,57,60],[48,55,60],[55,59,62]]   # Am F C G
    f=lambda m:440*2**((m-69)/12)
    nb=int(dur/beat)+1
    for b in range(nb):
        s=b*beat; bar=b//4; ch=prog[bar%4]
        put(kick,s)
        if b%4 in (1,3): put(clap,s)
        put(hat,s+beat/2); put(hat*0.6,s)
        # baixo (colcheias na tônica)
        for k in range(2):
            bl=int(beat/2*sr*0.9); bt=np.arange(bl)/sr
            put(np.sign(np.sin(2*np.pi*f(ch[0]-24)*bt))*0.22*np.exp(-bt*4),s+k*beat/2)
        # acorde (stab no 1 e no "e" do 2)
        if b%4 in (0,2):
            al=int(beat*0.8*sr); at=np.arange(al)/sr
            put(sum(np.sin(2*np.pi*f(m)*at)+0.4*np.sin(4*np.pi*f(m)*at) for m in ch)*0.07*np.exp(-at*3),s)
        # arpejo em semicolcheias
        for k in range(4):
            m=ch[k%3]+12+(12 if k==3 else 0); pl=int(beat/4*sr); pt=np.arange(pl)/sr
            put(np.sin(2*np.pi*f(m)*pt)*np.exp(-pt*18)*0.08,s+k*beat/4)
    # fade in/out
    fi=int(0.5*sr); out[:fi]*=np.linspace(0,1,fi); fo=int(1.5*sr); out[-fo:]*=np.linspace(1,0,fo)
    out=out/np.abs(out).max()*0.9
    w=wave.open(path,"wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((out*32767).astype(np.int16).tobytes()); w.close()
if __name__=="__main__": gerar(sys.argv[1], float(sys.argv[2]))
