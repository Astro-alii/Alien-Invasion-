import pygame 
from pygame.sprite import Sprite 
import settings
class Alien (Sprite):
    def __init__(self, game):
        super().__init__()
        self.setting = game.setting
        self.screen = game.setting.screen 
        

        self.image = pygame.image.load("Images/aliens.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
         
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        self.x = self.rect.x
    
    def update(self):
        """Updates the alien location"""
        self.x +=  self.setting.alien_speed 
        self.rect.x = self.rect.x