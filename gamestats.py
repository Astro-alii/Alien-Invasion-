

class Gamestats ():
    def __init__(self, game):
        self.setting = game.setting
        self.reset_stats()
        

    def reset_stats(self):
        self.ship_left = self.setting.ship_limit 
