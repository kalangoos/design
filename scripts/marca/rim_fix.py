"""Close the 1-px lavender seam at the silhouette of a vtracer 'stacked' SVG whose bottom layer is not the outline colour:
trace the silhouette (alpha mask of the snapped raster) with vtracer in binary mode and draw it last as a thin charcoal stroke.
Usage: rim_fix.py <snapped.png> <icon.svg>"""
import re, subprocess, sys, os
import numpy as np
from PIL import Image

flat, svg = sys.argv[1:3]
VT = os.path.expanduser("~/.cargo/bin/vtracer")
a = np.asarray(Image.open(flat).convert("RGBA"))[..., 3] > 0
mask = Image.fromarray(np.where(a, 0, 255).astype(np.uint8), "L").convert("RGB")
tmp_in = flat[:-4] + "-mask.png"; tmp_out = flat[:-4] + "-mask.svg"
mask.save(tmp_in)
subprocess.run([VT, "--input", tmp_in, "--output", tmp_out, "--colormode", "binary", "--mode", "spline", "--filter_speckle", "10",
                "--corner_threshold", "60", "--segment_length", "4", "--splice_threshold", "45", "--path_precision", "1"], check=True, stdout=subprocess.DEVNULL)
m = open(tmp_out).read()
paths = []
for tag in re.findall(r"<path [^>]*/>", m):
    if 'fill="#000000"' not in tag:          # keep the black silhouette, not the white page
        continue
    d = re.search(r'd="([^"]*)"', tag).group(1)
    t = re.search(r'transform="([^"]*)"', tag)
    paths.append((d, t.group(1) if t else ""))
rim = "".join(f'<path d="{d}" fill="none" stroke="#16171B" stroke-width="2" stroke-linejoin="round"' + (f' transform="{t}"' if t else "") + "/>\n" for d, t in paths)
s = open(svg).read()
s = s.replace("</svg>", rim + "</svg>")
open(svg, "w").write(s)
print(f"rim: {len(paths)} path(s) added; svg {os.path.getsize(svg) // 1024} KB")
