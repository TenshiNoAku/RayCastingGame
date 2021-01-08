import random
from Settings import *

test_floor = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]
floor1 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 4],
    [4, 1, 1, 2, 2, 2, 0, 3, 0, 0, 4, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 4],
    [4, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]  # Карта

floor2 = [

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 's', 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 2, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 3, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 3, 1, 2, 0, 1],
    [1, 0, 2, 2, 0, 0, 2, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта
floor3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 's', 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 2, 3, 1, 0, 0, 1],
    [1, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта

floor4 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 2, 1, 2, 1, 2, 2, 1, 0, 4],
    [4, 0, 2, 0, 1, 0, 1, 1, 2, 1, 4, 4],
    [4, 0, 1, 0, 2, 0, 1, 2, 3, 2, 0, 4],
    [4, 0, 2, 1, 1, 1, 2, 1, 2, 1, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor5 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 1, 2, 1, 2, 1, 2, 1, 2, 1, 3, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor6 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 2, 0, 0, 0, 0, 1, 0, 1, 0, 4],
    [4, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 4],
    [4, 0, 2, 0, 0, 2, 0, 1, 0, 1, 0, 4],
    [4, 1, 0, 1, 2, 0, 2, 0, 0, 0, 0, 4],
    [4, 0, 1, 0, 0, 2, 0, 0, 2, 0, 0, 4],
    [4, 1, 0, 1, 0, 0, 0, 2, 3, 2, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor7 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 2, 1, 2, 1, 's', 1, 2, 1, 2, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 3, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor8 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2),
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
    [4, 's', 0, 0, 0, 0, 2, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 4],
    [4, 0, 0, 0, 1, 2, 3, 2, 1, 0, 0, 4],
    [4, 0, 0, 0, 0, 2, 1, 2, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

floor10 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 2, 2, 0, 0, 0, 0, 2, 2, 0, 4],
    [4, 0, 2, 3, 2, 0, 0, 2, 0, 0, 2, 4],
    [4, 0, 2, 2, 0, 0, 0, 0, 0, 2, 0, 4],
    [4, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 4],
    [4, 0, 2, 0, 0, 2, 0, 2, 2, 2, 2, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]

class Floor:
    def __init__(self):
        self.wall_coords = []
        self.wall_collise = []
        self.wall_texture = {}
        width, height = SIZE
        for numi, distance in enumerate(floor1):
            for numj, j in enumerate(distance):
                if j == 1:
                    self.wall_texture[(WALL * numj, WALL * numi)] = '1'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 2:
                    self.wall_texture[(WALL * numj, WALL * numi)] = '2'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 3:
                    self.wall_texture[(WALL * numj, WALL * numi)] = '3'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                    self.ruby_block = (numj * WALL, numi * WALL)
                elif j == 4:
                    self.wall_texture[(WALL * numj, WALL * numi)] = '4'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 's':
                    self.spawn = (numj * WALL + 50, numi * WALL + 50)
    def update(self, lvl):
        self.wall_coords = []
        self.wall_collise = []
        self.wall_texture = {}
        width, height = SIZE
        for numi, distance in enumerate(eval(f'floor{lvl}')):
            for numj, j in enumerate(distance):
                if j == 1:
                    self.wall_texture[(WALL * numj, WALL * numi)] = '1'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 2:
                    self.wall_texture[(WALL * numj, WALL * numi)] = '2'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 3:
                    self.wall_texture[(WALL * numj, WALL * numi)] = '3'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                    self.ruby_block = (numj * WALL, numi * WALL)
                elif j == 4:
                    self.wall_texture[(WALL * numj, WALL * numi)] = '4'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 's':
                    self.spawn = (numj * WALL + 50, numi * WALL + 50)



def render(screen):  # Рисование карты
    for numi, i in enumerate(floor10):
        for numj, j in enumerate(i):
            if j == 1:
                pygame.draw.rect(screen, COLOR_GREEN,
                                 (WALL * numj, WALL * numi, WALL, WALL), 1)
            if j == 0:
                pygame.draw.rect(screen, COLOR_BLUE,
                                 (WALL * numj, WALL * numi, WALL, WALL), 1)
