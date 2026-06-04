import pygame 
import sys 
import settings

class Ship ():
    def __init__(self, game):
        self.game = game 
        self.setting = game.setting
        self.screen = game.setting.screen 
        self.screen_rect = self.screen.get_rect()
        

        self.ship = pygame.image.load("Images/starship.bmp")
        self.ship = pygame.transform.scale(self.ship , (50 , 50 ))
        self.rect = self.ship.get_rect()

        self.x = float(self.rect.x)
        self.rect.midbottom = self.screen_rect.midbottom
         
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def get_damaged(self):
        """Reduces lifeline when alien hits ship"""
        self.game.stats.lifeline -= 25 * self.game.hud.original_width / 100

    def reset_ship(self):
        """Resets ship's position to screen midbottom"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float (self.rect.x)