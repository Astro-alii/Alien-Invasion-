import pygame 
class Button():
    def __init__(self, game , x, y , width , height ,label , font_colour = (255,0,0) , bg_colour = (0, 54, 255) ):
        self.screen = game.setting.screen
        self.setting = game.setting
        
        self.font_colour = font_colour
        self.bg_colour = bg_colour
        self.width = width
        self.height = height

        self.screenx = x
        self.screeny = y

        self.button_rect = pygame.Rect(self.screenx,self.screeny, self.width , self.height)

        self.label = label



    def draw(self):
        pygame.draw.rect(self.screen , self.bg_colour , self.button_rect )
        self.font = pygame.font.SysFont(None , 38)
        self.text = self.font.render(self.label,True, self.font_colour)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.button_rect.center
        self.screen.blit(self.text , self.text_rect)

    def get_clicked(self , event):
        if event.button == 1 :
            x , y = event.pos
            return self.button_rect.collidepoint(x,y)