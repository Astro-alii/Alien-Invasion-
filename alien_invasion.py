import sys
import pygame 
import ship 
from settings import Settings
import bullet 
from alien import Alien 

class Alien_Invasion ():
    def __init__ (self):
        self.setting = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen.fill(self.setting.bg_colour)
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
        #aliens object and sprite object 
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #Fps controller
        self.clock = pygame.time.Clock()
        
    def run (self):
        """Main function to execute game flow"""
        running = True
        while running:
            self._check_event() 
            self.ship.update()    
            self._update_bullet()
            self._update_screen()
            self.clock.tick(120) # Controls frames rate per second 
    
    def _check_event (self):
        """Identify type of event"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.KEYDOWN_events(event)
                elif event.type == pygame.KEYUP:
                    self.KEYUP_events(event)


    def KEYDOWN_events(self, event):
        """Button press response"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True 
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_SPACE:
            if len(self.bullets) < self.setting.bullets_allowed:
                bullet_shot = bullet.Bullet(self)
                self.bullets.add(bullet_shot)
        if event.key == pygame.K_q:
            sys.exit()


    def KEYUP_events (self, event):
        """Button release response"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

    def _create_fleet(self):
        """Create the fleet of aliens"""
        alien = Alien (self)
        alien_width = alien.rect.width

        current_x =alien_width * 0.3
        while current_x < (self.screen.get_rect().width - 2.8*alien_width):
            new_alien = Alien(self) 
            new_alien.rect.left = current_x + alien_width
            current_x = new_alien.rect.left
            self.aliens.add(new_alien)


    def _update_bullet(self):
        """Remove bullets on top and manage total bullets allowed"""
        self.bullets.update()
        for bullet in self.bullets.copy(): #deletes bullet after reaching top 
            if bullet.bullet_rect.y <= 0:
                self.bullets.remove(bullet)

    
    def _update_screen (self):
        """Update the screen on each frame"""
        self.screen.fill (self.setting.bg_colour)
        self.screen.blit(self.ship.ship,self.ship.ship_rect)
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip() #display.update is more usefull--> can Update specified parts  

if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run()