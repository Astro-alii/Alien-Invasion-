import pygame 
class HUD():
    def __init__(self, game ):
        self.setting = game.setting 
        self.screen = game.setting.screen 
        self.screen_rect = self.setting.screen_rect
        self.stats = game.stats

        #Font settings 
        self.text_colour =(138, 1, 255)
        self.font = pygame.font.SysFont(None ,48)

        self.prep_score()

    def prep_score(self):
        """Turn score into image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str , True, self.text_colour,(0,0,0))

        #Display score 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20 

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image , self.score_rect)
 

