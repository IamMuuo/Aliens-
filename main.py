'''
Project: Aliens!

Filename: main.py
Author: hearteric57@gmail.com


Description: Contains the entry point to the game
'''

import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create a screen object.

    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Aliens!")

    # make a ship
    ship = Ship(screen)

    # start the main loop of the game

    while True:

        # watch for keyboard and mouse events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn sceen available
        screen.fill(game_settings.bg_color)
        ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    run_game()
