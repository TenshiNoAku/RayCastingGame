import pygame
import math
from Settings import *
from Player import *
from Floor import *
from RayCasting import *
from Render import *

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
        player.movement()

        render.background()
        render.world(player.player_pos(), player.angle)
        render.mini_map(player)
        clock.tick(60)  # Установка ограничения FPS
        pygame.display.flip()
        print(clock.get_fps())
    pygame.quit()
