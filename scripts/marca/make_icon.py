"""Kalango Train app icon, made the same way as the other 19 icons in icones/:
fonte (raw Higgsfield PNG) -> trim + 4% pad, square -> 512 and 128 PNG (LANCZOS) -> palette snap -> vtracer CLI -> SVG.
Usage: make_icon.py <raw.png> <hf-job-id> <design-worktree> <name>"""
import os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageFilter
from PIL.PngImagePlugin import PngInfo

raw, job, W, name = sys.argv[1:5]
IC = os.path.join(W, "icones")
VT = os.path.expanduser("~/.cargo/bin/vtracer")
TMP = os.path.join(os.path.dirname(os.path.abspath(__file__)), "trace_tmp"); os.makedirs(TMP, exist_ok=True)
DARK = ["#A5A1E2", "#8ED2C3", "#7CC3DF", "#F1DDB0", "#E5C98C", "#EFA2A6", "#16171B"]

# 1. source, tagged with its Higgsfield job like the other fonte/*.png
src = Image.open(raw)
meta = PngInfo(); meta.add_text("hf-job-id", job)
src.save(f"{IC}/fonte/{name}.png", pnginfo=meta)

# 2. trim to the drawing, 4% margin, square; 512 and 128 PNGs
def trim(im, pad=0.04):
    im = im.convert("RGBA"); a = im.getchannel("A").point(lambda v: 255 if v > 8 else 0)
    im = im.crop(a.getbbox()); w, h = im.size; p = round(max(w, h) * pad); s = max(w, h) + 2 * p
    out = Image.new("RGBA", (s, s), (0, 0, 0, 0)); out.alpha_composite(im, ((s - w) // 2, (s - h) // 2)); return out
im = trim(Image.open(raw))
im.resize((512, 512), Image.LANCZOS).save(f"{IC}/{name}.png", optimize=True)
im.resize((128, 128), Image.LANCZOS).save(f"{IC}/128/{name}.png", optimize=True)

# 3. snap to the design-system palette (plus real extra cel tones), clean 1-2 px fringes
rgb = lambda h: np.array([int(h[i:i + 2], 16) for i in (1, 3, 5)], dtype=np.float32)
hexs = lambda c: "#%02X%02X%02X" % tuple(int(round(v)) for v in c)
def palette_for(im, base, n):
    a = np.asarray(im)
    opaque = a[a[..., 3] > 200][:, :3]
    sample = Image.fromarray(opaque[:: max(1, len(opaque) // 400000)].reshape(-1, 1, 3), "RGB")
    q = sample.quantize(colors=n, method=Image.Quantize.MEDIANCUT)
    pal = np.array(q.getpalette()[: n * 3], dtype=np.float32).reshape(-1, 3)
    cnt = np.bincount(np.asarray(q).ravel(), minlength=n)
    out = [rgb(h) for h in base]
    for c, k_ in sorted(zip(pal, cnt), key=lambda t: -t[1]):
        if k_ < 0.004 * cnt.sum():
            continue
        if min(np.linalg.norm(c - o) for o in out) > 34:
            out.append(c)
    return out
def snap(im, pal):
    a = np.asarray(im).astype(np.float32)
    P = np.stack(pal)
    px = a[..., :3].reshape(-1, 3)
    idx = np.empty(len(px), dtype=np.uint8)
    for s in range(0, len(px), 1 << 20):
        d = ((px[s:s + (1 << 20), None, :] - P[None]) ** 2).sum(-1)
        idx[s:s + (1 << 20)] = d.argmin(1)
    idx = idx.reshape(a.shape[:2])
    alpha = a[..., 3] > 127
    lab = Image.fromarray(np.where(alpha, idx + 1, 0).astype(np.uint8), "L").filter(ImageFilter.ModeFilter(5))
    lab = np.asarray(lab)
    used = [i for i in range(len(pal)) if (lab == i + 1).sum() > 0.0006 * alpha.sum()]
    out = np.zeros((*lab.shape, 4), dtype=np.uint8)
    for i in range(len(pal)):
        m = lab == i + 1
        if not m.any():
            continue
        j = i if i in used else min(used, key=lambda u: np.linalg.norm(pal[u] - pal[i]))
        out[m] = (*[int(round(v)) for v in pal[j]], 255)
    return Image.fromarray(out, "RGBA"), [hexs(pal[i]) for i in used]

im512 = Image.open(f"{IC}/{name}.png").convert("RGBA")
flat, used = snap(im512, palette_for(im512, DARK, 14))
tmp = f"{TMP}/{name}.png"; flat.save(tmp)
out = f"{IC}/svg/{name}.svg"
subprocess.run([VT, "--input", tmp, "--output", out, "--colormode", "color", "--hierarchical", "stacked", "--mode", "spline", "--filter_speckle", "10",
                "--color_precision", "8", "--gradient_step", "1", "--corner_threshold", "60", "--segment_length", "4", "--splice_threshold", "45",
                "--path_precision", "1"], check=True, stdout=subprocess.DEVNULL)
s = open(out).read()
w, h = flat.size
s = re.sub(r"<svg[^>]*>", f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n<title>KalangoOS — {name.replace("kalango-", "")}</title>', s, count=1)
s = re.sub(r"<\?xml[^>]*\?>\s*", "", s); s = re.sub(r"<!--.*?-->\s*", "", s, flags=re.S)
open(out, "w").write(s)
fills = sorted(set(re.findall(r'fill="(#[0-9A-Fa-f]{6})"', s)))
print(f"{name}.svg  {os.path.getsize(out) // 1024} KB  {s.count('<path')} paths  colours: {' '.join(c.upper() for c in fills)}  (snapped: {' '.join(used)})")
