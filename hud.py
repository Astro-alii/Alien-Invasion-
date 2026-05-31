import pygame 
class HUD():
    def __init__(self, game ):
        self.setting = game.setting 
        self.screen = game.setting.screen 
        self.screen_rect = self.setting.screen_rect
        self.game = game

        #Font settings 
        self.text_colour =(138, 1, 255)
        self.font = pygame.font.SysFont(None ,48)

        #Lifeline bar 
        #Filled bar
        self.image_filled_bar = pygame.image.load("Images/hp_filled.gif")
        self.image_filled_bar_rect = self.image_filled_bar.get_rect()
        self.original_width = self.image_filled_bar_rect.width # Equal the original lifeline
        self.original_height = self.image_filled_bar_rect.height
        self.image_filled_bar_rect.topleft = self.screen_rect.topleft

        #Empty bar
        self.image_empty_bar = pygame.image.load("Images/hp_empty.gif")
        self.image_empty_bar_rect = self.image_empty_bar.get_rect()
        self.image_empty_bar_rect.topleft = self.screen_rect.topleft
        self.image_empty_bar_rect.top += 5

        #Heart Icon
        self.image_heart_icon = pygame.image.load("Images/hp_heart.gif")
        self.image_heart_icon_rect = self.image_heart_icon.get_rect()
        self.image_heart_icon_rect.left = self.screen_rect.left + 185
        self.image_heart_icon_rect.top -= 5

    def prep_lifeline(self):
        """Prepares the lifeline bar to be displayed on screen"""
        self.hp_bar_reduced = pygame.transform.scale(self.image_filled_bar, (self.original_width , self.original_height))

    def prep_score(self):
        """Initilizes and renders score to be displayed on screen"""
        score_str = str(self.game.stats.score)
        self.score_image = self.font.render(score_str , True, self.text_colour,(0,0,0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20 
    def show_lifeline (self):
        """Displays lifeline bar on screen"""
        self.screen.blit(self.image_empty_bar , self.image_empty_bar_rect)
        self.screen.blit(self.image_filled_bar, self.image_filled_bar_rect)
        self.screen.blit(self.image_heart_icon,self.image_heart_icon_rect)
    
    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image , self.score_rect)
 
    def write_score_to_file(self):
        with open("scores.txt", "a") as file:
            file.write(str(self.game.stats.score) + "\n")


