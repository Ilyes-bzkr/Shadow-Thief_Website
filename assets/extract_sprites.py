from PIL import Image
import os
ASSETS = os.path.dirname(os.path.abspath(__file__))
img = Image.open(os.path.join(ASSETS, 'sprite_sheet_player.png'))
fw, fh = img.width // 4, img.height // 7
frame = img.crop((0, 0, fw, fh))
frame = frame.resize((fw * 6, fh * 6), Image.NEAREST)
frame.save(os.path.join(ASSETS, 'player_front.png'))
print(f'Saved player_front.png ({fw*6}x{fh*6}px)')
