import math
from Player import *
from Settings import *

player = Player()


def raycast(screen):
    screen.fill((0, 0, 0))
    cos, sin = player.cos_sin_player()
    x, y = player.player_pos()

    pygame.draw.circle(screen, (255, 0, 0), [x, y], 10)
    pygame.draw.aaline(screen, (255, 0, 0), [x, y],
                       [x + RENDER_DISTANCE * cos, y + RENDER_DISTANCE * sin])
    current_angle = player.angle + DELTA_ANGLE
    for ray in range(RAY_NUMBER // 2 - 1):
        n_rad = current_angle * math.pi / 180
        cos = math.cos(n_rad)
        sin = math.sin(n_rad)
        pygame.draw.aaline(screen, COLOR_GREEN, [x, y],
                           [x + RENDER_DISTANCE * cos, y + RENDER_DISTANCE * sin])
        current_angle += DELTA_ANGLE
    current_angle = player.angle - DELTA_ANGLE
    for ray in range(RAY_NUMBER // 2 - 1):
        n_rad = current_angle * math.pi / 180
        cos = math.cos(n_rad)
        sin = math.sin(n_rad)
        pygame.draw.aaline(screen, COLOR_GREEN, [x, y],
                           [x + RENDER_DISTANCE * cos, y + RENDER_DISTANCE * sin])
        current_angle -= DELTA_ANGLE
