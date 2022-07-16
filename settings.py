'''
settings.py

Contains settings class definition used as a
settings wrapper in the game

'''

class Settings():
    '''A class to store settings for Aliens!'''

    def __init__(self):
        # Screen Settings
        self.screen_dimensions = (1200,800)
        self.bg_color = (230,230,230)   #RBG format
