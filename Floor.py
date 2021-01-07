import pygame
import random
from Settings import *

test_floor = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]
floor1 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 4],
    [4, 1, 1, 2, 2, 2, 0, 3, 0, 0, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 4],
    [4, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]  # Карта

floor2 = [

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта
floor3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта

floor4 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 2, 1, 2, 1, 2, 2, 1, 0, 4],
    [4, 0, 2, 0, 1, 0, 1, 1, 2, 1, 4, 4],
    [4, 0, 1, 0, 2, 0, 1, 2, 3, 2, 0, 4],
    [4, 0, 2, 1, 1, 1, 2, 1, 2, 1, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor5 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 3, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor6 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 4],
    [4, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 4],
    [4, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 4],
    [4, 1, 0, 1, 2, 0, 2, 0, 0, 0, 0, 4],
    [4, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 4],
    [4, 1, 0, 1, 0, 0, 0, 2, 3, 2, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor7 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 3, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor8 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),
     random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), 2, 4],
    [4, random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),
     random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), 4],
    [4, random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),
     random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), 4],
    [4, random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),
     random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), 3, 4],
    [4, random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),
     random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), 4],
    [4, random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),
     random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor9 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 4],
    [4, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 4],
    [4, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor10 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 4],
    [4, 0, 2, 3, 2, 0, 0, 2, 0, 0, 2, 4],
    [4, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 4],
    [4, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 4],
    [4, 0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

wall_coords = []
wall_collise = []
wall_texture = {}
width, height = SIZE
for numi, distance in enumerate(floor10):
    for numj, j in enumerate(distance):
        if j == 1:
            wall_texture[(WALL * numj, WALL * numi)] = '1'
            wall_coords.append((WALL * numj, WALL * numi))
            wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
        elif j == 2:
            wall_texture[(WALL * numj, WALL * numi)] = '2'
            wall_coords.append((WALL * numj, WALL * numi))
            wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
        elif j == 3:
            wall_texture[(WALL * numj, WALL * numi)] = '3'
            wall_coords.append((WALL * numj, WALL * numi))
            wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
            ruby_block = (numj * WALL, numi * WALL)
        elif j == 4:
            wall_texture[(WALL * numj, WALL * numi)] = '4'
            wall_coords.append((WALL * numj, WALL * numi))
            wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
print(wall_collise)


def render(screen):  # Рисование карты
    for numi, i in enumerate(floor10):
        for numj, j in enumerate(i):
            if j == 1:
                pygame.draw.rect(screen, COLOR_GREEN,
                                 (WALL * numj, WALL * numi, WALL, WALL), 1)
            if j == 0:
                pygame.draw.rect(screen, COLOR_BLUE,
                                 (WALL * numj, WALL * numi, WALL, WALL), 1)
