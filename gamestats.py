import pygame

class Gamestats ():
    def __init__(self, game):
        self.setting = game.setting
        self.game = game
        self.reset_stats()
        
    def reset_stats(self):
        self.ship_left = self.setting.ship_limit 
        self.score = 0
        self.max_lifeline = self.game.hud.original_width
        self.lifeline = self.max_lifeline
        self.game.hud.hp_bar_reduced = pygame.transform.scale(self.game.hud.image_filled_bar, (self.max_lifeline , self.game.hud.original_height))

    def get_highest_score (self):
        self.highest_score = 0 
        with open("scores.txt" , "r") as file:
            for line in file:
                if int(line)  > self.highest_score:
                    self.highest_score = int(line)
            return str(self.highest_score)
    