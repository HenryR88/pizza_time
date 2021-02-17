import pygame
from pygame.sprite import Sprite


class Eater(Sprite):
    """A class to manage the eater"""

    def __init__(self, pt_game):
        """Initialize the eater and set its starting position"""
        super().__init__()
        self.screen = pt_game.screen
        self.settings = pt_game.settings
        self.screen_rect = pt_game.screen.get_rect()

        # Load the eater image and get its rect.
        self.image = pygame.image.load('images/eater.bmp')
        self.rect = self.image.get_rect()

        # Start each new eater at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the eater's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.eater_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.eater_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.eater_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.eater_speed

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the eater at its current location."""
        self. screen.blit(self.image, self.rect)

    def center_eater(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)