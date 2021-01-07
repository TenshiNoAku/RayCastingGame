import pygame
import math
from Settings import *
from Player import *
from Floor import *
from RayCasting import *
from Render import *

mixer = pygame.mixer
mixer.init()
mixer.music.load('Data/Music/music1.mp3')
mixer.music.set_volume(0.05)
mixer.music.play()
counter = 0
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    running = True
    menu = True
    clock = pygame.time.Clock()
    player = Player()
    screen_map = pygame.Surface((SIZE[0] // 5, SIZE[1] // 5))
    render = Render(screen, screen_map)
    btn_play = pygame.Rect(400, 200, 400, 100)
    btn_exit = pygame.Rect(400, 300, 400, 100)
    texture_current_btn_play = render.texturs['btn_play']
    texture_current_btn_exit = render.texturs['btn_exit']
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                running = False
            if event.type == pygame.MOUSEMOTION:
                if btn_play.collidepoint(event.pos):
                    texture_current_btn_play = render.texturs['btn_play_pressed']
                else:
                    texture_current_btn_play = render.texturs['btn_play']
                if btn_exit.collidepoint(event.pos):
                    texture_current_btn_exit = render.texturs['btn_exit_pressed']
                else:
                    texture_current_btn_exit = render.texturs['btn_exit']
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.collidepoint(event.pos):
                    menu = False
                if btn_exit.collidepoint(event.pos):
                    menu = False
                    running = False
            if event.type == pygame.KEYDOWN:
                pass
        screen.blit(render.texturs['background_1'], (0, 0))

        screen.blit(texture_current_btn_play, btn_play[:2])
        screen.blit(texture_current_btn_exit, btn_exit[:2])

        clock.tick(600)  # Установка ограничения FPS
        print(clock.get_fps())
        pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    counter = player.destroy_block(block,counter)
                    player.destruction = True

                if ruby_block not in wall_coords:
                    print(f'Вы победили,потратив на это {counter} действий')
                    running=False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    player.destruction = False

        if player.destruction:
            player.animation_count += 1
            player.animation_count %= 16
        else:
            player.animation_count = -1


        player.movement()
        render.background()
        block_v, block_h = render.world(player.player_pos(), player.angle)
        block = player.block_check(block_v, block_h)
        render.HUD(player)
        render.mini_map(player)
        clock.tick(600)  # Установка ограничения FPS
        pygame.display.flip()
    pygame.quit()
