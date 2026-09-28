"""Trilha DARK para o Grana e Finanças (credibilidade, tom sério), gerada por código — sem direitos autorais.

Ré menor, ~84 BPM, progressão cinematográfica i–VI–iv–V (Dm–Bb–Gm–A): pad grave escuro, sub-baixo,
batida de "coração" (bumbo nos tempos 1 e 3), chimbal discreto e notas de piano esparsas com eco.
"""
import numpy as np, wave


def _lowpass(x, cutoff, sr):
    a = np.exp(-2 * np.pi * cutoff / sr); y = np.empty_like(x); acc = 0.0
    for i, v in enumerate(x):
        acc = (1 - a) * v + a * acc; y[i] = acc
    return y


def gerar(path, dur, sr=44100, bpm=84, seed=0):
    rng = np.random.default_rng(seed); n = int(sr * dur); out = np.zeros(n)
    beat = 60 / bpm; bar = 4 * beat
    f = lambda m: 440 * 2 ** ((m - 69) / 12)
    def put(sig, start):
        i = int(start * sr); j = min(n, i + len(sig))
        if 0 <= i < n: out[i:j] += sig[:j - i]
    prog = [[50, 53, 57], [46, 50, 53], [43, 46, 50], [45, 49, 52]]   # Dm Bb Gm A
    nbars = int(dur / bar) + 2
    # pad escuro (serras levemente desafinadas, filtradas), ataque lento
    L = int(bar * sr); t = np.arange(L) / sr
    env = np.minimum(1, t / 1.2) * np.minimum(1, (bar - t) / 0.8 + 0.3)
    for b in range(nbars):
        ch = prog[b % 4]; sig = np.zeros(L)
        for m in ch:
            for det in (-0.12, 0.12):
                ph = 2 * np.pi * f(m + det) * t
                sig += (2 * ((ph / (2 * np.pi)) % 1) - 1) * 0.5
        sig = _lowpass(sig * env, 700, sr) * 0.05
        put(sig, b * bar)
        # sub-baixo (seno na tônica, uma oitava abaixo)
        put(np.sin(2 * np.pi * f(ch[0] - 12) * t) * env * 0.22, b * bar)
    # batida de coração e chimbal discreto
    kl = int(0.4 * sr); kt = np.arange(kl) / sr
    kick = np.sin(2 * np.pi * (45 + 60 * np.exp(-kt * 25)) * kt) * np.exp(-kt * 7) * 0.8
    hl = int(0.04 * sr); hat = rng.normal(0, 1, hl) * np.exp(-np.arange(hl) / sr * 120) * 0.05
    for k in range(int(dur / beat) + 1):
        s = k * beat
        if k % 4 in (0, 2): put(kick, s)
        if k % 4 == 2: put(kick * 0.45, s + beat * 0.35)
        put(hat, s + beat / 2)
    # piano esparso (notas do acorde, 2 oitavas acima) com eco
    pl = int(2.5 * sr); pt = np.arange(pl) / sr
    for b in range(nbars):
        ch = prog[b % 4]
        for q, idx in ((0, 2), (1.5, 1), (3, 0)):
            if rng.random() < 0.8:
                m = ch[idx] + 24
                note = (np.sin(2 * np.pi * f(m) * pt) + 0.3 * np.sin(4 * np.pi * f(m) * pt)) * np.exp(-pt * 2.2) * 0.06
                for e, g in ((0, 1), (0.36, 0.4), (0.72, 0.16)): put(note * g, b * bar + q * beat + e)
    fi = int(1.0 * sr); out[:fi] *= np.linspace(0, 1, fi)
    fo = int(2.0 * sr); out[-fo:] *= np.linspace(1, 0, fo)
    out = out / np.abs(out).max() * 0.9
    w = wave.open(path, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
    w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()


if __name__ == "__main__":
    import sys; gerar(sys.argv[1], float(sys.argv[2]))
