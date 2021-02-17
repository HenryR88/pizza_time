import pygame
from pygame.sprite import Sprite

class Pizza(Sprite):

    def __init__(self, pt_game):
        """Initialize the pizza and set its starting poistion"""
        super().__init__()
        self.screen = pt_game.screen
        self.settings = pt_game.settings

        # Load the pizza image and set tis rect attribute.
        self.image = pygame.image.load('images/pizza.bmp')
        self.rect = self.image.get_rect()

        # Start each new pizza near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the pizza's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.pizza_speed *
                   self.settings.batch_direction)
        self.rect.x = self.x






