class GameStats:

    def __init__(self, pt_game):
        self.settings = pt_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.attempts_left = self.settings.attempts_limit
        self.calories = 0
