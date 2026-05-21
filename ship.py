import pygame 
import sys 

class Ship ():
    def __init__(self, game):
        self.game = game 

        self.screen = game.screen 
        self.screen_rect = self.screen.get_rect()
        

        self.ship = pygame.image.load("Images/starship.bmp")
        self.ship = pygame.transform.scale(self.ship , (100 , 100 ))
        self.ship_rect = self.ship.get_rect()

        self.ship_rect.midbottom = self.screen_rect.midbottom
         
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update (self):
        if self.moving_right:
            if not self.ship_rect.right >= self.screen_rect.right:
                self.ship_rect.centerx += 3
        if self.moving_left:                              
            if not self.ship_rect.left <= self.screen_rect.left:
                self.ship_rect.centerx -= 3
        if self.moving_down:
            if not self.ship_rect.bottom >= self.screen_rect.bottom:
                self.ship_rect.bottom += 3
        if self.moving_up:
            if not self.ship_rect.top <= self.screen_rect.top:
                self.ship_rect.y -=3
        