'''
Project: Aliens!

Filename: main.py
Author: hearteric57@gmail.com


Description: Contains the entry point to the game
'''

import sys
import pygame

def run_game():
    # Initialize game and create a screen object.

    pygame.init()

    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Aliens!")

    # start the main loop of the game

    while True:

        # watch for keyboard and mouse events

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn sceen available
        pygame.display.flip()

if __name__ == '__main__':
    run_game()
