import pygame
from Settings import *
from RayCasting import *
from Floor import wall_coords


class Render:
    def __init__(self, screen, screen_map):
        self.screen = screen
        self.mini_map_screen = screen_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texturs = {'1': pygame.image.load('Data\Texture\stone1.jpg').convert(),
                        '2': pygame.image.load('Data\Texture\stone.jpg').convert(),
                        '3': pygame.image.load('Data\Texture\Ruby.jpg').convert(),
                        '4': pygame.image.load('Data\Texture\CaveWall.jpg').convert(),
                        'pickaxe_static': pygame.image.load('Data\Sprites\pickaxe.png').convert_alpha(),
                        'pickaxe_frame_0': pygame.image.load('Data\Sprites\pickaxe_frame_0.png').convert_alpha(),
                        'pickaxe_frame_1': pygame.image.load('Data\Sprites\pickaxe_frame_1.png').convert_alpha(),
                        'pickaxe_frame_2': pygame.image.load('Data\Sprites\pickaxe_frame_2.png').convert_alpha(),
                        'pickaxe_frame_3': pygame.image.load('Data\Sprites\pickaxe_frame_3.png').convert_alpha(),
                        'pickaxe_frame_4': pygame.image.load('Data\Sprites\pickaxe_frame_4.png').convert_alpha(),
                        'pickaxe_frame_5': pygame.image.load('Data\Sprites\pickaxe_frame_5.png').convert_alpha(),
                        'btn_play': pygame.image.load("Data\Texture\Button_play.png").convert_alpha(),
                        'btn_play_pressed': pygame.image.load(r'Data\Texture\button_play_pressed.png').convert_alpha(),
                        'btn_exit': pygame.image.load("Data\Texture\Button_exit.png").convert_alpha(),
                        'btn_exit_pressed': pygame.image.load(r'Data\Texture\Button_exit_pressed.png').convert_alpha(),
                        'background_1': pygame.image.load(r'Data\Backgrounds\main_menu.png').convert_alpha()

        }

    def background(self):
        pygame.draw.rect(self.screen, COLOR_DARKSLATEGRAY, (0, 0, SIZE[0], SIZE[1] // 2))
        pygame.draw.rect(self.screen, COLOR_DARKGRAY, (0, SIZE[1] // 2, SIZE[0], SIZE[1] // 2))

    def world(self, player_pos, player_angle):
        block_v, block_h = raycast(self.screen, player_pos, player_angle, self.texturs)
        return block_v, block_h

    def HUD(self, player):
        if not player.destruction:
            self.screen.blit(self.texturs['pickaxe_static'], (0, 0))
        else:
            print(player.animation_count)
            self.screen.blit(self.texturs[f'pickaxe_frame_{player.animation_count // 3}'], (0, 0))

    def mini_map(self, player):
        self.mini_map_screen.fill(COLOR_BLACK)
        map_x, map_y = player.player_pos()[0] // 5, player.player_pos()[1] // 5
        pygame.draw.line(self.mini_map_screen, COLOR_BLUE, (map_x + 1, map_y + 1), (map_x + 12 * math.cos(player.angle),
                                                                                    map_y + 12 * math.sin(
                                                                                        player.angle)), 2)
        pygame.draw.rect(self.mini_map_screen, COLOR_RED, (int(map_x), int(map_y), 5, 5))
        COLOR = COLOR_WHITE
        for x, y in wall_coords:
            if wall_texture[(x, y)] == '1':
                COLOR = (10, 10, 255)
            elif wall_texture[(x, y)] == '2':
                COLOR = (255, 255, 20)
            elif wall_texture[(x, y)] == '3':
                COLOR = (255, 0, 0)
            elif wall_texture[(x, y)] == '4':
                COLOR = (40, 40, 45)
            pygame.draw.rect(self.mini_map_screen, COLOR, (x // 5, y // 5, MAP_WALL, MAP_WALL))
        self.screen.blit(self.mini_map_screen, MAP_POS)
