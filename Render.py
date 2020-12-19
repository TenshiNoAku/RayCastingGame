import pygame
from Settings import *
from RayCasting import *
from Floor import wall_coords


class Render:
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.mini_map_screen = screen_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.screen, COLOR_BLUE, (0, 0, SIZE[0], SIZE[1] // 2))
        pygame.draw.rect(self.screen, COLOR_DARKGRAY, (0, SIZE[1] // 2, SIZE[0], SIZE[1] // 2))

    def world(self, player_pos, player_angle):
        raycast(self.screen, player_pos, player_angle)

    def mini_map(self, player):
        self.mini_map_screen.fill(COLOR_BLACK)
        map_x, map_y = player.player_pos()[0] // 5, player.player_pos()[1] // 5
        pygame.draw.line(self.mini_map_screen, COLOR_BLUE, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                                            map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.mini_map_screen, COLOR_RED, (int(map_x), int(map_y)), 5)
        for x, y in wall_coords:
            pygame.draw.rect(self.mini_map_screen, COLOR_GREEN, (x, y, MAP_WALL, MAP_WALL))
        self.screen.blit(self.mini_map_screen, MAP_POS)
