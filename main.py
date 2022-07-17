'''
Project: Aliens!

Filename: main.py
Author: hearteric57@gmail.com


Description: Contains the entry point to the game
'''

import sys
import pygame
import utils
from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create a screen object.

    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.screen_dimensions)
    pygame.display.set_caption("Aliens!")

    # make a ship
    ship = Ship(game_settings,screen)

    # start the main loop of the game

    while True:
        utils.check_events(ship)
        ship.update()
        utils.update_screen(game_settings,screen,ship)

if __name__ == '__main__':
    run_game()
