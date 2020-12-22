import pygame
from Settings import *
floor = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [1, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 4],
    [1, 1, 1, 2, 2, 2, 3, 3, 3, 0, 4, 4],
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта
floor2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0,1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта
floor3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0,1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта
wall_coords = []
wall_texture = {}
width, height = SIZE
for numi, distance in enumerate(floor):
    for numj, j in enumerate(distance):
        if j == 1:
            wall_texture[(WALL * numj, WALL * numi)] = '1'
            wall_coords.append((WALL * numj, WALL * numi))
        elif j == 2:
            wall_texture[(WALL * numj, WALL * numi)] = '2'
            wall_coords.append((WALL * numj, WALL * numi))
        elif j == 3:
            wall_texture[(WALL * numj, WALL * numi)] = '3'
            wall_coords.append((WALL * numj, WALL * numi))
        elif j == 4:
            wall_texture[(WALL * numj, WALL * numi)] = '4'
            wall_coords.append((WALL * numj, WALL * numi))
print(wall_coords)
def render(screen):  # Рисование карты
    for numi, i in enumerate(floor):
        for numj, j in enumerate(i):
            if j == 1:
                pygame.draw.rect(screen, COLOR_GREEN,
                                 (WALL * numj, WALL * numi, WALL, WALL), 1)
            if j == 0:
                pygame.draw.rect(screen, COLOR_BLUE,
                                 (WALL * numj, WALL * numi, WALL, WALL), 1)
