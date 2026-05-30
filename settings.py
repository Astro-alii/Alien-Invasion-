import pygame 
import sys 
class Settings():
    def __init__(self, game):
        #screen_settings
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN )
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height 

        pygame.display.set_caption ("Alien Invasion")
        icon = pygame.image.load ("Images/alien_icon.png")
        pygame.display.set_icon(icon)
        
        #Backgrounf Image setting
        self.bg_image = pygame.image.load("Images/spacebg.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen.get_rect().width , self.screen.get_rect().height))
        self.bg_image_rect = self.bg_image.get_rect()
        self.bg_image_rect.topleft = (0,0) 

        
        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (0, 255, 0)
        self.bullet_speed = 15
        self.bullets_allowed = 2

        #Powerstrike settings
        self.ps_width = 40 
        self.ps_height = 40
        self.ps_speed = 5
        self.ps_allowed = 1

        #Aliens settings
        self.alien_speed = 5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #new level speed multiplier
        self.speed_increase = 1.1
        #Ship settings
        self.ship_limit = 3
        #Scoring
        self.alien_points = 10
    def initialize_settings(self):
        self.alien_speed = 5
        self.bullet_speed = 15
        self.ps_speed = 5

    def new_level_settings(self):
        self.alien_speed *= self.speed_increase
        self.bullet_speed *= self.speed_increase
        self.ps_speed *= self.speed_increase

        