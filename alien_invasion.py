import sys
import pygame 
import ship 
from button import Button
from settings import Settings
import bullet 
from alien import Alien 
from powerstrike import Powerstrike
from gamestats import Gamestats
from time import sleep
class Alien_Invasion ():
    def __init__ (self):
        pygame.init()
        self.setting = Settings(self)
        #Gamestats object 
        self.stats = Gamestats(self)
        #Button objects
        self.play_button = Button(self, self.setting.screen_rect.centerx - 100, self.setting.screen_rect.centery, 200, 75, "Play")
        self.quit_button = Button(self, self.setting.screen_rect.centerx - 100, self.setting.screen_rect.centery +100 , 200 , 75 , "Quit")
        #Score display bar
        self.score_bar = Button(self , self.setting.screen_rect.left , self.setting.screen_rect.top, 50, 25, "0", (0,255,0) ,(255,255,255))
        #font object
        self.font = pygame.font.SysFont(None, 48)
        #Ship object 
        self.ship = ship.Ship(self)
        #bullet SPRITE GROUP object 
        self.bullets = pygame.sprite.Group()
        #Powerstrike SPRITE GROUP object 
        self.powerstrikes = pygame.sprite.Group()
        #aliens object and sprite object 
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        #Fps controller
        self.clock = pygame.time.Clock()
        self.game_over = True
        self.game_lost = False

    def run (self):
        """Main function to execute game flow"""
        running = True
        while running:
            self._check_event() 
            if not self.game_over:
                self.ship.update()    
                self._update_bullet()
                self._update_powerstrike()
                self._update_alien()
            self._update_screen()
            self.clock.tick(120) # Controls frames rate per second 


    def _check_event (self):
        """Identify type of event"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.MOUSEBUTTONDOWN_events(event)
                elif event.type == pygame.KEYDOWN:
                    self.KEYDOWN_events(event)
                elif event.type == pygame.KEYUP:
                    self.KEYUP_events(event)

    def _create_intro(self):
        self.heading_alien  = pygame.font.SysFont("ariel", 150)
        self.heading_invasion = pygame.font.SysFont("ariel", 150)
        self.text_alien = self.heading_alien.render("Alien", True , (110, 0 , 217))
        self.text_invasion = self.heading_invasion.render("Invasion", True , (110, 0 ,217))
        self.setting.screen.blit(self.text_alien , (self.setting.screen_rect.centerx -125, self.setting.screen_rect.centery - 300))
        self.setting.screen.blit(self.text_invasion, (self.setting.screen_rect.centerx-200  , self.setting.screen_rect.centery -200 ))
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
        if event.key == pygame.K_z:
             if len(self.powerstrikes) < self.setting.ps_allowed:
                ps_shot = Powerstrike(self)
                self.powerstrikes.add(ps_shot)
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

    def MOUSEBUTTONDOWN_events(self,event):
        if event.button == 1:
            if self.play_button.get_cliked(event):
                self.game_over = False
               # pygame.mouse.set_visible(False)
            elif self.quit_button.get_cliked(event):
                sys.exit() 
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


    def _check_fleet_edges(self):
        """Takes appropriate action if any alien has reched the edge"""
        for alien in self.aliens:
            if alien.check_edge():
                self._change_fleet_direction()
                break


    def _create_alien(self, x_position , y_position):
        """Creates an instance of alien and adds to sprite group"""
        new_alien = Alien(self) 
        new_alien.x = x_position 
        new_alien.rect.left = x_position
        new_alien.rect.bottom = y_position
        self.aliens.add(new_alien)
   
          
    def _change_fleet_direction(self):
        """Changes fleet direction if either edge is touched"""
        for alien in self.aliens:
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1


    def _update_alien (self):
        """Moves the alien to right"""
        self._check_fleet_edges()
        self.aliens.update()
        self._check_alien_bullet_collision
        self._check_alien_ship_collision()
        self._check_alien_bottom() 


    def _ship_hit (self):
        if self.stats.ship_left > 1:
            self.stats.ship_left -= 1 

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.reset_ship()
            sleep(0.3)
        else: 
            self.game_over = True
            self.game_lost = True 
        
    def _update_bullet(self):
        """Remove bullets on top and manage total bullets allowed"""
        self.bullets.update()
        for bullet in self.bullets.copy(): #deletes bullet after reaching top 
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self._check_alien_bullet_collision()
        if len(self.aliens) <= 0:
            self._create_fleet()


    def _update_powerstrike(self):
        """Remove bullets on top and manage total bullets allowed"""
        self.powerstrikes.update()
        for powerstrike in self.powerstrikes.copy(): #deletes bullet after reaching top 
            if powerstrike.rect.y <= 0:
                self.powerstrikes.remove(powerstrike)
        self._check_alien_pw_collision()


    def _check_alien_bullet_collision(self):
        """Checks collsions between alien and fired bullet"""
        hits = len(pygame.sprite.groupcollide(self.aliens , self.bullets, True, True))
        
   

    def _check_alien_pw_collision(self):
        """Checks collisions between aliens and powerstrike"""
        pygame.sprite.groupcollide(self.aliens, self.powerstrikes, True , False)


    def _check_alien_ship_collision(self):
        """Checks Collisions between alien and ship"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            if self.setting.ship_limit > 0 :
                 self._ship_hit() 

    def _check_alien_bottom(self):
        """Checks weather alien has reached bottom"""
        for alien in self.aliens:
            if alien.rect.bottom >= self.setting.screen_rect.bottom and self.setting.ship_limit:
                self._ship_hit()
                break
            
    
    

    def _update_screen (self): 
        """Update the screen on each frame"""
        self.setting.screen.fill ((0,0,0))
        self.setting.screen.blit(self.setting.bg_image, self.setting.bg_image_rect)
        if self.game_over:
            self.play_button.draw()
            self.quit_button.draw()
            self._create_intro()
            self.aliens.empty()
            self.bullets.empty()
            self.ship.rect.midbottom = self.setting.screen_rect.midbottom
            self.stats.reset_stats()
        elif self.game_lost: # Make a complete end page, like intro page 
            self.play_again_button()
            self.you_lost_msg()
            self.display_score()
            self.display_level()
        elif not self.game_over:
            self.setting.screen.blit(self.ship.ship,self.ship.rect)
            for bullet in self.bullets:
                bullet.draw()
            self.aliens.draw(self.setting.screen)
            for powerstrike in self.powerstrikes:
                self.setting.screen.blit(powerstrike.image , powerstrike.rect)
        
        
        pygame.display.flip() #display.update is more usefull--> can Update specified parts  


if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run()