#!/usr/bin/env python3
"""
Extracts a single clean front-facing frame from each sprite sheet.
Sprite sheets are 4 columns x 7 rows (28 frames).
Each frame is sheet_width/4 x sheet_height/7 pixels.
We take row 0 (front-facing), col 0 for a clean static pose.
Then upscale 4x with nearest-neighbor to keep pixel-art crisp.
"""
from PIL import Image
import os

ASSETS = os.path.dirname(os.path.abspath(__file__))

sprites = {
    "player_front.png": "sprite_sheet_player2.png",  # dark thief player
    "guard_front.png": "sprite_sheet_guard1.png",     # red guard (best contrast)
}

for output_name, sheet_name in sprites.items():
    sheet_path = os.path.join(ASSETS, sheet_name)
    img = Image.open(sheet_path)
    
    cols = 4
    rows = 7
    fw = img.width // cols
    fh = img.height // rows
    
    # Row 0, Col 0 = front-facing idle
    frame = img.crop((0, 0, fw, fh))
    
    # Upscale 6x with nearest-neighbor for crisp pixel art
    scale = 6
    frame = frame.resize((fw * scale, fh * scale), Image.NEAREST)
    
    out_path = os.path.join(ASSETS, output_name)
    frame.save(out_path)
    print(f"Saved {output_name} ({fw*scale}x{fh*scale}px)")

print("Done!")
