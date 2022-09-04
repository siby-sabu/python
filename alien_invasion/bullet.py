import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai):
        super().__init__()
        self.screen = ai.screen
        # self.direction = direction
        self.settings = ai.settings
        self.colour = self.settings.bullet_colour

        self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai.ship.rect.midtop
        self.y = float(self.rect.y)
        # self.rect = pygame.Rect(0,0,self.settings.bullet_width, self.settings.bullet_height)
        # self.rect.midleft = ai.ship.rect.midleft
        # self.x = float(self.rect.x)

        
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.colour, self.rect)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        # self.x += self.settings.bullet_speed
        # self.rect.x = self.x


