import pygame
import math
from Settings import *
from Player import *
from Floor import *
from RayCasting import *

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    running = True
    start_pos_player = [400, 300]
    grad_pos_player = 0
    clock = pygame.time.Clock()
    while running:
        raycast(screen)
        render(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.movement()
        clock.tick(FPS)  # Установка ограничения FPS
        pygame.display.flip()
    pygame.quit()
