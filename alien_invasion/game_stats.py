class GameStats:
    def __init__(self, ai):
        self.settings = ai.settings
        self.active = True
        self.reset_stats()
    
    def reset_stats(self):
        self.ships_left = self.settings.ships_left