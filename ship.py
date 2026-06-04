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


    def update (self):
        """Updates the Rect coordinates of Ship"""
        if self.moving_right:
            if not self.rect.right >= self.screen_rect.right:
                self.rect.centerx += 3
        if self.moving_left:                              
            if not self.rect.left <= self.screen_rect.left:
                self.rect.centerx -= 3
        if self.moving_down:
            if not self.rect.bottom >= self.screen_rect.bottom:
                self.rect.bottom += 3
        if self.moving_up:
            if not self.rect.top <= self.screen_rect.top:
                self.rect.y -=3
    def get_damaged(self):
        """Reduces lifeline when alien hits ship"""
        self.game.stats.lifeline -= 25 * self.game.hud.original_width / 100

    def reset_ship(self):
        """Resets ship's position to screen midbottom"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float (self.rect.x)