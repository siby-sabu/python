import pygame
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    def __init__(self, ai):
        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai.settings
        self.stats = ai.game_stats
        self.ai = ai

        self.font_colour = (255,0,0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        formatted_score = "{:,}".format(rounded_score)

        score_str = str(formatted_score)
        self.score_image = self.font.render(score_str, False, self.font_colour, self.settings.bg_colour)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right -20
        self.score_rect.top =  20

    def prep_highscore(self):
        rounded_highscore = round(self.stats.high_score)
        formatted_highscore = "{:,}".format(rounded_highscore)
        highscore_str = str(formatted_highscore)
        self.highscore_image = self.font.render(highscore_str, False, self.font_colour, self.settings.bg_colour)
        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.score_rect.top

    def prep_level(self):
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.font_colour, self.settings.bg_colour)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10


    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_highscore()

    def prep_ships(self):
        self.ships = Group()
        for ship in range(self.stats.ships_left):
            ship = Ship(self.ai)
            ship.rect.x= 10 + ship * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)