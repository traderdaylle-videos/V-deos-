"""Trilha CINEMATOGRÁFICA escura (estilo documentário/estoico) para o Grana e Finanças. Gerada por código,
sem direitos autorais.

Ré menor lento (~64 BPM): drone grave que respira, pad escuro com acordes longos (Dm–Bb–Gm–A, 2 compassos cada),
piano grave esparso com reverb longo, batida de coração discreta e IMPACTOS graves ("boom") nos instantes
pedidos (viradas do roteiro). Uso: gerar(caminho, duração, impactos=[s1, s2, ...], seed=0)
"""
import numpy as np, wave

SR = 44100


def _reverb(x, secs=3.2, mix=0.45, seed=1):
    rng = np.random.default_rng(seed); n = int(secs * SR); t = np.arange(n) / SR
    ir = rng.normal(0, 1, n) * np.exp(-t * 6.9 / secs)
    ir = np.convolve(ir, np.ones(8) / 8, mode="same"); ir /= np.sqrt((ir ** 2).sum())   # escurece o reverb
    m = len(x) + n - 1; N = 1 << (m - 1).bit_length()
    wet = np.fft.irfft(np.fft.rfft(x, N) * np.fft.rfft(ir, N), N)[:len(x)]
    return (1 - mix) * x + mix * wet / (np.abs(wet).max() + 1e-9) * np.abs(x).max()


def _lp(x, cutoff):   # passa-baixa de 1 polo via FFT (rápido)
    N = len(x); F = np.fft.rfftfreq(N, 1 / SR)
    return np.fft.irfft(np.fft.rfft(x) / (1 + 1j * F / cutoff), N)


def gerar(path, dur, impactos=(), seed=0, bpm=64):
    rng = np.random.default_rng(seed); n = int(SR * (dur + 1)); t = np.arange(n) / SR
    f = lambda m: 440 * 2 ** ((m - 69) / 12)
    beat = 60 / bpm; bar = 4 * beat; seg = 2 * bar
    prog = [[50, 53, 57], [46, 50, 53], [43, 46, 50], [45, 49, 52]]   # Dm Bb Gm A
    # 1) drone grave que "respira"
    breath = 0.75 + 0.25 * np.sin(2 * np.pi * t / 9.0)
    drone = (np.sin(2 * np.pi * f(26) * t) * 0.55 + np.sin(2 * np.pi * f(38) * t) * 0.35
             + np.sin(2 * np.pi * f(45) * t + 0.3) * 0.12) * breath
    # 2) pad escuro (serras desafinadas filtradas), acorde muda a cada 2 compassos
    pad = np.zeros(n); L = int(seg * SR); tt = np.arange(L) / SR
    env = np.minimum(1, tt / 2.0) * np.minimum(1, (seg - tt) / 1.5 + 0.2)
    for k in range(int(dur / seg) + 2):
        s = np.zeros(L)
        for m in prog[k % 4]:
            for det in (-0.1, 0.0, 0.1):
                s += 2 * ((f(m + det) * tt) % 1) - 1
        i = int(k * seg * SR); j = min(n, i + L)
        if i < n: pad[i:j] += (s * env)[:j - i]
    pad = _lp(pad, 380) * 0.09
    # 3) piano grave esparso (uma nota a cada 2 tempos, notas do acorde), com reverb longo
    pn = np.zeros(n); pl = int(4 * SR); pt = np.arange(pl) / SR
    for k in range(int(dur / (2 * beat)) + 1):
        if k < 2 or rng.random() < 0.3: continue
        ch = prog[int(k * 2 * beat / seg) % 4]; m = ch[rng.integers(0, 3)] + 12
        note = (np.sin(2 * np.pi * f(m) * pt) + 0.25 * np.sin(4 * np.pi * f(m) * pt) + 0.08 * np.sin(6 * np.pi * f(m) * pt))
        note *= np.exp(-pt * 1.4) * np.minimum(1, pt / 0.004) * (0.8 + 0.2 * rng.random())
        i = int(k * 2 * beat * SR); j = min(n, i + pl)
        pn[i:j] += note[:j - i] * 0.13
    pn = _reverb(pn, 3.5, 0.55)
    # 4) batida de coração (entra depois de ~6s), bem abafada
    hb = np.zeros(n); kl = int(0.35 * SR); kt = np.arange(kl) / SR
    kick = np.sin(2 * np.pi * (40 + 45 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 9)
    for k in range(int(dur / beat) + 1):
        s = k * beat
        if s < 6 or k % 2: continue
        for off, g in ((0, 0.5), (0.28, 0.28)):
            i = int((s + off) * SR); j = min(n, i + kl)
            if i < n: hb[i:j] += kick[:j - i] * g
    # 5) impactos graves nas viradas do roteiro
    im = np.zeros(n); il = int(3.5 * SR); it = np.arange(il) / SR
    boom = (np.sin(2 * np.pi * (30 + 50 * np.exp(-it * 6)) * it) * np.exp(-it * 1.6)
            + _lp(rng.normal(0, 1, il), 300) * np.exp(-it * 3) * 0.6)
    for s in impactos:
        i = int(s * SR); j = min(n, i + il)
        if 0 <= i < n: im[i:j] += boom[:j - i] * 0.9
    im = _reverb(im, 2.5, 0.35, seed=3)
    out = drone * 0.22 + pad + pn + hb * 0.55 + im * 0.6
    out = out[:int(SR * dur)]
    fi = int(1.5 * SR); out[:fi] *= np.linspace(0, 1, fi); fo = int(2.5 * SR); out[-fo:] *= np.linspace(1, 0, fo)
    out = out / (np.abs(out).max() + 1e-9) * 0.9
    w = wave.open(path, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()


if __name__ == "__main__":
    import sys; gerar(sys.argv[1], float(sys.argv[2]), impactos=[0.2, 8, 20])
