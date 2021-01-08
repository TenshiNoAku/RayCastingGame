import math
import pygame
from Settings import *


class Player:
    def __init__(self, floor):
        self.x = 150  # Позиция игрока по оси x
        self.y = 150  # Позиция игрока по оси y
        self.angle = 0  # Угол на который повернут игрок
        self.player_collise = pygame.Rect(self.x, self.y, 5, 5)
        self.destruction = False
        self.animation_count = 0
        self.lvl = 1
        self.floor = floor
        self.counter = 0

    def cos_sin_player(self):
        cos = math.cos(self.angle)
        sin = math.sin(self.angle)
        return (cos, sin)

    def player_pos(self):  # Возвращение координат игрока
        return (self.x, self.y)

    def movement(self):  # Управление игрока
        cos, sin = self.cos_sin_player()
        key = pygame.key.get_pressed()
        rx = self.x
        ry = self.y
        if key[pygame.K_RIGHT]:
            self.angle += 0.04
        if key[pygame.K_LEFT]:
            self.angle -= 0.04
        if key[pygame.K_w]:
            ry += sin * PLAYER_SPEED
            rx += cos * PLAYER_SPEED
            self.check_collision(rx, ry)
        if key[pygame.K_s]:
            ry -= sin * PLAYER_SPEED
            rx -= cos * PLAYER_SPEED
            self.check_collision(rx, ry)
        if key[pygame.K_a]:
            ry -= cos * PLAYER_SPEED
            rx += sin * PLAYER_SPEED
            self.check_collision(rx, ry)
        if key[pygame.K_d]:
            ry += cos * PLAYER_SPEED
            rx -= sin * PLAYER_SPEED
            self.check_collision(rx, ry)
        self.player_collise = pygame.Rect(self.x - 5, self.y - 5, 5, 5)

    def check_collision(self, x, y):
        if pygame.Rect.collidelist(pygame.Rect(x, y, 25, 25), self.floor.wall_collise) == -1:
            self.x, self.y = x, y
        elif pygame.Rect.collidelist(pygame.Rect(self.x, y, 25, 25), self.floor.wall_collise) == -1:
            self.y = y
        elif pygame.Rect.collidelist(pygame.Rect(x, self.y, 25, 25), self.floor.wall_collise) == -1:
            self.x = x

    def coord_player(self):
        return (self.x // WALL, self.y // WALL)

    def block_check(self, block_v, block_h):
        if block_v[0] < block_h[0] or block_v[1] < block_h[1]:
            block = block_v
        else:
            block = block_h
        return block

    def destroy_block(self, block,counter):
        if block in self.floor.wall_coords:
            x, y = self.player_pos()
            dist = math.sqrt((x - block[0]) ** 2 + (y - block[1]) ** 2)
            if block[0] > 0 and block[1] > 0 and block[0] < 1100 and block[1] < 700 and dist <= 200:
                ind = self.floor.wall_coords.index(block)
                del self.floor.wall_coords[ind]
                del self.floor.wall_collise[ind]
                counter += 1
        return counter

    def respawn(self):
        self.x, self.y = self.floor.spawn
        #self.counter = 0

