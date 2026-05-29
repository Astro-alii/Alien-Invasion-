import pygame 
class Button():
    def __init__(self, game , x, y , width , height ,label , font_colour = (255,255,255) , bg_colour = (0, 0, 0) ):
        self.screen = game.setting.screen
        self.setting = game.setting
        
        self.font_colour = font_colour
        self.bg_colour = bg_colour
        self.width = width
        self.height = height

        self.screenx = x
        self.screeny = y

        self.rect = pygame.Rect(self.screenx,self.screeny, self.width , self.height)

        self.label = label



    def draw(self):
        pygame.draw.rect(self.screen , self.bg_colour , self.rect )
        self.font = pygame.font.SysFont(None , 38)
        self.text = self.font.render(self.label,True, self.font_colour)
        self.screen.blit(self.text , (self.rect.centerx - self.width * 0.15, self.rect.centery - self.height * 0.175))

    def get_cliked(self , event):
        if event.button == 1 :
            x , y = event.pos
            return self.rect.collidepoint(x,y)