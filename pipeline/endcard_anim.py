"""Cartão final ANIMADO (chamada para ação), estilo Reels.

Fundo: clipe de vídeo real em movimento com véu da marca (azul-marinho -> roxo).
Por cima, com animação:
  - logo (PRIME ciano / WIN amarelo, fonte Anton) descendo;
  - botão amarelo pulsando "COMENTE PRIME";
  - cartão de comentário simulado digitando "PRIME" e coração;
  - setas pulando;
  - selo da 5PI e aviso de risco.
A parte de baixo (~1480-1700px) fica livre para as legendas.

Uso via make_video.py com spec "endcard": {"animado": true, "bg_clip": "arquivo.mp4", ...}
Chaves opcionais do "endcard": marca1, marca2, tagline, botao, sub, comentario, usuario, selo, aviso,
cor1, cor2, bg, clip_offset.
"""
import math, os, subprocess as sp
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
F_ANTON = os.path.join(HERE, "fonts", "Anton-Regular.ttf")
F_XB = os.path.join(HERE, "fonts", "Montserrat-ExtraBold.ttf")
F_SB = os.path.join(HERE, "fonts", "Montserrat-SemiBold.ttf")
W, H, FPS = 1080, 1920, 30


def _hex(c, a=255):
    c = c.lstrip("#"); return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), a)


def _ease_out(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3


def _pop(x):  # 0 -> overshoot -> 1
    x = max(0.0, min(1.0, x))
    return 1 + 2.2 * (x - 1) ** 3 + 1.2 * (x - 1) ** 2 if x < 1 else 1.0


def render(bg_clip, dur, out, cfg=None):
    cfg = cfg or {}
    c1, c2 = cfg.get("cor1", "#3fe0ff"), cfg.get("cor2", "#ffd23f")
    navy = _hex(cfg.get("bg", "#0a0f2e"))
    f_logo = ImageFont.truetype(F_ANTON, 190)
    f_btn = ImageFont.truetype(F_ANTON, 112)
    f_tag = ImageFont.truetype(F_XB, 34)
    f_sub = ImageFont.truetype(F_SB, 42)
    f_user = ImageFont.truetype(F_XB, 34)
    f_com = ImageFont.truetype(F_XB, 52)
    f_chip = ImageFont.truetype(F_XB, 33)
    f_av = ImageFont.truetype(F_XB, 22)

    m1, m2 = cfg.get("marca1", "PRIME"), cfg.get("marca2", "WIN")
    tag = cfg.get("tagline", "AUTOMAÇÕES DE MERCADO FINANCEIRO")
    tag = "   ".join(" ".join(w) for w in tag.split())          # espaçamento largo entre letras
    ts = 34
    while ts > 20 and ImageDraw.Draw(Image.new("RGB", (1, 1))).textlength(tag, font=ImageFont.truetype(F_XB, ts)) > 980: ts -= 1
    f_tag = ImageFont.truetype(F_XB, ts)
    btn = cfg.get("botao", "COMENTE PRIME")
    sub = cfg.get("sub", "e receba todas as informações no direct")
    com = cfg.get("comentario", "PRIME")
    user = cfg.get("usuario", "você")
    selo = cfg.get("selo", "MESA PROPRIETÁRIA 5PI  •  ATÉ R$ 100 MIL")
    aviso = cfg.get("aviso", "Operar envolve risco. Resultados passados não garantem resultados futuros.")

    # véu da marca (estático): degradê semitransparente
    veil = Image.new("RGBA", (W, H))
    top, bot = np.array(_hex("#0a0f2e")), np.array(_hex("#1c0d45"))
    arr = np.zeros((H, W, 4), np.uint8)
    for y in range(H):
        k = y / H; col = top * (1 - k) + bot * k
        arr[y, :, :3] = col[:3]; arr[y, :, 3] = int(150 + 70 * k)
    veil = Image.fromarray(arr, "RGBA")

    # botão pré-renderizado (depois só escala)
    bw, bh = 860, 190
    btn_img = Image.new("RGBA", (bw + 80, bh + 80), (0, 0, 0, 0))
    glow = Image.new("RGBA", btn_img.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow).rounded_rectangle([40, 40, 40 + bw, 40 + bh], 95, fill=_hex(c2, 200))
    glow = glow.filter(ImageFilter.GaussianBlur(26))
    d = ImageDraw.Draw(btn_img)
    d.rounded_rectangle([40, 40, 40 + bw, 40 + bh], 95, fill=_hex(c2))
    tw = d.textlength(btn, font=f_btn)
    d.text((40 + (bw - tw) / 2, 40 + bh / 2), btn, font=f_btn, fill=navy, anchor="lm")

    def frame(t):
        im = veil.copy(); dr = ImageDraw.Draw(im)
        # logo descendo
        a = _ease_out(t / 0.45); y = 150 + int(-220 * (1 - a))
        w1 = dr.textlength(m1 + " ", font=f_logo); w2 = dr.textlength(m2, font=f_logo)
        x0 = (W - w1 - w2) / 2
        dr.text((x0 + 5, y + 6), m1, font=f_logo, fill=(0, 0, 0, int(120 * a)))
        dr.text((x0 + w1 + 5, y + 6), m2, font=f_logo, fill=(0, 0, 0, int(120 * a)))
        dr.text((x0, y), m1, font=f_logo, fill=_hex(c1, int(255 * a)))
        dr.text((x0 + w1, y), m2, font=f_logo, fill=_hex(c2, int(255 * a)))
        a = _ease_out((t - 0.3) / 0.4)
        dr.text((W / 2, 425), tag, font=f_tag, fill=(230, 232, 255, int(230 * a)), anchor="mm")
        # botão com pop + pulso + brilho
        if t > 0.55:
            s = _pop((t - 0.55) / 0.45) * (1 + 0.045 * math.sin(2 * math.pi * 1.3 * t))
            g = glow.copy(); g.putalpha(g.getchannel("A").point(lambda v: int(v * (0.55 + 0.45 * abs(math.sin(math.pi * 1.3 * t))))))
            layer = Image.alpha_composite(g, btn_img)
            nw, nh = int(layer.width * s), int(layer.height * s)
            layer = layer.resize((nw, nh), Image.LANCZOS)
            im.alpha_composite(layer, (int(W / 2 - nw / 2), int(610 - nh / 2)))
        a = _ease_out((t - 0.9) / 0.4)
        dr = ImageDraw.Draw(im)
        dr.text((W / 2, 770), sub, font=f_sub, fill=(255, 255, 255, int(255 * a)), anchor="mm")
        # cartão de comentário simulado
        if t > 1.2:
            a = _ease_out((t - 1.2) / 0.35); yy = 880 + int(60 * (1 - a))
            card = Image.new("RGBA", (W, H), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
            cd.rounded_rectangle([110, yy, 970, yy + 170], 36, fill=(255, 255, 255, int(240 * a)))
            cd.ellipse([140, yy + 35, 240, yy + 135], fill=_hex(c1, int(255 * a)))
            cd.ellipse([150, yy + 45, 230, yy + 125], fill=_hex("#1c0d45", int(255 * a)))
            cd.text((190, yy + 85), "EU", font=f_av, fill=_hex(c2, int(255 * a)), anchor="mm")
            cd.text((270, yy + 40), user, font=f_user, fill=(90, 90, 110, int(255 * a)))
            n = int(max(0, (t - 1.55)) * 7)
            txt = com[:n]
            cd.text((270, yy + 82), txt, font=f_com, fill=(15, 15, 30, int(255 * a)))
            if n < len(com) and int(t * 3) % 2 == 0:
                cx = 270 + cd.textlength(txt, font=f_com) + 4
                cd.rectangle([cx, yy + 88, cx + 5, yy + 140], fill=(15, 15, 30, int(255 * a)))
            # coração
            tl = 1.55 + len(com) / 7 + 0.25
            hs = 1.0 if t < tl else _pop((t - tl) / 0.35)
            hc = (200, 200, 210, int(255 * a)) if t < tl else (255, 48, 88, 255)
            hx, hy, r = 905, yy + 85, 22 * hs
            cd.ellipse([hx - r, hy - r * 0.9, hx, hy + r * 0.1], fill=hc)
            cd.ellipse([hx, hy - r * 0.9, hx + r, hy + r * 0.1], fill=hc)
            cd.polygon([(hx - r * 0.98, hy - r * 0.2), (hx + r * 0.98, hy - r * 0.2), (hx, hy + r * 1.1)], fill=hc)
            im.alpha_composite(card)
        dr = ImageDraw.Draw(im)
        # setas pulando
        if t > 1.4:
            a = _ease_out((t - 1.4) / 0.3); off = 14 * math.sin(2 * math.pi * 1.6 * t)
            for i, yy in enumerate((1100, 1150)):
                col = _hex(c1, int(255 * a * (1 if i else 0.6)))
                y0 = yy + off
                dr.line([(W / 2 - 50, y0), (W / 2, y0 + 38), (W / 2 + 50, y0)], fill=col, width=12, joint="curve")
        # selo 5PI
        if t > 1.0:
            a = _ease_out((t - 1.0) / 0.5); x = int(-900 * (1 - a))
            tw = dr.textlength(selo, font=f_chip); pw = tw + 80
            x0 = (W - pw) / 2 + x
            dr.rounded_rectangle([x0, 1265, x0 + pw, 1345], 40, fill=(10, 15, 46, 210), outline=_hex(c2), width=4)
            dr.text((x0 + pw / 2, 1305), selo, font=f_chip, fill=_hex(c2), anchor="mm")
        f_av2 = ImageFont.truetype(F_SB, 23)
        dr.text((W / 2, 1880), aviso, font=f_av2, fill=(190, 190, 215, 230), anchor="mm")
        return im

    off = str(cfg.get("clip_offset", 1.0))
    p = sp.Popen(["ffmpeg", "-y", "-loglevel", "error", "-stream_loop", "-1", "-ss", off, "-i", bg_clip,
                  "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                  "-filter_complex",
                  f"[0:v]fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},eq=saturation=1.1[bg];"
                  "[bg][1:v]overlay=0:0:shortest=1,format=yuv420p[v]",
                  "-map", "[v]", "-an", "-t", str(dur), "-r", str(FPS), "-c:v", "libx264", "-crf", "20", out],
                 stdin=sp.PIPE)
    for i in range(int(math.ceil(dur * FPS)) + 2):
        p.stdin.write(frame(i / FPS).tobytes())
    p.stdin.close(); p.wait()
    if p.returncode: raise SystemExit("ERRO ao gerar cartão final animado")


if __name__ == "__main__":
    import sys
    render(sys.argv[1], float(sys.argv[2]), sys.argv[3])
