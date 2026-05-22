import sys
import pygame 
import ship 
from settings import Settings
import bullet 
from alien import Alien 

class Alien_Invasion ():
    def __init__ (self):
        self.setting = Settings(self)
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
            self._update_alien()
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
        alien_height = alien.rect.height
        current_x =alien_width * 2
        current_y = alien_height * 2
        while current_y < (self.setting.screen.get_rect().height * 0.6):
            horizontal_fleet_set = False
            while not horizontal_fleet_set:
                if current_x < (self.setting.screen.get_rect().width - 2*alien_width):
                    self._create_alien(current_x , current_y)
                    current_x += alien_width * 2
                else: 
                    horizontal_fleet_set = True
                    current_x = alien_width * 2  
            current_y += alien_height

    def _create_alien(self, x_position , y_position):
        """Creates an instance of alien and adds to sprite group"""
        new_alien = Alien(self) 
        new_alien.x = x_position 
        new_alien.rect.left = x_position
        new_alien.rect.bottom = y_position
        self.aliens.add(new_alien)
   
    def _check_fleet_edges(self):
        """Takes appropriate action if any alien has reched the edge"""
        for alien in self.aliens:
            if alien.check_edge():
                self._change_fleet_direction()
                break

                
    def _change_fleet_direction(self):
        """Changes fleet direction if either edge is touched"""
        for alien in self.aliens:
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1
    
    def _update_alien (self):
        """Moves the alien to right"""
        self._check_fleet_edges()
        self.aliens.update()


    def _update_bullet(self):
        """Remove bullets on top and manage total bullets allowed"""
        self.bullets.update()
        for bullet in self.bullets.copy(): #deletes bullet after reaching top 
            if bullet.bullet_rect.y <= 0:
                self.bullets.remove(bullet)

    
    def _update_screen (self): 
        """Update the screen on each frame"""
        self.setting.screen.fill ((0,0,0))
        self.setting.screen.blit(self.setting.bg_image, self.setting.bg_image_rect)
        self.setting.screen.blit(self.ship.ship,self.ship.ship_rect)
        for bullet in self.bullets:
            bullet.draw()
        self.aliens.draw(self.setting.screen)
        pygame.display.flip() #display.update is more usefull--> can Update specified parts  

if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run()