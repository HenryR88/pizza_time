class Settings:
    """A class to store all settings for Pizza Time"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 750
        self.screen_height = 400
        self.bg_color = (255, 252, 213)

        # Eater settings
        self.attempts_limit = 3

        # Pizza settings
        self.batch_drop_speed = 10

        # How fast the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # Calories
        self.pizza_calories = 100

    def initialize_dynamic_settings(self):
        self.eater_speed = 1
        self.pizza_speed = 1
        self.batch_direction = 1

    def increase_speed(self):
        self.eater_speed *= self.speedup_scale
        self.pizza_speed *= self.speedup_scale


