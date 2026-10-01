"""Trilha INSPIRADORA (mais alegre e atrativa) para o Grana e Finanças — aprovada pelo usuário em 30/09
no lugar da trilha escura. Gerada por código, sem direitos autorais.

Ré maior (~104 BPM), progressão motivacional (D–A–Bm–G ou G–D–Em–C, conforme o seed):
- arpejo "pluck" brilhante em colcheias (o gancho que prende a atenção);
- pad quente, baixo seguindo a fundamental;
- kick + palmas + chimbal leves (entram depois da abertura e crescem);
- "impactos" com prato/riser nas viradas do roteiro (mesma interface da trilha antiga).
Uso: gerar(caminho, duração, impactos=[s1, s2, ...], seed=0)
"""
import numpy as np, wave

SR = 44100


def _lp(x, cutoff):
    from scipy.signal import lfilter
    a = np.exp(-2 * np.pi * cutoff / SR)
    return lfilter([1 - a], [1, -a], x)


def _hp(x, cutoff):
    return x - _lp(x, cutoff)


def _reverb(x, secs=1.8, mix=0.25, seed=1):
    from scipy.signal import oaconvolve
    rng = np.random.default_rng(seed); n = int(secs * SR); t = np.arange(n) / SR
    ir = rng.normal(0, 1, n) * np.exp(-t * 6.9 / secs); ir /= np.sqrt((ir ** 2).sum())
    wet = oaconvolve(x, ir)[:len(x)]
    return (1 - mix) * x + mix * wet / (np.abs(wet).max() + 1e-9) * np.abs(x).max()


def _add(buf, i, sig, g=1.0):
    if i >= len(buf) or i < 0: return
    j = min(len(buf), i + len(sig)); buf[i:j] += sig[:j - i] * g


def gerar(path, dur, impactos=(), seed=0, bpm=104):
    rng = np.random.default_rng(seed); n = int(SR * (dur + 1)); f = lambda m: 440 * 2 ** ((m - 69) / 12)
    beat = 60 / bpm; bar = 4 * beat
    progs = [[[62, 66, 69], [57, 61, 64], [59, 62, 66], [55, 59, 62]],    # D A Bm G
             [[55, 59, 62], [62, 66, 69], [64, 67, 71], [60, 64, 67]]]    # G D Em C
    prog = progs[seed % 2]
    nb = int(dur / bar) + 2
    pad = np.zeros(n); arp = np.zeros(n); bass = np.zeros(n); drums = np.zeros(n)
    # pad quente (senos + leve serra filtrada), 1 acorde por compasso
    L = int(bar * SR); tt = np.arange(L) / SR; env = np.minimum(1, tt / 0.25) * np.minimum(1, (bar - tt) / 0.3 + 0.1)
    for k in range(nb):
        s = np.zeros(L)
        for m in prog[k % 4]:
            s += np.sin(2 * np.pi * f(m) * tt) + 0.3 * (2 * ((f(m) * 1.003 * tt) % 1) - 1)
        _add(pad, int(k * bar * SR), s * env, 0.05)
    pad = _lp(pad, 2200)
    # arpejo pluck em colcheias (padrão 1-3-5-8-5-3-5-8), brilhante, com eco
    pl = int(0.45 * SR); pt = np.arange(pl) / SR
    for k in range(nb):
        ch = prog[k % 4]; notes = [ch[0], ch[1], ch[2], ch[0] + 12, ch[2], ch[1], ch[2], ch[0] + 12]
        for j, m in enumerate(notes):
            m += 12; w = (np.sin(2 * np.pi * f(m) * pt) + 0.35 * np.sin(4 * np.pi * f(m) * pt) + 0.12 * np.sin(6 * np.pi * f(m) * pt))
            w *= np.exp(-pt * 9) * np.minimum(1, pt / 0.002)
            _add(arp, int((k * bar + j * beat / 2) * SR), w, 0.07 * (1.0 if j % 2 == 0 else 0.8))
    d = int(beat * 0.75 * SR)
    arp = arp + np.concatenate([np.zeros(d), arp[:-d]]) * 0.35   # eco em semínima pontuada
    # baixo: fundamental em colcheias "pulsando"
    bl = int(beat / 2 * SR); bt = np.arange(bl) / SR
    for k in range(nb):
        m = prog[k % 4][0] - 24
        for j in range(8):
            w = np.sin(2 * np.pi * f(m) * bt) + 0.3 * np.sin(4 * np.pi * f(m) * bt)
            _add(bass, int((k * bar + j * beat / 2) * SR), w * np.exp(-bt * 6) * np.minimum(1, bt / 0.005), 0.11)
    # bateria leve: entra após 2 compassos; palmas no 2 e 4; chimbal em colcheias
    kl = int(0.3 * SR); kt = np.arange(kl) / SR
    kick = np.sin(2 * np.pi * (48 + 70 * np.exp(-kt * 35)) * kt) * np.exp(-kt * 10)
    cl = int(0.18 * SR); ct = np.arange(cl) / SR
    clap = _hp(rng.normal(0, 1, cl), 900) * np.exp(-ct * 22)
    hl = int(0.05 * SR); ht = np.arange(hl) / SR
    hat = _hp(rng.normal(0, 1, hl), 6000) * np.exp(-ht * 70)
    for k in range(int(dur / beat) + 2):
        s = k * beat; ramp = min(1.0, max(0.0, (s - 2 * bar) / (2 * bar)))
        if s < 2 * bar: continue
        if k % 2 == 0: _add(drums, int(s * SR), kick, 0.55 * ramp)
        else: _add(drums, int(s * SR), clap, 0.16 * ramp)
        for h in (0, 0.5): _add(drums, int((s + h * beat) * SR), hat, 0.05 * ramp * (1 if h else 0.7))
    # impactos: prato + kick grave nas viradas, com riser curto antes
    im = np.zeros(n); il = int(2.2 * SR); it = np.arange(il) / SR
    crash = _hp(rng.normal(0, 1, il), 3000) * np.exp(-it * 2.2) * 0.35 + np.sin(2 * np.pi * (40 + 60 * np.exp(-it * 20)) * it) * np.exp(-it * 5)
    rl = int(1.0 * SR); rt = np.arange(rl) / SR
    riser = _hp(rng.normal(0, 1, rl), 2000) * (rt / 1.0) ** 2 * 0.25
    for s in impactos:
        _add(im, int((s - 1.0) * SR), riser); _add(im, int(s * SR), crash)
    im = _reverb(im, 1.5, 0.3, seed=3)
    out = pad + _reverb(arp, 1.6, 0.25) + bass + drums + im * 0.5
    out = out[:int(SR * dur)]
    fi = int(0.8 * SR); out[:fi] *= np.linspace(0, 1, fi); fo = int(2.0 * SR); out[-fo:] *= np.linspace(1, 0, fo)
    out = out / (np.abs(out).max() + 1e-9) * 0.9
    w = wave.open(path, "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((out * 32767).astype(np.int16).tobytes()); w.close()


if __name__ == "__main__":
    import sys; gerar(sys.argv[1], float(sys.argv[2]), impactos=[0.2, 8, 20], seed=int(sys.argv[3]) if len(sys.argv) > 3 else 0)
