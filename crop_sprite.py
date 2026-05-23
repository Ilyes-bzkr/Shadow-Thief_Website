import sys
try:
    from PIL import Image
    sheet = Image.open('assets/sprite_sheet_player2.png')
    w, h = sheet.size
    # Assuming the sprites are square (w = n * h)
    sprite_size = h
    if sprite_size == 0: sprite_size = 32
    sprite = sheet.crop((0, 0, sprite_size, sprite_size))
    sprite.save('assets/isolated_player.png')
    print("PIL: Cropped player sprite")

    sheet_guard = Image.open('assets/sprite_sheet_guard.png')
    wg, hg = sheet_guard.size
    sprite_size_g = hg
    sprite_g = sheet_guard.crop((0, 0, sprite_size_g, sprite_size_g))
    sprite_g.save('assets/isolated_guard.png')
    print("PIL: Cropped guard sprite")

except ImportError:
    try:
        import pygame
        pygame.init()
        pygame.display.set_mode((1, 1), pygame.NOFRAME)
        
        sheet = pygame.image.load('assets/sprite_sheet_player2.png')
        h = sheet.get_height()
        sprite = pygame.Surface((h, h), pygame.SRCALPHA)
        sprite.blit(sheet, (0, 0), (0, 0, h, h))
        pygame.image.save(sprite, 'assets/isolated_player.png')
        print("Pygame: Cropped player sprite")

        sheet_g = pygame.image.load('assets/sprite_sheet_guard.png')
        hg = sheet_g.get_height()
        sprite_g = pygame.Surface((hg, hg), pygame.SRCALPHA)
        sprite_g.blit(sheet_g, (0, 0), (0, 0, hg, hg))
        pygame.image.save(sprite_g, 'assets/isolated_guard.png')
        print("Pygame: Cropped guard sprite")
    except Exception as e:
        print(f"Error: {e}")
