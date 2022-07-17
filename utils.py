'''
utils.py

Contains game functions

'''

import sys
import pygame

def check_events(ship):
    '''Respond to keypress and mouse events '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        check_key_up_movements(event, ship)
        check_key_down_movements(event,ship)


def update_screen(settings, screen, ship):
    '''Render objects into the screen'''

    screen.fill(settings.bg_color)
    ship.blitme()

    # Render
    pygame.display.flip()


def check_key_up_movements(event, ship):
     if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            ship.movin_left = True


def check_key_down_movements(event, ship):
    if event.type == pygame.KEYUP:
        # stop moving
        if event.key == pygame.K_LEFT:
            ship.movin_left = False
        elif event.key == pygame.K_RIGHT:
            ship.moving_right = False
