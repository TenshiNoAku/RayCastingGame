import pygame
from Settings import *

floor = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта
wall_coords = []
width, height = SIZE
for numi, distance in enumerate(floor):
    for numj, j in enumerate(distance):
        if j == 1:
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
