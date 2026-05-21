import sys
import pygame 
import ship 
from settings import Settings
import bullet 

class Alien_Invasion ():
    def __init__ (self):
        self.setting = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.setting.width = self.screen.get_rect().width
        self.setting.height = self.screen.get_rect().height 

    

        self.screen.fill(self.setting.bg_colour)
        pygame.display.set_caption ("Alien Invasion")
        icon = pygame.image.load ("Images/alien.png")
        pygame.display.set_icon(icon)
        #Ship object 
        self.ship = ship.Ship(self)
        #bullet SPRITE GROUP object 
        self.bullets = pygame.sprite.Group()
        #Fps controller
        self.clock = pygame.time.Clock()
        
    def run (self):
        running = True
        while running:
            self._check_event() 
            self.ship.update()    
            self.bullets.update()    
            self._update_screen()
            self.clock.tick(120) # Controls frames rate per second 
    
    def _check_event (self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    self.KEYDOWN_events(event)
                
                elif event.type == pygame.KEYUP:
                    self.KEYUP_events(event)


    def KEYDOWN_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True 
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_SPACE:
            bullet_shot = bullet.Bullet(self)
            self.bullets.add(bullet_shot)
        if event.key == pygame.K_q:
            sys.exit()

    def KEYUP_events (self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
    


    def _update_screen (self):
        self.screen.fill ((0,0,0))
        self.screen.blit(self.ship.ship,self.ship.ship_rect)
        for bullet in self.bullets:
            bullet.draw_bullet()
        pygame.display.flip() #display.update is more usefull--> can Update specified parts  

if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run()