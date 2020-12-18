import math
from Player import *
from Settings import *
from Floor import *
player = Player()


def delta_wall_y(sin, cos):
    xp, yp = player.player_pos()
    xw, yw = player.coord_player()
    if sin >= 0:
        delta_y = (yp - ((yw + 1) * WALL)) / (sin + 0.00001)
        delta_y = int(abs(delta_y))
    else:
        delta_y = (yp - (yw * WALL)) / (sin + 0.00001)
        delta_y = int(abs(delta_y))
    if cos >= 0:
        delta_x = (xp - ((xw + 1) * WALL)) / (cos + 0.00001)
        delta_x = int(abs(delta_x))
    else:
        delta_x = (xp - (xw * WALL)) / (cos + 0.00001)
        delta_x = int(abs(delta_x))
    return min(delta_x, delta_y)


def raycast(screen):
    screen.fill((0, 0, 0))
    x, y = player.player_pos()

    pygame.draw.circle(screen, (255, 0, 0), [x, y], 10)
    current_angle = player.angle - (DELTA_ANGLE * (RAY_NUMBER // 2))
    for ray in range(RAY_NUMBER):  # Рисование дополнительных луча
        n_rad = current_angle * math.pi / 180
        cos = math.cos(n_rad)
        sin = math.sin(n_rad)
        cos1 = -cos
        sin1 = -sin
        xp, yp = x + delta_wall_y(sin, cos) * cos, y + delta_wall_y(sin, cos) * sin
        xp1, yp1 = x + delta_wall_y(sin1, cos1) * cos1, y + delta_wall_y(sin1, cos1) * sin1
        del_dist = ((xp - xp1) ** 2 + (yp - yp1) ** 2) ** 0.5+ 1
        dist = ((xp - x) ** 2 + (yp - y) ** 2) ** 0.5
        for i in range(RENDER_DISTANCE // int(del_dist)):
            dist += del_dist
            if ((int(x + dist * cos) + 1) // 100 * 100,(int(y + dist * sin) + 1) // 100 * 100) in wall_coords:
                break
        pygame.draw.aaline(screen, COLOR_GREEN, [x, y],
                           [int(x+dist*cos), int(y+dist*sin)])
        print(xp - xp1, yp - yp1)
        current_angle += DELTA_ANGLE
