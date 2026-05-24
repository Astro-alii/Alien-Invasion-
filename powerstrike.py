import pygame 
from pygame.sprite import Sprite
import settings

class Powerstrike(Sprite):
    def __init__(self , game):
        super().__init__()
        self.settings = game.setting
        
        self.image = pygame.image.load("Images/Powerstrike.png")
        self.image = pygame.transform.scale(self.image , (self.settings.ps_width, self.settings.ps_height))
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.ship_rect.midtop

    
    def update(self):
        self.rect.y -= self.settings.ps_speed
    
    def draw(self):
        self.setting.screen.blit(self.image ,self.rect)
            