#!/usr/bin/env python3
"""
Re-extract guard from the correct sprite sheet (sprite_sheet_guard.png = blue guard).
"""
from PIL import Image
import os

ASSETS = os.path.dirname(os.path.abspath(__file__))

sheet_path = os.path.join(ASSETS, "sprite_sheet_guard.png")
img = Image.open(sheet_path)

cols = 4
rows = 7
fw = img.width // cols
fh = img.height // rows

# Row 0, Col 0 = front-facing idle
frame = img.crop((0, 0, fw, fh))

# Upscale 6x nearest-neighbor
scale = 6
frame = frame.resize((fw * scale, fh * scale), Image.NEAREST)

out_path = os.path.join(ASSETS, "guard_front.png")
frame.save(out_path)
print(f"Saved guard_front.png ({fw*scale}x{fh*scale}px)")
