import pygame
from Settings import *
from RayCasting import *
from Floor import wall_coords


class Render:
    def __init__(self, screen, screen_map, screen2):
        self.screen = screen
        self.mini_map_screen = screen_map
        self.screen2 = screen2
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texturs = {'1': pygame.image.load('Data\Texture\DungeonWall.jpg').convert(),
                        '2': pygame.image.load('Data\Texture\stone.jpg').convert(),
                        '3': pygame.image.load('Data\Texture\stone2.jpg').convert(),
                        '4': pygame.image.load('Data\Texture\metall.jpg').convert()}

    def background(self):
        pygame.draw.rect(self.screen, COLOR_DARKSLATEGRAY, (0, 0, SIZE[0], SIZE[1] // 2))
        pygame.draw.rect(self.screen, COLOR_DARKGRAY, (0, SIZE[1] // 2, SIZE[0], SIZE[1] // 2))

    def world(self, world_object):
        for obj in sorted(world_object, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.screen.blit(object, object_pos)

    def mini_map(self, player):
        self.mini_map_screen.fill(COLOR_BLACK)
        map_x, map_y = player.player_pos()[0] // 5, player.player_pos()[1] // 5
        pygame.draw.line(self.mini_map_screen, COLOR_BLUE, (map_x+1, map_y+1), (map_x + 12 * math.cos(player.angle),
                                                                            map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.rect(self.mini_map_screen, COLOR_RED, (int(map_x), int(map_y),5,5))
        COLOR = COLOR_WHITE
        for x, y in wall_coords:
            if wall_texture[(x, y)] == '1':
                COLOR = (10, 10, 255)
            elif wall_texture[(x, y)] == '2':
                COLOR = (255, 255, 20)
            elif wall_texture[(x, y)] == '3':
                COLOR = (30, 30, 60)
            elif wall_texture[(x, y)] == '4':
                COLOR = (40, 40, 45)
            pygame.draw.rect(self.mini_map_screen, COLOR, (x // 5, y // 5, MAP_WALL, MAP_WALL))
        self.screen2.blit(self.mini_map_screen, MAP_POS)