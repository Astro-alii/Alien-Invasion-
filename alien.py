import pygame 
from pygame.sprite import Sprite 
import settings
class Alien (Sprite):
    def __init__(self, game):
        super().__init__()
        self.setting = game.setting
        self.screen = game.setting.screen 
        self.screen_rect = game.setting.screen.get_rect()
        

        self.image = pygame.image.load("Images/alien.png")
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
         
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        self.x = self.rect.x
    
    def check_edge(self):
        """return True if either is touching"""
        return (self.rect.right  >= self.screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Updates the alien location"""
        self.x +=  self.setting.alien_speed * self.setting.fleet_direction
        self.rect.x = self.x

