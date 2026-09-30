"""Trilha suave estilo lo-fi/acústico para os vídeos da @delíciadajoanna (gerada por código, sem direitos autorais).
Uso: from musica_suave import gerar; gerar("saida.wav", duracao_s, seed=0)"""
import numpy as np, soundfile as sf

def gerar(path, dur, sr=44100, bpm=84, seed=0):
    rng = np.random.default_rng(seed)
    n = int(dur * sr); t = np.arange(n) / sr; out = np.zeros(n)
    beat = 60 / bpm; bar = beat * 4
    # progressões suaves (Imaj7 - vi7 - IVmaj7 - V)
    progs = [[(60, 64, 67, 71), (57, 60, 64, 67), (53, 57, 60, 64), (55, 59, 62, 65)],
             [(62, 65, 69, 72), (57, 60, 64, 67), (58, 62, 65, 69), (60, 64, 67, 70)]]
    prog = progs[seed % 2]
    f = lambda m: 440 * 2 ** ((m - 69) / 12)
    def env(L, a=0.02, r=0.6):
        e = np.ones(L); A = int(a * sr); R = int(min(r * sr, L))
        e[:A] = np.linspace(0, 1, A); e[-R:] *= np.linspace(1, 0, R); return e
    # teclado elétrico macio (acordes)
    k = 0
    while k * bar < dur:
        ch = prog[k % 4]; s = int(k * bar * sr); L = min(int(bar * sr), n - s)
        if L <= 0: break
        tt = np.arange(L) / sr
        for m in ch:
            w = np.sin(2 * np.pi * f(m) * tt) + 0.25 * np.sin(2 * np.pi * 2 * f(m) * tt)
            out[s:s + L] += 0.05 * w * env(L, 0.08, 1.2) * np.exp(-tt * 0.35)
        # baixo
        bl = min(int(beat * 2 * sr), L); tb = np.arange(bl) / sr
        out[s:s + bl] += 0.09 * np.sin(2 * np.pi * f(ch[0] - 24) * tb) * env(bl, 0.01, 0.5)
        # arpejo delicado (tipo kalimba)
        for j in range(8):
            ps = s + int(j * beat / 2 * sr); pl = min(int(0.5 * sr), n - ps)
            if pl <= 0: break
            tp = np.arange(pl) / sr; m = ch[(j * 2 + k) % 4] + 12
            out[ps:ps + pl] += 0.035 * np.sin(2 * np.pi * f(m) * tp) * np.exp(-tp * 7)
        k += 1
    # percussão leve: rimshot/hat suaves
    nb = int(dur / beat)
    for b in range(nb):
        s = int(b * beat * sr)
        if b % 2 == 1:  # snare leve
            L = min(int(0.12 * sr), n - s); out[s:s + L] += 0.03 * rng.normal(0, 1, L) * np.exp(-np.arange(L) / sr * 30)
        for h in (0, 0.5):  # hat
            hs = s + int(h * beat * sr); L = min(int(0.04 * sr), n - hs)
            if L > 0: out[hs:hs + L] += 0.012 * rng.normal(0, 1, L) * np.exp(-np.arange(L) / sr * 90)
        if b % 4 == 0:  # kick macio
            L = min(int(0.25 * sr), n - s); tk = np.arange(L) / sr
            out[s:s + L] += 0.12 * np.sin(2 * np.pi * (55 + 40 * np.exp(-tk * 25)) * tk) * np.exp(-tk * 12)
    # vinil suave
    out += 0.003 * rng.normal(0, 1, n)
    fade = int(1.5 * sr); out[:fade] *= np.linspace(0, 1, fade); out[-fade:] *= np.linspace(1, 0, fade)
    out /= max(1e-9, np.abs(out).max()) / 0.8
    sf.write(path, out.astype(np.float32), sr)
