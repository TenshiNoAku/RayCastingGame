import pygame
import math
from Settings import *
from Player import *
from Floor import *
from RayCasting import *
from Render import Drawing
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    running = True
    clock = pygame.time.Clock()
    player = Player()
    screen_map = pygame.Surface((SIZE[0] // 5, SIZE[1] // 5))
    drawing = Drawing(screen,screen_map)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.movement()

        drawing.background()
        drawing.world(player.player_pos(), player.angle)
        drawing.mini_map(player)
        clock.tick(FPS)  # Установка ограничения FPS
        pygame.display.flip()
    pygame.quit()
