import math
import pygame
from Settings import *


class Player:
    def __init__(self):
        self.x = 400  # Позиция игрока по оси x
        self.y = 300  # Позиция игрока по оси y
        self.angle = 0  # Угол на который повернут игрок

    def cos_sin_player(self):
        self.angle = self.angle % 360
        n_rad = self.angle * math.pi / 180
        cos = math.cos(n_rad)
        sin = math.sin(n_rad)
        return (cos, sin)

    def player_pos(self):  # Возвращение координат игрока
        return (self.x, self.y)

    def movement(self):  # Управление игрока
        cos, sin = self.cos_sin_player()
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.angle += 1
        if key[pygame.K_LEFT]:
            self.angle -= 1
        if key[pygame.K_w]:
            self.y += sin * PLAYER_SPEED
            self.x += cos * PLAYER_SPEED
        if key[pygame.K_s]:
            self.y -= sin * PLAYER_SPEED
            self.x -= cos * PLAYER_SPEED
        if key[pygame.K_a]:
            self.y -= cos * PLAYER_SPEED
            self.x += sin * PLAYER_SPEED
        if key[pygame.K_d]:
            self.y += cos * PLAYER_SPEED
            self.x -= sin * PLAYER_SPEED

    def coord_player(self):
        return (self.x // WALL, self.y // WALL)
