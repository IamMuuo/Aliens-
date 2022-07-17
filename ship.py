# Contains class definition for ship
import pygame

class Ship():

    def __init__(self,settings, screen):
        ''' Initialize the ship and set its starting position'''

        self.screen = screen
        self.settings = settings

        # load the texture
        self.image = pygame.image.load('images/eagle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store the devimal value for ships center
        self.center = float(self.rect.centerx)

        # movement flag
        self.moving_right = False
        self.movin_left = False

    def blitme(self):
        '''Draw ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        ''' update the ships position using the movement flag'''

        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.center += self.settings.ship_speed_factor

        elif self.movin_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        # update the rect object
        self.rect.centerx = self.center

