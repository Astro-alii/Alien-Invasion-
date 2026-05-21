import pygame 
from pygame.sprite import Sprite 
class Bullet (Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.setting
        self.bullet_colour = self.settings.bullet_colour
         
        self.bullet_rect = pygame.Rect(0, 0 , self.settings.bullet_width , 
                                       self.settings.bullet_height)
        self.bullet_rect.midtop = game.ship.ship_rect.midtop

        self.bullet_y = float (self.bullet_rect.y) # Use to adjust bullet speed - increment or decrement

    def update (self):
        self.bullet_y -= self.settings.bullet_speed 
        self.bullet_rect.y = self.bullet_y
    # draw_bullet method is required because Bullet object is not an image 
    def draw_bullet (self):
        pygame.draw.rect(self.screen, self.settings.bullet_colour ,self.bullet_rect)
    


