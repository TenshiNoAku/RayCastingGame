from RayCasting import *
from numba import njit



class Render:
    def __init__(self, screen, screen_map, floor, player):
        self.floor = floor
        self.screen = screen
        self.player = player
        self.mini_map_screen = screen_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.texturs = {
            '1': pygame.image.load(r'Data\Texture\stone1.jpg').convert(),
                        '2': pygame.image.load(r'Data\Texture\stone.jpg').convert(),
                        '3': pygame.image.load(r'Data\Texture\Ruby.jpg').convert(),
                        '4': pygame.image.load(r'Data\Texture\CaveWall.jpg').convert(),
                        'pickaxe_static': pygame.image.load(r'Data\Sprites\pickaxe.png').convert_alpha(),
                        'pickaxe_frame_0': pygame.image.load(r'Data\Sprites\pickaxe_frame_0.png').convert_alpha(),
                        'pickaxe_frame_1': pygame.image.load(r'Data\Sprites\pickaxe_frame_1.png').convert_alpha(),
                        'pickaxe_frame_2': pygame.image.load(r'Data\Sprites\pickaxe_frame_2.png').convert_alpha(),
                        'pickaxe_frame_3': pygame.image.load(r'Data\Sprites\pickaxe_frame_3.png').convert_alpha(),
                        'pickaxe_frame_4': pygame.image.load(r'Data\Sprites\pickaxe_frame_4.png').convert_alpha(),
                        'pickaxe_frame_5': pygame.image.load(r'Data\Sprites\pickaxe_frame_5.png').convert_alpha(),
                        'black': pygame.image.load(r'Data\Texture\black.png').convert_alpha(),
                        'btn_play': pygame.image.load(r"Data\Texture\Button_play.png").convert_alpha(),
                        'btn_play_pressed': pygame.image.load(r'Data\Texture\Button_play_pressed.png').convert_alpha(),
                        'btn_main_menu': pygame.image.load(r"Data\Texture\Button_main_menu.png").convert_alpha(),
                        'btn_main_menu_pressed': pygame.image.load(r'Data\Texture\Button_main_menu_pressed.png').convert_alpha(),
                        'btn_exit': pygame.image.load(r"Data\Texture\Button_exit.png").convert_alpha(),
                        'btn_exit_pressed': pygame.image.load(r'Data\Texture\Button_exit_pressed.png').convert_alpha(),
                        'btn_settings': pygame.image.load(r"Data\Texture\Button_settings.png").convert_alpha(),
                        'btn_settings_pressed': pygame.image.load(r'Data\Texture\Button_settings_pressed.png').convert_alpha(),
                        'btn_next_level': pygame.image.load(r"Data\Texture\Button_next_level.png").convert_alpha(),
                        'btn_next_level_pressed': pygame.image.load(r'Data\Texture\Button_next_level_pressed.png').convert_alpha(),
                        'btn_off': pygame.image.load(r"Data\Texture\button_off.png").convert_alpha(),
                        'btn_on': pygame.image.load(r"Data\Texture\button_on.png").convert_alpha(),
                        'aim': pygame.image.load(r"Data\Texture\aim.png").convert_alpha(),
                        'Background_hud': pygame.transform.scale(
                            pygame.image.load(r'Data\Texture\Background_hud.png').convert_alpha(), (300, 150)),
                        'fracture_1': pygame.image.load(r"Data\Texture\Fracture\fracture_1.png").convert_alpha(),
                        'fracture_2': pygame.image.load(r"Data\Texture\Fracture\fracture_2.png").convert_alpha(),
                        'fracture_3': pygame.image.load(r"Data\Texture\Fracture\fracture_3.png").convert_alpha(),
                        'fracture_4': pygame.image.load(r"Data\Texture\Fracture\fracture_4.png").convert_alpha(),
                        'fracture_5': pygame.image.load(r"Data\Texture\Fracture\fracture_5.png").convert_alpha(),
                        'background_settings': pygame.image.load(
                            r"Data\Texture\Background_settings.png").convert_alpha(),
                        'background_inside_game_menu': pygame.image.load(
                            r"Data\Texture\Background_inside_game_menu.png").convert_alpha(),
                        'background_1': pygame.image.load(r'Data\Backgrounds\main_menu.png').convert_alpha()

                        }
        self.century_schoolbook = pygame.font.SysFont('Century Schoolbook', 25)

    def background(self):
        pygame.draw.rect(self.screen, COLOR_DARKSLATEGRAY, (0, 0, SIZE[0], SIZE[1] // 2))
        pygame.draw.rect(self.screen, COLOR_DARKGRAY, (0, SIZE[1] // 2, SIZE[0], SIZE[1] // 2))

    def world(self, player_pos, player_angle):
        block_v, block_h = raycast(self.screen, player_pos, player_angle, self.texturs, self.floor)
        return block_v, block_h

    def HUD(self, player):
        text_level = self.century_schoolbook.render('Level: ' + str(player.lvl), False, (51, 51, 51))
        text_counter = self.century_schoolbook.render('Разрушено блоков: ' + str(player.counter), False, (51, 51, 51))

        if not player.destruction:
            self.screen.blit(self.texturs['pickaxe_static'], (0, 0))
        else:
            self.screen.blit(self.texturs[f'pickaxe_frame_{player.animation_count // 3}'], (0, 0))
        self.screen.blit(self.texturs['Background_hud'], (0, 0))
        self.screen.blit(text_level, (20, 10))
        self.screen.blit(text_counter, (20, 30))
        self.screen.blit(self.texturs['aim'], (HALF_WIDTH - 25, HALF_HEIGHT - 25))

    def mini_map(self, player):
        self.mini_map_screen.fill(COLOR_BLACK)
        map_x, map_y = player.player_pos()[0] // 5, player.player_pos()[1] // 5
        pygame.draw.line(self.mini_map_screen, COLOR_BLUE, (map_x + 1, map_y + 1), (map_x + 12 * math.cos(player.angle),
                                                                                    map_y + 12 * math.sin(
                                                                                        player.angle)), 2)
        pygame.draw.rect(self.mini_map_screen, COLOR_RED, (int(map_x), int(map_y), 5, 5))
        COLOR = COLOR_WHITE
        for x, y in self.floor.wall_coords:
            if self.floor.wall_texture[(x, y)] == '1':
                COLOR = (10, 10, 255)
            elif self.floor.wall_texture[(x, y)] == '2':
                COLOR = (255, 255, 20)
            elif self.floor.wall_texture[(x, y)] == '3':
                COLOR = (255, 0, 0)
            elif self.floor.wall_texture[(x, y)] == '4':
                COLOR = (40, 40, 45)
            pygame.draw.rect(self.mini_map_screen, COLOR, (x // 5, y // 5, MAP_WALL, MAP_WALL))
        self.screen.blit(self.mini_map_screen, MAP_POS)
