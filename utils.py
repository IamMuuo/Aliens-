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

        elif event.type == pygame.KEYDOWN:
            # Pilot the ship
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                ship.movin_left = True

        elif event.type == pygame.KEYUP:
            # stop moving
            if event.key == pygame.K_LEFT:
                ship.movin_left = False
            elif event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(settings, screen, ship):
    '''Render objects into the screen'''

    screen.fill(settings.bg_color)
    ship.blitme()

    # Render
    pygame.display.flip()
