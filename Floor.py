import random
from Settings import *
import pygame

test_floor = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]
floor1 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 2, 0, 2, 0, 0, 0, 0, 0, 4],
    [4, 1, 1, 2, 2, 2, 0, 1, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 4],
    [4, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]  # Карта

floor2 = [

    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 's', 1, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 2, 1, 2, 2, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 2, 1, 2, 0, 1],
    [1, 0, 2, 2, 0, 0, 2, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]  # Карта
floor3 = [
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 2, 0, 0, 0, 0, 0, 0, 1, 1, 4],
    [4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 4],
    [4, 0, 0, 0, 0, 1, 1, 2, 0, 3, 0, 4],
    [4, 0, 1, 0, 0, 0, 2, 2, 1, 0, 0, 4],
    [4, 0, 0, 2, 2, 0, 0, 1, 1, 0, 0, 4],
    [4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

]  # Карта

floor4 = [

    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [4, 's', 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 1, 2, 1, 2, 1, 2, 2, 1, 0, 4],
    [4, 0, 2, 0, 1, 0, 1, 1, 2, 1, 0, 4],
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
        self.update(1)
    def update(self, lvl):
        self.walls = []
        self.wall_coords = []
        self.wall_collise = []
        self.wall_texture = {}
        width, height = SIZE
        for numi, distance in enumerate(eval(f'floor{lvl}')):
            for numj, j in enumerate(distance):
                if j == 1:
                    self.walls.append(Block((WALL * numj, WALL * numi), '1',
                                            pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2)))
                    self.wall_texture[(WALL * numj, WALL * numi)] = '1'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 2:
                    self.walls.append(Block((WALL * numj, WALL * numi), '2',
                                            pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2)))
                    self.wall_texture[(WALL * numj, WALL * numi)] = '2'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 3:
                    self.walls.append(Block((WALL * numj, WALL * numi), '3',
                                            pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2), ruby=True))
                    self.wall_texture[(WALL * numj, WALL * numi)] = '3'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                    self.ruby_block = (numj * WALL, numi * WALL)
                elif j == 4:
                    self.walls.append(Block((WALL * numj, WALL * numi), '4',
                                            pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2), destructibility=False))

                    self.wall_texture[(WALL * numj, WALL * numi)] = '4'
                    self.wall_coords.append((WALL * numj, WALL * numi))
                    self.wall_collise.append(pygame.Rect(WALL * numj, WALL * numi, WALL + 2, WALL + 2))
                elif j == 's':
                    self.spawn = (numj * WALL + 50, numi * WALL + 50)
    def checkout_block(self, wall):
        check = False
        for index, block in enumerate(self.walls):
            if block.coords == wall:
                check = True
                break
        return check, index

    def search_ruby(self):
        check = False
        for block in self.walls:
            if block.ruby:
                check = True
                break

        return check

    def search_wall_collise(self):
        wall_collise = []
        for block in self.walls:
            wall_collise.append(block.collise)
        return wall_collise



class Block:
    def __init__(self, coords, texture, collise, destructibility=True, ruby=False):
        self.coords = self.x, self.y = coords
        self.texture = texture
        self.collise = collise
        self.destructibility = destructibility
        self.level_of_destruction = 0
        self.ruby = ruby
        self.start_destruction = 0





def render(screen):  # Рисование карты
    for numi, i in enumerate(floor10):
        for numj, j in enumerate(i):
            if j == 1:
                pygame.draw.rect(screen, COLOR_GREEN,
                                 (WALL * numj, WALL * numi, WALL, WALL), 1)
            if j == 0:
                pygame.draw.rect(screen, COLOR_BLUE,
                                 (WALL * numj, WALL * numi, WALL, WALL), 1)
