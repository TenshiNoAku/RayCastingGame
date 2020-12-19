import pygame
from Settings import *
from Floor import wall_coords


def mapping(a, b):
    return (a // WALL) * WALL, (b // WALL) * WALL


def raycast(sc, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(RAY_NUMBER):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + WALL, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, SIZE[0], WALL):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in wall_coords:
                break
            x += dx * WALL

        # horizontals
        y, dy = (ym + WALL, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, SIZE[1], WALL):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in wall_coords:
                break
            y += dy * WALL

        # projection
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        depth += 1
        proj_height = min(int(PROJ_COEFF / depth),2 * SIZE[1])
        c = 255 / (1 + depth * depth * 0.00002)
        color = (c//3, c, c // 3)
        pygame.draw.rect(sc, color, (ray * SCALE, SIZE[1] // 2 - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE
