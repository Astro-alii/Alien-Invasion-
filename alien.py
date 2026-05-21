import pygame 
from pygame.sprite import Sprite 

class Alien (Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen 
        self.setting = game.setting

        self.alien = pygame.image.load("image/aliens.png")
        self.rect = self.alien.get_rect()
         
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        self.x = self.rect.x



