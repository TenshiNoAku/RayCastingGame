import pygame
import math
from Settings import *
from Player import *
from Floor import *
from RayCasting import *
from Render import *
from Sprite_render import *
mixer = pygame.mixer
mixer.init()
mixer.music.load('Data/Music/music1.mp3')
mixer.music.set_volume(0.05)
mixer.music.play()
if __name__ == '__main__':
    pygame.init()
    screen2 = pygame.display.set_mode(SIZE)
    screen = pygame.Surface(SIZE)
    running = True
    sprites = Sprites()
    clock = pygame.time.Clock()
    player = Player()
    screen_map = pygame.Surface((SIZE[0] // 5, SIZE[1] // 5))
    render = Render(screen, screen_map, screen2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.movement()

        render.background()
        walls = raycast(player, render.texturs)
        render.world(walls + [obj.object_locate(player, walls)  for obj in sprites.list_sprites])
        render.mini_map(player)
        clock.tick(600)  # Установка ограничения FPS
        pygame.display.flip()
        screen2.fill(COLOR_DARKSLATEGRAY)
        screen2.blit(screen, (0, 0 + float(player.z_player())))
        print(clock.get_fps())
    pygame.quit()
