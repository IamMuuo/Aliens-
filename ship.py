# Contains class definition for ship
import pygame

class Ship():

    def __init__(self, screen):
        ''' Initialize the ship and set its starting position'''

        self.screen = screen

        # load the texture
        self.image = pygame.image.load('images/eagle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # movement flag
        self.moving_right = False
        self.movin_left = False

    def blitme(self):
        '''Draw ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        ''' update the ships position using the movement flag'''
        if self.moving_right:
            self.rect.centerx += 1
        elif self.movin_left:
            self.rect.centerx -= 1

