import math
from Player import *
from Settings import *

player = Player()


def delta_wall_y(sin, cos):
    xp, yp = player.player_pos()
    xw, yw = player.coord_player()
    if sin >= 0:
        delta_y = (yp - ((yw + 1) * 100)) / (sin + 0.00001)
        delta_y = int(abs(delta_y))
    else:
        delta_y = (yp - (yw * 100)) / (sin + 0.00001)
        delta_y = int(abs(delta_y))
    if cos >= 0:
        delta_x = (xp - ((xw + 1) * 100)) / (cos + 0.00001)
        delta_x = int(abs(delta_x))
    else:
        delta_x = (xp - (xw * 100)) / (cos + 0.00001)
        delta_x = int(abs(delta_x))
    return min(delta_x, delta_y)


def raycast(screen):
    screen.fill((0, 0, 0))
    cos, sin = player.cos_sin_player()
    x, y = player.player_pos()

    pygame.draw.circle(screen, (255, 0, 0), [x, y], 10)
    # pygame.draw.aaline(screen, (255, 0, 0), [x, y],
    #                   [x + RENDER_DISTANCE * cos, y + RENDER_DISTANCE * sin])  # Рисование основного луча
    current_angle = player.angle
    for ray in range(RAY_NUMBER // 2):  # Рисование дополнительных луча
        n_rad = current_angle * math.pi / 180
        cos = math.cos(n_rad)
        sin = math.sin(n_rad)
        pygame.draw.aaline(screen, COLOR_GREEN, [x, y],
                           [x + delta_wall_y(sin, cos) * cos, y + delta_wall_y(sin, cos) * sin])
        current_angle += DELTA_ANGLE
    current_angle = player.angle - DELTA_ANGLE
    delta_wall_y(sin, cos)
    for ray in range(RAY_NUMBER // 2 - 1):
        n_rad = current_angle * math.pi / 180
        cos = math.cos(n_rad)
        sin = math.sin(n_rad)
        pygame.draw.aaline(screen, COLOR_GREEN, [x, y],
                           [x + delta_wall_y(sin, cos) * cos, y + delta_wall_y(sin, cos) * sin])
        current_angle -= DELTA_ANGLE
