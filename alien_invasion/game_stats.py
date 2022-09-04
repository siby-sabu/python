class GameStats:
    def __init__(self, ai):
        self.settings = ai.settings
        self.active = True
        self.reset_stats()
        self.score = 0
        self.high_score = 0
        self.level = 1
    
    def reset_stats(self):
        self.ships_left = self.settings.ships_left
        self.score = 0
        self.level = 1