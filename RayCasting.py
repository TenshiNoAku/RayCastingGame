import pygame
from numba import njit

from Floor import *
from Settings import *


@njit(fastmath=True)
def mapping(a, b):
    return (a // WALL) * WALL, (b // WALL) * WALL


@njit(fastmath=True)
def sin_cos(cur_angle):
    sin_a = math.sin(cur_angle)
    cos_a = math.cos(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = cos_a if cos_a else 0.000001
    return sin_a, cos_a


@njit(fastmath=True)
def projection(player_angle, cur_angle, depth, offset):
    offset = int(offset) % WALL
    depth *= math.cos(player_angle - cur_angle)
    depth += 1
    proj_height = min(int(PROJ_COEFF / depth), int(SIZE[1] * 2))
    return offset, proj_height

@njit(fastmath=True)
def depth_h_poisk(y, oy, ox, sin_a, cos_a):
    depth_h = (y - oy) / sin_a
    xh = ox + depth_h * cos_a
    return xh, depth_h

@njit(fastmath=True)
def depth_v_poisk(x, oy, ox, sin_a, cos_a):
    depth_v = (x - ox) / cos_a
    yv = oy + depth_v * sin_a
    return yv, depth_v


def raycast(sc, player_pos, player_angle, texturs):
    global yv, xh, depth_h, depth_v, texture_v, texture_h
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(RAY_NUMBER):
        sin_a, cos_a = sin_cos(cur_angle)

        # verticals
        x, dx = (xm + WALL, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, SIZE[0], WALL):
            yv, depth_v = depth_v_poisk(x, oy, ox, sin_a, cos_a)
            wall_v = mapping(x + dx, yv)
            if wall_v in wall_coords:
                texture_v = wall_texture[wall_v]
                break
            x += dx * WALL

        # horizontals
        y, dy = (ym + WALL, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, SIZE[1], WALL):
            xh, depth_h = depth_h_poisk(y, oy, ox, sin_a, cos_a)
            wall_h = mapping(xh, y + dy)
            if wall_h in wall_coords:
                texture_h = wall_texture[wall_h]
                break
            y += dy * WALL

        # projection
        depth, offset, texture_wall = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
        offset, proj_height = projection(player_angle, cur_angle, depth, offset)

        wall_column = texturs[texture_wall].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, (SIZE[1] - proj_height) // 2))
        # c = 120 / (1 + depth * depth * 0.00002)
        # color = (c, c//2, c // 4)
        # pygame.draw.rect(sc, color, (ray * SCALE, SIZE[1] // 2 - proj_height // 2, SCALE, proj_height))

        cur_angle += DELTA_ANGLE
