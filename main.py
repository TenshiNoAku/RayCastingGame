import pygame
import math
from Settings import *
from Player import *
from Floor import *
from RayCasting import *
from Render import *

mixer = pygame.mixer
mixer.init()
mixer.music.load('Data/Music/music1.mp3')
mixer.music.set_volume(0.05)
mixer.music.play()
counter = 0
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    running = True
    clock = pygame.time.Clock()
    player = Player()
    screen_map = pygame.Surface((SIZE[0] // 5, SIZE[1] // 5))
    render = Render(screen, screen_map)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    counter = player.destroy_block(block,counter)
                if ruby_block not in wall_coords:
                    print(f'Вы победили,потратив на это {counter} действий')
                    running=False

        player.movement()
        render.background()
        block_v, block_h = render.world(player.player_pos(), player.angle)
        block = player.block_check(block_v, block_h)
        render.mini_map(player)
        clock.tick(600)  # Установка ограничения FPS
        pygame.display.flip()
    pygame.quit()
