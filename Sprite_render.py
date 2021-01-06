import pygame
from Settings import *

class Sprites:
    def __init__(self):
        self.images = {
            'box': pygame.image.load('Sprites/box.png').convert_alpha()
        }
        self.list_sprites = {
            Sprit_object(self.images['box'], True, (1.2, 1.2), 1.8, 0.4)
        }
class Sprit_object:
    def __init__(self, object, ststic, pos, shift, scale):
        self.object = object
        self.ststic = ststic
        self.pos = self.x, self.y = pos[0] * WALL, pos[1] * WALL
        self.shift = shift
        self.scale = scale

    def object_locate(self, player, walls):
        x, y = player.coord_player()
        player_angle = player.player_angle()
        dx, dy = self.x - x, self.y - y
        dist_to_sprite = math.sqrt(dx ** 2 + dy ** 2)

        theta = math.atan2(dy, dx)
        gamma = theta - player_angle

        if dx > 0 and 180 <= math.degrees(player_angle) <= 360 or dx < 0 and dy < 0:
            gamma += DOUBLE_PI

        delta_rays = int(gamma// DELTA_ANGLE)
        current_ray = CENTRAL_RAY + delta_rays
        dist_to_sprite *= math.cos(HALF_FOV - current_ray * DELTA_ANGLE)

        if 0 <= current_ray <= RAY_NUMBER - 1 and dist_to_sprite < walls[current_ray][0]:
            proj_height = (PROJ_COEFF / dist_to_sprite * self.scale)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            sprite_pos = (current_ray * SCALE - half_proj_height, SIZE[1] // 2 - half_proj_height + shift)
            sprite = pygame.transform.scale(self.object, (proj_height, proj_height))
            return (dist_to_sprite, sprite, sprite_pos)
        else:
            return (False,)


