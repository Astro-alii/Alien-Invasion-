import sys
import pygame
import cv2
from cvzone.HandTrackingModule import HandDetector 
import ship 
from button import Button
from settings import Settings
import bullet 
from alien import Alien 
from powerstrike import Powerstrike
from gamestats import Gamestats
import gestures
from hud import HUD
from time import sleep
class Alien_Invasion ():
    def __init__ (self):
        pygame.init()
        pygame.mixer.init()
    
        # Load sound effects
        self.bullet_sound = pygame.mixer.Sound("Sounds/bullet.wav")
        self.powerstrike_sound = pygame.mixer.Sound("Sounds/powerstrike.wav")
        self.game_start_sound = pygame.mixer.Sound("Sounds/start.wav")
        self.game_over_sound = pygame.mixer.Sound("Sounds/game_over.wav")
        
        # Load background music 
        pygame.mixer.music.load("Sounds/Bg.mp3")
        pygame.mixer.music.set_volume(0.3)  # 30% volume
       
        self.setting = Settings(self)

        self.gesture = gestures.Gestures(self)
       
        #HUD display object
        self.hud = HUD (self)
        #Gamestats object 
        self.stats = Gamestats(self)
        #Button objects - Front Page 
        self.play_button = Button(self, self.setting.screen_rect.centerx - 100, self.setting.screen_rect.centery, 200, 75, "Play")
        self.quit_button = Button(self, self.setting.screen_rect.centerx - 100, self.setting.screen_rect.centery +100 , 200 , 75 , "Quit")
        #Button objects - Last page
        self.play_again_button = Button(self, self.setting.screen_rect.centerx - 100, self.setting.screen_rect.centery, 200, 75, "Play Again")
        
    
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
        #Game start - stop flags       
        self.game_start= False
        self.game_end = False  
    
        #Score save flag 
        self.score_saved = False


    def run (self):
        """Main function to execute game flow"""
        pygame.mixer.music.play(-1)
        running = True
        while running:
            self._check_event() 
            if self.game_start:
                self.gesture.camera_screen_on()    
                self._update_bullet()
                self._update_powerstrike()
                self._update_alien()
            self._update_screen()
            self.clock.tick(120) # Controls frames rate per second 


    def _check_event (self):
        """Identify type of event"""
        if not self.game_start:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._KEYDOWN_events(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.MOUSEBUTTONDOWN_events(event)
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self._KEYDOWN_events(event)
            self._shoot_bullet()
            self._shoot_powerstrike()
            self._update_movement()
    
    def _shoot_bullet(self):
        if self.gesture.index_finger_up_sensor():
            if len(self.bullets) < self.setting.bullets_allowed:
                bullet_shot = bullet.Bullet(self)
                self.bullets.add(bullet_shot)
                self.bullet_sound.play()

    def _shoot_powerstrike(self):
        if self.gesture.all_finger_up_sensor():
            if len(self.powerstrikes) < self.setting.ps_allowed:
                ps_shot = Powerstrike(self)
                self.powerstrikes.add(ps_shot)
                self.powerstrike_sound.play()
    
    def _update_movement(self):
        self.gesture.horizontal_movement_sensor()
        self.gesture.vertical_movement_sensor()

    def _create_intro_page(self):
        """Creates the Intro page for Alien Invasion"""
        self.play_button.draw()
        self.quit_button.draw()
        #Alien invasion heading 
        self.heading_alien  = pygame.font.SysFont("ariel", 150)
        self.text_alien_invasion = self.heading_alien.render("Alien Invasion", True , (0, 195, 255))
        self.setting.screen.blit(self.text_alien_invasion , (self.setting.screen_rect.centerx -350, self.setting.screen_rect.centery - 200))
        #ADD GESTURE CONTROL MODE info box here 

    def _create_end_page (self):
        """Creates the end page when player runs out of ships"""
        self.play_again_button.draw()
        self.quit_button.draw()
        #Font initialization
        self.heading_game_over = pygame.font.SysFont (None , 150)
        self.high_score = pygame.font.SysFont(None , 50)
        self.current_score = pygame.font.SysFont (None , 50)       
        self.high_score_val = pygame.font.SysFont(None , 50)
        self.current_score_val = pygame.font.SysFont(None , 50)
      
        #Text renders
        self.text_game_over = self.heading_game_over.render("Game Over!" , True , (255, 240, 0))
        self.text_current_score = self.current_score.render ("Current Score:" ,True , (255, 0, 136))
        self.text_current_score_val = self.current_score_val.render(str(self.stats.score) ,True ,(255, 255, 255))
        self.text_high_score = self.high_score.render("High Score:" , True , (255, 0, 136))
        self.text_high_score_val = self.high_score_val.render(self.stats.get_highest_score() ,True ,(255, 255, 255))
        
        #Blits
        self.setting.screen.blit(self.text_game_over ,(self.setting.screen_rect.centerx -300 , self.setting.screen_rect.centery -300))
        self.setting.screen.blit(self.text_current_score ,(self.setting.screen_rect.centerx -150 , self.setting.screen_rect.centery -150))
        self.setting.screen.blit(self.text_high_score ,(self.setting.screen_rect.centerx -150 , self.setting.screen_rect.centery -100))
        self.setting.screen.blit(self.text_current_score_val ,(self.setting.screen_rect.centerx +100 , self.setting.screen_rect.centery -150))
        self.setting.screen.blit(self.text_high_score_val ,( self.setting.screen_rect.centerx +45 , self.setting.screen_rect.centery -100 ))
    

    def _KEYDOWN_events(self, event):
        """Button press response"""
        if event.key == pygame.K_q:
            sys.exit()



    def MOUSEBUTTONDOWN_events(self,event):
        """Mouse click response"""
        if event.button == 1:
            if self.play_button.get_clicked(event) :
                self.game_start= True
                self.game_start_sound.play()
               # pygame.mouse.set_visible(False)
            if self.play_again_button.get_clicked(event):
                self.game_start = True
                self.game_end = False
                self.game_start_sound.play()
                self._initialize_game_startup()
                self.hud.prep_score()
            if self.quit_button.get_clicked(event) and not self.game_start:
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
        """Initilizes game when ship is hit"""
        if self.stats.lifeline > 25 * (self.hud.original_width / 100): 
            print (self.stats.lifeline)
            self.ship.get_damaged()
            self.hud.prep_lifeline() 

            

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.reset_ship()
            sleep(0.3)
        else: 
            self.game_start = False
            self.game_end = True
            self.game_over_sound.play()

        
    def _update_bullet(self):
        """Remove bullets on top and manage total bullets allowed"""
        self.bullets.update()
        for bullet in self.bullets.copy(): #deletes bullet after reaching top 
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self._check_alien_bullet_collision()
        if len(self.aliens) <= 0:
            self.setting.new_level_settings()
            self.score_saved = False
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
        collisions = pygame.sprite.groupcollide(self.aliens , self.bullets, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.setting.alien_points * len (aliens)
                self.hud.prep_score()
        

    def _check_alien_pw_collision(self):
        """Checks collisions between aliens and powerstrike"""
        collisions = pygame.sprite.groupcollide(self.aliens, self.powerstrikes, True , False)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.setting.alien_points * len (aliens)
                self.hud.prep_score()

    def _check_alien_ship_collision(self):
        """Checks Collisions between alien and ship"""
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            if self.setting.ship_limit > 0 :
                 self._ship_hit() 
            else:
                self.game_start= False
                self.game_end = True

    def _check_alien_bottom(self):
        """Checks weather alien has reached bottom"""
        for alien in self.aliens:
            if alien.rect.bottom >= self.setting.screen_rect.bottom and self.setting.ship_limit:
                self._ship_hit()
                break
    def _save_score(self):
        """Saves score once per game session"""
        if not self.score_saved:
                self.hud.write_score_to_file()
                self.score_saved  = True

    def _initialize_game_startup (self):
        """Initilizes game to play again"""
        self.aliens.empty()
        self.bullets.empty()
        self.powerstrikes.empty()
        self.ship.rect.midbottom = self.setting.screen_rect.midbottom
        self.stats.reset_stats()
        self.setting.initialize_settings()
    
    def _update_screen (self): 
        """Update the screen on each frame"""
        self.setting.screen.fill ((0,0,0))
        self.setting.screen.blit(self.setting.bg_image, self.setting.bg_image_rect)
        if not self.game_start and not self.game_end:
            self._create_intro_page()
        elif self.game_start and not self.game_end:
            self.setting.screen.blit(self.ship.ship,self.ship.rect)
            for bullet in self.bullets:
                bullet.draw()
            self.aliens.draw(self.setting.screen)
            for powerstrike in self.powerstrikes:
                self.setting.screen.blit(powerstrike.image , powerstrike.rect)
            self.hud.show_score()
            self.hud.show_lifeline()
        elif self.game_end and not self.game_start:
            self.gesture.close_detection()
            self._save_score()
            self._create_end_page()
        
        
        pygame.display.flip() #display.update is more usefull--> can Update specified parts  


if __name__ == "__main__":
    ai = Alien_Invasion()
    ai.run()