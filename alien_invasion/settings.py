class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (100,100,100)
        self.ship_speed = 1.5
        self.ships_left = 0

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (60,60,60)
        self.bullets_allowed = 3
        self.bullet_count = 50

        self.alien_speed = .5
        self.drop_speed = 10
        self.fleet_direction = 1
