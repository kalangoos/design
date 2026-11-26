"""Kalango Train marketing variants, with the same geometry as the Cast ones in marca/apps (measured from those files):
- horizontal: logo 1024 -> 200x200 at (0,0); text in URW Gothic Demi 72 px drawn at (224, 68); width = ceil(224 + advance) + 8; height 200;
  light text #E2E2E6 for dark backgrounds, Roxo #322153 for light ones; transparent.
- sobre fundo: 1040x840 card, corner radius 16 (8x supersampled), #16171B or #F0F0F5, logo 800x800 at (100, 20).
- 512/: LANCZOS copy of the logo.
Usage: compose.py <logo.png> <out-dir> <slug> <title>"""
import math, os, sys
from PIL import Image, ImageDraw, ImageFont

src, out, slug, title = sys.argv[1:5]
logo = Image.open(src).convert("RGBA")
font = ImageFont.truetype("/usr/share/fonts/opentype/urw-base35/URWGothic-Demi.otf", 72)
TX, TY = 224, 68
width = math.ceil(TX + font.getlength(title)) + 8

for suffix, colour in [("fundo-escuro", (0xE2, 0xE2, 0xE6, 255)), ("fundo-claro", (0x32, 0x21, 0x53, 255))]:
    im = Image.new("RGBA", (width, 200), (0, 0, 0, 0))
    im.alpha_composite(logo.resize((200, 200), Image.LANCZOS), (0, 0))
    ImageDraw.Draw(im).text((TX, TY), title, font=font, fill=colour)
    p = f"{out}/{slug}-horizontal-{suffix}.png"; im.save(p, optimize=True); print(p, im.size)

ss = 8
mask = Image.new("L", (1040 * ss, 840 * ss), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, 1040 * ss - 1, 840 * ss - 1), radius=16 * ss, fill=255)
mask = mask.resize((1040, 840), Image.BOX)
big = logo.resize((800, 800), Image.LANCZOS)
for suffix, bg in [("sobre-fundo-escuro", (0x16, 0x17, 0x1B)), ("sobre-fundo-claro", (0xF0, 0xF0, 0xF5))]:
    card = Image.new("RGBA", (1040, 840), (*bg, 255))
    card.alpha_composite(big, (100, 20))
    card.putalpha(mask)
    p = f"{out}/{slug}-{suffix}.png"; card.save(p, optimize=True); print(p, card.size)

os.makedirs(f"{out}/512", exist_ok=True)
logo.resize((512, 512), Image.LANCZOS).save(f"{out}/512/{slug}.png", optimize=True); print(f"{out}/512/{slug}.png")
