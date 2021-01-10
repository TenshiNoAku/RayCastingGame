from Floor import *
from Player import *
from Render import *
import sqlite3

con = sqlite3.connect('Data/Data_Base/Game_db.sqlite')

cur = con.cursor()

mixer = pygame.mixer
mixer.init()
sound = pygame.mixer.Sound('Data/Music/Stone_Destroy.mp3')
mixer.music.load('Data/Music/music1.mp3')
mixer.music.set_volume(0.01)
mixer.music.play()
sound.set_volume(0.02)
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    screen_map = pygame.Surface((SIZE[0] // 5, SIZE[1] // 5))
    splash_screen = pygame.Surface(SIZE)

    running = True

    mode = 'main_menu'
    last_mode = None
    clock = pygame.time.Clock()

    floor = Floor()
    player = Player(floor)
    render = Render(screen, screen_map, floor, player)

    background_insade_game_menu = pygame.Surface(SIZE)

    btn_next_level = btn_play = pygame.Rect(400, 200, 400, 100)
    btn_settings = pygame.Rect(400, 300, 400, 100)
    btn_exit = pygame.Rect(400, 400, 400, 100)
    btn_main_menu = pygame.Rect(400, 400, 400, 100)
    btn_on_off = pygame.Rect(920, 275, 70, 40)
    btn_exit_settings = pygame.Rect(1010, 175, 40, 40)

    background = render.texturs['background_1']
    texture_current_btn_play = render.texturs['btn_play']
    texture_current_btn_settings = render.texturs['btn_settings']
    texture_current_btn_exit = render.texturs['btn_exit']
    texture_current_btn_main_menu = render.texturs['btn_main_menu']
    texture_current_btn_next_level = render.texturs['btn_next_level']
    texture_current_btn_on_off = render.texturs['btn_on']
    player.control = cur.execute("""Select control from Settings""").fetchone()[0]
    if player.control == 'arrows':
        texture_current_btn_on_off = render.texturs['btn_on']
    else:
        texture_current_btn_on_off = render.texturs['btn_off']
    alpha_channal = 0
    alpha_channal_count = 1
    player.lvl = cur.execute("""Select Current_floor from Settings""").fetchone()[0]
    floor.update(player.lvl)
    while running:
        if mode == 'game':
            if not floor.search_ruby():
                if cur.execute(f"""Select floor_record{player.lvl} from Record""").fetchone()[0] > player.counter:
                    cur.execute(f"""UPDATE Record SET floor_record{player.lvl} = {player.counter}""")
                    con.commit()
                player.lvl += 1
                if player.lvl > 10:
                    record_max = 0
                    for i in range(1, 10):
                        record_max += cur.execute(f"""Select floor_record{i} from Record""").fetchone()[0]
                    if record_max < cur.execute(f"""Select General_record from Record""").fetchone()[0]:
                        cur.execute(f"""UPDATE Record SET General_record = {record_max}""")
                        con.commit()
                    player.lvl = 1
                mode = 'splash_screen1'
                floor.update(player.lvl)
                player.respawn()
                background_insade_game_menu.blit(screen, (0, 0))
                cur.execute(f"""UPDATE Settings SET Current_Floor = {player.lvl}""")
                con.commit()
            mouse_buttons = pygame.mouse.get_pressed()
            pygame.mouse.set_visible(False)
            block_v, block_h = render.world(player.player_pos(), player.angle)
            block = player.block_check(block_v, block_h)
            block_object = floor.walls[floor.checkout_block(block)[1]]
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION and player.control == 'mouse':
                    player.mousemotion(event.pos[0] - HALF_WIDTH)
                    pygame.mouse.set_pos(HALF_WIDTH, HALF_HEIGHT)
            if (key[pygame.K_LEFT] or key[pygame.K_RIGHT]) and player.control == 'arrows':
                player.arrow_motion()
            x, y = player.player_pos()
            dist = math.sqrt((x - block[0]) ** 2 + (y - block[1]) ** 2)
            if key[pygame.K_q] and dist < 200 and player.control == 'arrows' or (
                    mouse_buttons[0] == 1 and dist < 200 and player.control == 'mouse'):
                block_object = floor.walls[floor.checkout_block(block)[1]]
                player.destruction = True
            else:
                player.destruction = False
            if key[pygame.K_ESCAPE]:
                mode = 'inside_game_menu'

            if player.destruction:
                player.animation_count += 1
                player.animation_count %= 16
                if player.animation_count % 3 == 1:
                    block_object.level_of_destruction += 1
                    if block_object.level_of_destruction == 6:
                        player.destroy_block(block)
                        sound.play()
            else:
                block_object.level_of_destruction = 0
                player.animation_count = -1

            player.movement()
            render.background()
            block_v, block_h = render.world(player.player_pos(), player.angle)
            block = player.block_check(block_v, block_h)
            render.HUD(player)
            render.mini_map(player)
            if mode == 'inside_game_menu' or mode == 'splash_screen':
                background_insade_game_menu.blit(screen, (0, 0))
                last_mode = 'game'
                # background = background_insade_game_menu
            clock.tick(600)  # Установка ограничения FPS
            pygame.display.flip()
        elif mode == 'main_menu':
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    if btn_play.collidepoint(event.pos):
                        texture_current_btn_play = render.texturs['btn_play_pressed']
                    else:
                        texture_current_btn_play = render.texturs['btn_play']
                    if btn_settings.collidepoint(event.pos):
                        texture_current_btn_settings = render.texturs['btn_settings_pressed']
                    else:
                        texture_current_btn_settings = render.texturs['btn_settings']
                    if btn_exit.collidepoint(event.pos):
                        texture_current_btn_exit = render.texturs['btn_exit_pressed']
                    else:
                        texture_current_btn_exit = render.texturs['btn_exit']

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_play.collidepoint(event.pos):
                        mode = 'game'
                    if btn_settings.collidepoint(event.pos):
                        mode = 'settings'
                        last_mode = 'main_menu'
                    if btn_exit.collidepoint(event.pos):
                        running = False
                if event.type == pygame.KEYDOWN:
                    pass
            screen.blit(background, (0, 0))

            screen.blit(texture_current_btn_play, btn_play[:2])
            screen.blit(texture_current_btn_settings, btn_settings[:2])
            screen.blit(texture_current_btn_exit, btn_exit[:2])

            clock.tick(600)  # Установка ограничения FPS
            pygame.display.flip()
        elif mode == 'inside_game_menu':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    if btn_play.collidepoint(event.pos):
                        texture_current_btn_play = render.texturs['btn_play_pressed']
                    else:
                        texture_current_btn_play = render.texturs['btn_play']
                    if btn_settings.collidepoint(event.pos):
                        texture_current_btn_settings = render.texturs['btn_settings_pressed']
                    else:
                        texture_current_btn_settings = render.texturs['btn_settings']
                    if btn_main_menu.collidepoint(event.pos):
                        texture_current_btn_main_menu = render.texturs['btn_main_menu_pressed']
                    else:
                        texture_current_btn_main_menu = render.texturs['btn_main_menu']
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_play.collidepoint(event.pos):
                        mode = 'game'
                    if btn_settings.collidepoint(event.pos):
                        mode = 'settings'
                    if btn_main_menu.collidepoint(event.pos):
                        mode = 'main_menu'
                        # background.blit(render.texturs['background_1'], (0, 0))

            pygame.mouse.set_visible(True)
            # Отрисовка заднего фона
            screen.blit(background_insade_game_menu, (0, 0))

            # Отрисовка рамки внутриигрового меню
            screen.blit(render.texturs['background_inside_game_menu'], (375, 100))

            # Отриовка кнопок внутригрового меню
            screen.blit(texture_current_btn_play, btn_play[:2])
            screen.blit(texture_current_btn_settings, btn_settings[:2])
            screen.blit(texture_current_btn_main_menu, btn_main_menu[:2])

            clock.tick(600)  # Установка ограничения FPS
            pygame.display.flip()
        elif mode == 'settings':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                # if event.type == pygame.MOUSEMOTION:
                #
                # if btn_play.collidepoint(event.pos):
                #     texture_current_btn_play = render.texturs['btn_play_pressed']
                # else:
                #     texture_current_btn_play = render.texturs['btn_play']
                # if btn_settings.collidepoint(event.pos):
                #     texture_current_btn_settings = render.texturs['btn_settings_pressed']
                # else:
                #     texture_current_btn_settings = render.texturs['btn_settings']
                # if btn_main_menu.collidepoint(event.pos):
                #     texture_current_btn_main_menu = render.texturs['btn_main_menu_pressed']
                # else:
                #     texture_current_btn_main_menu = render.texturs['btn_main_menu']
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_on_off.collidepoint(event.pos):
                        if texture_current_btn_on_off == render.texturs['btn_on']:
                            texture_current_btn_on_off = render.texturs['btn_off']
                            player.control = 'mouse'
                        else:
                            texture_current_btn_on_off = render.texturs['btn_on']
                            player.control = 'arrows'
                    if btn_exit_settings.collidepoint(event.pos):
                        mode = last_mode
                    # if btn_settings.collidepoint(event.pos):
                    #     mode = 'settings'
                    # if btn_main_menu.collidepoint(event.pos):
                    #     mode = 'main_menu'

            pygame.mouse.set_visible(True)
            # Отрисовка заднего фона
            if last_mode == 'game':
                screen.blit(background_insade_game_menu, (0, 0))
            else:
                screen.blit(background, (0, 0))

            # Отрисовка рамки внутриигрового меню
            screen.blit(render.texturs['background_settings'], (150, 175))

            # Отриовка кнопок внутригрового меню
            screen.blit(texture_current_btn_on_off, btn_on_off[:2])

            clock.tick(600)  # Установка ограничения FPS
            pygame.display.flip()
        elif mode == 'splash_screen1':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEMOTION:
                    if pygame.Rect(btn_play[0], btn_play[1] + 100, btn_play[2], btn_play[3]).collidepoint(event.pos):
                        texture_current_btn_next_level = render.texturs['btn_next_level_pressed']
                    else:
                        texture_current_btn_next_level = render.texturs['btn_next_level']
                    if pygame.Rect(btn_settings[0], btn_settings[1] + 100, btn_settings[2],
                                   btn_settings[3]).collidepoint(event.pos):
                        texture_current_btn_main_menu = render.texturs['btn_main_menu_pressed']
                    else:
                        texture_current_btn_main_menu = render.texturs['btn_main_menu']
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(btn_play[0], btn_play[1] + 100, btn_play[2], btn_play[3]).collidepoint(event.pos):
                        mode = 'splash_screen2'
                        alpha_channal = 0
                        alpha_channal_count = 1
                    if pygame.Rect(btn_settings[0], btn_settings[1] + 100, btn_settings[2],
                                   btn_settings[3]).collidepoint(event.pos):
                        mode = 'main_menu'

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_exit_settings.collidepoint(event.pos):
                        mode = 'main_menu'

                    # if btn_settings.collidepoint(event.pos):
                    #     mode = 'settings'
                    # if btn_main_menu.collidepoint(event.pos):
                    #     mode = 'main_menu'

            pygame.mouse.set_visible(True)
            # Отрисовка заднего фона
            screen.blit(background, (0, 0))

            # Отрисовка рамки внутриигрового меню
            screen.blit(render.texturs['background_settings'], (150, 175))

            # Отриовка кнопок внутригрового меню
            screen.blit(texture_current_btn_next_level, (btn_play[0], btn_play[1] + 100))
            screen.blit(texture_current_btn_main_menu, (btn_settings[0], btn_settings[1] + 100))

            clock.tick(600)  # Установка ограничения FPS
            pygame.display.flip()
        elif mode == 'splash_screen2':

            pygame.mouse.set_visible(True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if alpha_channal < 255 and alpha_channal_count == 1:
                screen.blit(background, (0, 0))
                alpha_channal += alpha_channal_count
            elif alpha_channal == 255:
                screen.blit(background_insade_game_menu, (0, 0))
                alpha_channal_count = -1
                alpha_channal += alpha_channal_count
            elif alpha_channal < 255 and alpha_channal_count == -1:
                screen.blit(background_insade_game_menu, (0, 0))
                alpha_channal += alpha_channal_count
            splash_screen.fill((0, 0, 0))
            splash_screen.set_alpha(alpha_channal)
            screen.blit(splash_screen, (0, 0))
            if alpha_channal < 1 and alpha_channal_count == -1:
                mode = 'game'

            clock.tick(600)  # Установка ограничения FPS
            pygame.display.flip()
        # print(bool(texture_current_btn_on_off == render.texturs['btn_on']))
        # print(player.control)
    cur.execute(f"""UPDATE Settings SET Control = '{player.control}'""")
    con.commit()
pygame.quit()
