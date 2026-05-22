import pygame 
import sys 
class Settings():
    def __init__(self):
        #Ship settings 
        self.width = 800
        self.height = 600
        self.bg_colour = (109,122,117) 

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (0, 255, 0)
        self.bullet_speed = 2.5
        self.bullets_allowed = 3

        #Aliens settings
        self.alien_speed = 3
        