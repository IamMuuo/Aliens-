'''
utils.py

Contains game functions

'''

import sys
import pygame

def check_events():
    '''Respond to keypress and mouse events '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings, screen, ship):
    '''Render objects into the screen'''

    screen.fill(settings.bg_color)
    ship.blitme()

    # Render
    pygame.display.flip()
