import math
from Player import *
from Settings import *
from Floor import *

player = Player()


def raycast(screen):
    global distance, distance_to_vertikal
    screen.fill((0, 0, 0))
    cos, sin = player.cos_sin_player()
    x, y = player.player_pos()

    pygame.draw.circle(screen, (255, 0, 0), [int(x), int(y)], 10)
    pygame.draw.aaline(screen, (255, 0, 0), [x, y],
                       [x + RENDER_DISTANCE * cos, y + RENDER_DISTANCE * sin])  # Рисование основного луча
    current_angle = player.angle + DELTA_ANGLE
    for ray in range(RAY_NUMBER // 2 - 1):  # Рисование дополнительных луча
        n_rad = current_angle * math.pi / 180
        cos = math.cos(n_rad)
        sin = math.sin(n_rad)
        px = x // 100 * 100
        if cos >= 0:
            px += 100
            dx = 1
        else:
            dx = -1
        distance_to_vertikal = (px - x) / cos

        for distance in range(0, RENDER_DISTANCE, 100):
            print(((x + (distance_to_vertikal + distance) * cos) // 100 * 100, (y + (distance_to_vertikal + distance) * sin) // 100 * 100))
            if ((x + (distance_to_vertikal + distance) * cos) // 100 * 100, (y + (distance_to_vertikal + distance) * sin) // 100 * 100) in wall_coords:
                print('столкновение')
                break
        pygame.draw.aaline(screen, COLOR_GREEN, [x, y],
                           [x + (distance_to_vertikal + distance) * cos, y + (distance_to_vertikal + distance) * sin])
        current_angle += DELTA_ANGLE
    current_angle = player.angle - DELTA_ANGLE
    # for ray in range(RAY_NUMBER // 2 - 1):
    #     n_rad = current_angle * math.pi / 180
    #     cos = math.cos(n_rad)
    #     sin = math.sin(n_rad)
    #     current_distance = (x + RENDER_DISTANCE * cos) % 100
    #     for distance in range(0, RENDER_DISTANCE, 100):
    #         if ((x + distance * cos) // 100 * 100, ((y + distance * sin) // 100 * 100)) in wall_coords:
    #             break
    #     pygame.draw.aaline(screen, COLOR_GREEN, [x, y],
    #                        [x + (current_distance + distance) * cos, y + (current_distance + distance) * sin])
    #     current_angle -= DELTA_ANGLE
