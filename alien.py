import pygame 
from pygame.sprite import Sprite 

class Alien (Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen 
        self.setting = game.setting

        self.image = pygame.image.load("Images/aliens.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
         
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        self.x = self.rect.x