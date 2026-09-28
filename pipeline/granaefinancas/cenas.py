"""Cenas animadas da identidade Grana e Finanças (verde-petróleo + dourado), 1080x1920, 30 fps.

Cada cena recebe a duração total e os instantes (em segundos, relativos ao início da cena) em que cada
elemento deve aparecer, para ficar sincronizada com a narração. O QUARTO INFERIOR fica livre para as legendas.
"""
import os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib.patches import FancyBboxPatch, Circle

FPS = 30
HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "fonts")
ANTON = fm.FontProperties(fname=os.path.join(FONTS, "Anton-Regular.ttf"))
MXB = fm.FontProperties(fname=os.path.join(FONTS, "Montserrat-ExtraBold.ttf"))
MSB = fm.FontProperties(fname=os.path.join(FONTS, "Montserrat-SemiBold.ttf"))

# Paleta do Instagram @granaefinancas
BG1, BG2 = "#04342C", "#085041"
GOLD, GOLD_SOFT = "#E8B84A", "#F3D98B"
WHITE, MUTED = "#FFFFFF", "#B9D3CC"
CORAL = "#E8765C"


def _base():
    fig = plt.figure(figsize=(7.2, 12.8), dpi=150)
    bg = fig.add_axes([0, 0, 1, 1], zorder=-10)
    g = np.linspace(0, 1, 256)[:, None]
    from matplotlib.colors import LinearSegmentedColormap
    cm = LinearSegmentedColormap.from_list("gf", [BG2, BG1])
    bg.imshow(g, aspect="auto", cmap=cm, extent=[0, 1, 0, 1])
    # moedas/círculos dourados discretos no fundo (cenário ilustrado, nunca fundo liso)
    rng = np.random.default_rng(7)
    for _ in range(14):
        x, y, r = rng.uniform(0, 1), rng.uniform(0.25, 1), rng.uniform(0.02, 0.07)
        bg.add_patch(Circle((x, y), r, fill=False, ec=GOLD, lw=1.2, alpha=0.10))
    bg.set_xlim(0, 1); bg.set_ylim(0, 1); bg.axis("off")
    fig.text(0.5, 0.965, "GRANA E FINANÇAS", ha="center", va="center", fontproperties=MXB,
             fontsize=15, color=GOLD, alpha=0.9)
    return fig


def _alpha(t, t0, fade=0.35):
    return float(np.clip((t - t0) / fade, 0, 1))


def _save(fig, update, dur, out_mp4, out_png=None, alpha=False):
    n = max(1, int(round(dur * FPS)))
    anim = FuncAnimation(fig, lambda f: update(f / FPS), frames=n, blit=False)
    if alpha:   # .mov com canal alfa (para sobrepor a um clipe real)
        anim.save(out_mp4, writer=FFMpegWriter(fps=FPS, codec="png"), savefig_kwargs={"transparent": True})
    else:
        anim.save(out_mp4, writer=FFMpegWriter(fps=FPS, codec="libx264",
                                               extra_args=["-pix_fmt", "yuv420p", "-crf", "20"]))
    if out_png:
        update(dur); fig.savefig(out_png)
    plt.close(fig)


def pessoa(ax, x, y, s, color, fill):
    """Ícone de pessoa (cabeça + corpo) em coordenadas do eixo."""
    head = Circle((x, y + 0.62 * s), 0.22 * s, fc=color if fill else "none", ec=color, lw=3)
    body = FancyBboxPatch((x - 0.36 * s, y - 0.45 * s), 0.72 * s, 0.78 * s,
                          boxstyle=f"round,pad=0,rounding_size={0.3 * s}",
                          fc=color if fill else "none", ec=color, lw=3)
    ax.add_patch(head); ax.add_patch(body)
    return head, body


def cena_estatistica(dur, t_badge, t_frase, out_mp4, out_png,
                     pct=82, texto_pct="das famílias brasileiras\nestão endividadas",
                     badge="CONTA DE LUZ: +7,42% EM SETEMBRO",
                     frase="O problema quase nunca é o salário.\nÉ o comportamento.",
                     fonte="Fontes: CNC (Peic) e IBGE (IPCA-15 de setembro/2026)"):
    fig = _base()
    num = fig.text(0.5, 0.855, "0%", ha="center", va="center", fontproperties=ANTON, fontsize=120, color=GOLD)
    sub = fig.text(0.5, 0.745, texto_pct, ha="center", va="center", fontproperties=MXB, fontsize=25,
                   color=WHITE, linespacing=1.25)
    ax = fig.add_axes([0.08, 0.50, 0.84, 0.19]); ax.set_xlim(0, 10); ax.set_ylim(-0.1, 4.2); ax.axis("off")
    icons = []
    for i in range(10):
        r, c = divmod(i, 5)
        x, y = 1 + c * 2, 3.0 - r * 2.1
        icons.append((pessoa(ax, x, y, 1.15, GOLD, False), pessoa(ax, x, y, 1.15, CORAL, True)))
    for _, filled in icons:
        for p in filled: p.set_alpha(0)
    n_fill = int(round(pct / 10))
    # selo da conta de luz
    bax = fig.add_axes([0.08, 0.405, 0.84, 0.065]); bax.axis("off"); bax.set_xlim(0, 1); bax.set_ylim(0, 1)
    box = FancyBboxPatch((0.01, 0.08), 0.98, 0.84, boxstyle="round,pad=0,rounding_size=0.25",
                         fc=GOLD, ec="none", transform=bax.transAxes)
    bax.add_patch(box)
    btxt = bax.text(0.5, 0.5, badge or "", ha="center", va="center", fontproperties=MXB, fontsize=19, color=BG1)
    fr = fig.text(0.5, 0.325, frase, ha="center", va="center", fontproperties=MXB, fontsize=24,
                  color=GOLD_SOFT, linespacing=1.3)
    src = fig.text(0.5, 0.265, fonte, ha="center", va="center", fontproperties=MSB, fontsize=11, color=MUTED)
    t_count = 0.7   # gancho: o número já aparece grande no primeiro quadro e sobe rápido

    def up(t):
        k = min(1.0, t / t_count); e = 1 - (1 - k) ** 3
        num.set_text(f"{pct}%")   # gancho: número final já no 1º quadro (vira a capa)
        num.set_fontsize(120 * (1 + 0.10 * np.exp(-3 * max(0, t - t_count)) * (t >= t_count)))
        sub.set_alpha(1.0)
        for i, (_, filled) in enumerate(icons):
            a = _alpha(t, i * 0.06, 0.1) if i < n_fill else 0
            for p in filled: p.set_alpha(a)
        a = _alpha(t, t_badge) if badge else 0; box.set_alpha(a); btxt.set_alpha(a)
        fr.set_alpha(_alpha(t, t_frase)); src.set_alpha(0.9 * _alpha(t, 0.5))
    _save(fig, up, dur, out_mp4, out_png)


def cena_lista(dur, titulo, itens, tempos, out_mp4, out_png, destaque=None):
    """Lista numerada que aparece item a item nos instantes de `tempos`."""
    fig = _base()
    tt = fig.text(0.5, 0.86, titulo, ha="center", va="center", fontproperties=ANTON, fontsize=58,
                  color=WHITE, linespacing=1.05)
    rows = []
    y0, dy = 0.70, 0.135
    for i, txt in enumerate(itens):
        y = y0 - i * dy
        ax = fig.add_axes([0.07, y - 0.05, 0.86, 0.105]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        card = FancyBboxPatch((0.0, 0.05), 1.0, 0.9, boxstyle="round,pad=0,rounding_size=0.18",
                              fc=BG1, ec=GOLD, lw=2.5, transform=ax.transAxes)
        ax.add_patch(card)
        circ = FancyBboxPatch((0.03, 0.2), 0.11, 0.6, boxstyle="round,pad=0,rounding_size=0.05",
                              fc=GOLD, ec="none", transform=ax.transAxes)
        ax.add_patch(circ)
        numt = ax.text(0.085, 0.48, str(i + 1), ha="center", va="center", fontproperties=ANTON, fontsize=32, color=BG1)
        tx = ax.text(0.19, 0.5, txt, ha="left", va="center", fontproperties=MXB, fontsize=21, color=WHITE,
                     linespacing=1.2)
        rows.append((ax, [card, circ, numt, tx]))
    dest = fig.text(0.5, 0.29, destaque or "", ha="center", va="center", fontproperties=MXB, fontsize=22,
                    color=GOLD_SOFT, linespacing=1.3)
    circ_fix = []

    def up(t):
        tt.set_alpha(_alpha(t, 0.0))
        for (ax, els), t0 in zip(rows, tempos):
            a = _alpha(t, t0, 0.3)
            for e in els: e.set_alpha(a)
            # desliza da direita
            pos = ax.get_position()
            ax.set_position([0.07 + 0.12 * (1 - a) ** 2, pos.y0, pos.width, pos.height])
        dest.set_alpha(_alpha(t, tempos[-1] + 1.2) if destaque else 0)
    _save(fig, up, dur, out_mp4, out_png)


def cena_final(dur, out_mp4, handle="@granaefinancas", chamada="Segue pra mais\neducação financeira",
               aviso="Conteúdo educativo. Não é recomendação de investimento."):
    fig = _base()
    g = fig.text(0.5, 0.80, "GOSTOU?", ha="center", va="center", fontproperties=ANTON, fontsize=86, color=WHITE)
    c = fig.text(0.5, 0.685, chamada, ha="center", va="center", fontproperties=MXB, fontsize=28, color=MUTED,
                 linespacing=1.3)
    bax = fig.add_axes([0.1, 0.52, 0.8, 0.085]); bax.axis("off"); bax.set_xlim(0, 1); bax.set_ylim(0, 1)
    box = FancyBboxPatch((0.0, 0.05), 1.0, 0.9, boxstyle="round,pad=0,rounding_size=0.3", fc=GOLD, ec="none",
                         transform=bax.transAxes)
    bax.add_patch(box)
    h = bax.text(0.5, 0.5, handle, ha="center", va="center", fontproperties=MXB, fontsize=32, color=BG1)
    q = fig.text(0.5, 0.435, "Comenta aqui: qual hábito você\nvai começar hoje?", ha="center", va="center",
                 fontproperties=MSB, fontsize=19, color=GOLD_SOFT, linespacing=1.3)
    av = fig.text(0.5, 0.285, aviso, ha="center", va="center", fontproperties=MSB, fontsize=12, color=MUTED)

    def up(t):
        g.set_alpha(_alpha(t, 0.0)); c.set_alpha(_alpha(t, 0.3))
        s = 1 + 0.045 * np.sin(t * 5) if t > 0.8 else 1
        a = _alpha(t, 0.6); box.set_alpha(a); h.set_alpha(a); h.set_fontsize(32 * s)
        q.set_alpha(_alpha(t, 1.2)); av.set_alpha(_alpha(t, 0.2))
    _save(fig, up, dur, out_mp4)


def cena_final_sobre_clipe(dur, out_mov, linhas):
    """Textos do cartão final com fundo TRANSPARENTE (.mov), para sobrepor a um clipe real de dinheiro.
    linhas: [{"t":..., "y":..., "size":..., "cor":"gold|white|soft", "fonte":"anton|mxb|msb", "caixa":bool, "t0":seg}]"""
    fig = plt.figure(figsize=(7.2, 12.8), dpi=150); fig.patch.set_alpha(0)
    cores = {"gold": GOLD, "white": WHITE, "soft": GOLD_SOFT, "bg": BG1}
    fontes = {"anton": ANTON, "mxb": MXB, "msb": MSB}
    fig.text(0.5, 0.965, "GRANA E FINANÇAS", ha="center", va="center", fontproperties=MXB, fontsize=15, color=GOLD)
    els = []
    for L in linhas:
        if L.get("caixa"):
            ax = fig.add_axes([0.08, L["y"] - 0.045, 0.84, 0.09]); ax.axis("off"); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
            box = FancyBboxPatch((0, 0.05), 1, 0.9, boxstyle="round,pad=0,rounding_size=0.3", fc=GOLD, ec="none",
                                 transform=ax.transAxes)
            ax.add_patch(box)
            tx = ax.text(0.5, 0.5, L["t"], ha="center", va="center", fontproperties=fontes[L.get("fonte", "mxb")],
                         fontsize=L.get("size", 30), color=BG1)
            els.append((L, [box, tx], tx))
        else:
            tx = fig.text(0.5, L["y"], L["t"], ha="center", va="center", fontproperties=fontes[L.get("fonte", "mxb")],
                          fontsize=L.get("size", 28), color=cores[L.get("cor", "white")], linespacing=1.2)
            tx.set_path_effects([__import__("matplotlib.patheffects", fromlist=["x"]).withStroke(linewidth=6, foreground=BG1)])
            els.append((L, [tx], tx))

    def up(t):
        for L, parts, tx in els:
            a = _alpha(t, L.get("t0", 0), 0.3)
            for p in parts: p.set_alpha(a)
            if L.get("caixa") and t > L.get("t0", 0) + 0.6:
                tx.set_fontsize(L.get("size", 30) * (1 + 0.04 * np.sin(t * 5)))
    _save(fig, up, dur, out_mov, alpha=True)
