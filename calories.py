import pygame.font
from pygame.sprite import Group

from eater import Eater

class Calories:

    def __init__(self, pt_game):
        self.pt_game = pt_game
        self.screen = pt_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = pt_game.settings
        self.stats = pt_game.stats
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_calories()
        self.prep_eaters()

    def prep_calories(self):
        calories_str = "{:,}".format(self.stats.calories)
        self.calories_image = self.font.render(calories_str, True,
                    self.text_color, self.settings.bg_color)
        self.calories_rect = self.calories_image.get_rect()
        self.calories_rect.right = self.screen_rect.right - 20
        self.calories_rect.top = 20

    def show_calories(self):
        self.screen.blit(self.calories_image, self.calories_rect)
        self.eaters.draw(self.screen)

    def prep_eaters(self):
        """Show how many attempts are left"""
        self.eaters = Group()
        for eater_number in range(self.stats.attempts_left):
            eater = Eater(self.pt_game)
            eater.rect.x = 10 + eater_number * eater.rect.width
            eater.rect.y = 10
            self.eaters.add(eater)
