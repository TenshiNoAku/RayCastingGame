import pygame
# from numba import njit
import math
from Settings import *


# @njit(fastmath=True)
def mapping(a, b):
    return (a // WALL) * WALL, (b // WALL) * WALL


# @njit(fastmath=True)
def sin_cos(cur_angle):
    sin_a = math.sin(cur_angle)
    cos_a = math.cos(cur_angle)
    sin_a = sin_a if sin_a else 0.000001
    cos_a = cos_a if cos_a else 0.000001
    return sin_a, cos_a


# @njit(fastmath=True)
def projection(player_angle, cur_angle, depth, offset):
    offset = int(offset) % WALL
    depth *= math.cos(player_angle - cur_angle)
    depth += 1
    proj_height = min(int(PROJ_COEFF / depth), int(SIZE[1] * 2))
    return offset, proj_height


# @njit(fastmath=True)
def depth_h_poisk(y, oy, ox, sin_a, cos_a):
    depth_h = (y - oy) / sin_a
    xh = ox + depth_h * cos_a
    return xh, depth_h


# @njit(fastmath=True)
def depth_v_poisk(x, oy, ox, sin_a, cos_a):
    depth_v = (x - ox) / cos_a
    yv = oy + depth_v * sin_a
    return yv, depth_v


def dele(ray, x, y):
    if ray == 150:
        return (x, y)


def raycast(sc, player_pos, player_angle, texturs, floor):
    global yv, xh, depth_h, depth_v, texture_v, texture_h, a, destruction_v, destruction_h
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
            checkout, index = floor.checkout_block(wall_v)
            if checkout:
                texture_v = floor.walls[index].texture
                destruction_v = floor.walls[index].level_of_destruction
                break
            x += dx * WALL
        if ray == 149:
            block_v = wall_v

        # horizontals
        y, dy = (ym + WALL, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, SIZE[1], WALL):
            xh, depth_h = depth_h_poisk(y, oy, ox, sin_a, cos_a)
            wall_h = mapping(xh, y + dy)
            checkout, index = floor.checkout_block(wall_h)
            if checkout:
                texture_h = floor.walls[index].texture
                destruction_h = floor.walls[index].level_of_destruction
                break
            y += dy * WALL

        if ray == 149:
            block_h = wall_h
        # projection
        depth, offset, texture_wall, destruction = (depth_v, yv, texture_v, destruction_v) if depth_v < depth_h else (depth_h, xh, texture_h, destruction_h)
        offset, proj_height = projection(player_angle, cur_angle, depth, offset)

        wall_column = texturs[texture_wall].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, (SIZE[1] - proj_height) // 2))
        if destruction and destruction < 6:
            wall_column = texturs[f'fracture_{destruction}'].subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
            wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
            sc.blit(wall_column, (ray * SCALE, (SIZE[1] - proj_height) // 2))
        cur_angle += DELTA_ANGLE
    return block_v, block_h
