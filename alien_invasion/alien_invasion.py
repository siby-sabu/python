import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Class to handle alien invasion"""
    def __init__(self):
        """Initialize game, create game resources"""
        pygame.init()
        self.settings = Settings()
        
       

        #self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption("Alien Invasion")
        self.game_stats = GameStats(self)
        self.ship = Ship(self)

        
        self.bullet_count = self.settings.bullet_count

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self,"Play")
        self.scoreboard = Scoreboard(self)
    


    def run_game(self):
        """Start the main loop to run the game"""
        while True:
            self._check_events()
            if self.game_stats.active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
                self._update_screen()  

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
           
            self._check_keydown_events(event)
            self._check_keyup_events(event)
       

    def _check_keydown_events(self, event):
        if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_q:
                    sys.exit()
             
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self._check_play_button(mouse_pos)


    def _check_keyup_events(self, event):
       if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed and self.bullet_count > 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.bullet_count -= 1

                
                    

    def _update_screen(self):
        self.screen.fill(self.settings.bg_colour)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()
        if not self.game_stats.active:
            self.play_button.draw_button()
        
        pygame.display.flip()

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
         collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
         if collisions:
            for aliens in collisions.values():
                self.game_stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()
         if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.ship.update_ship_pos()
            self._reset_bullet_count()
            self.game_stats.level +=1
            self.scoreboard.prep_level()

       
    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_alien_x = available_space_x // (2 * alien_width)
        alien_height = alien.rect.height
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)


        for row_number in range (number_rows):
            for alien_number in range (available_alien_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien.rect.height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._hit_ship()
        self._check_alien_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.drop_speed
        self.settings.fleet_direction *= -1

    def _hit_ship(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -= 1
            self.scoreboard.prep_ships()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
            
            sleep(.5)
        else:
            self.game_stats.active = False
            pygame.mouse.set_visible(True)

        
    
    def _check_alien_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._hit_ship()
                break
        
    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos) and not self.game_stats.active:
            self.game_stats.active = True

            pygame.mouse.set_visible(False)

            self.game_stats.reset_stats()

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
            self.settings.initialize_dymanic_settings()

            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()


    def _reset_bullet_count(self):
        self.bullet_count = self.settings.bullet_count


    
if __name__ == '__main__' :
    ai = AlienInvasion()
    ai.run_game()
