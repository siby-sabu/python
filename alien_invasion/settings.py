class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (100,100,100)
        
        self.ships_left = 0

        #Bullet settings
       
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60,60,60)
        self.bullets_allowed = 3
        self.bullet_count = 50


        self.drop_speed = 10
        self.fleet_direction = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dymanic_settings()

    def initialize_dymanic_settings(self):
        self.alien_speed = .5
        self.ship_speed = 1
        self.bullet_speed = 3.0
        self.bullet_count = 100
        self.alien_points = 50

    def increase_speed(self):
        self.alien_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.bullet_count *= self.bullet_count
        self.alien_points = int(self.alien_points * self.score_scale)
