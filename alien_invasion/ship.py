from email.headerregistry import Group
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    """Class that controls player's ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.moving_right = False
        self.moving_left = False
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.game_stats = ai_game.game_stats

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        # self.rect.midleft = self.screen_rect.midleft

        # self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x
        # if self.moving_right and self.rect.bottom < self.screen_rect.bottom:
        #     self.y += self.settings.ship_speed
        # if self.moving_left and self.rect.top >  0:
        #     self.y -= self.settings.ship_speed
        
        # self.rect.y = self.y
    
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # self.rect.midleft = self.screen_rect.midleft
        # self.y = float(self.rect.y)
    
    def update_ship_pos(self):
        self.rect.y -= 25

 

        
