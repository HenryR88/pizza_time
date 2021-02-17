import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from calories import Calories
from button import Button
from eater import Eater
from pizza import Pizza


class PizzaTime:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # self.screen = pygame.display.set_mode((self.settings.screen_width,
        #                                        self.settings.screen_width))

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Pizza Time!!!")
        self.stats = GameStats(self)
        self.cal = Calories(self)
        self.eater = Eater(self)
        self.pizzas = pygame.sprite.Group()
        self._create_batch()
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.eater.update()
                self._update_pizzas()

            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.cal.prep_calories()
            self.pizzas.empty()
            self._create_batch()
            self.eater.center_eater()
            self.cal.prep_eaters()
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.eater.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.eater.moving_left = True
        elif event.key == pygame.K_UP:
            self.eater.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.eater.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.eater.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.eater.moving_left = False
        elif event.key == pygame.K_UP:
            self.eater.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.eater.moving_down = False

    def _create_batch(self):
        """Create the batch of pizzas"""
        pizza = Pizza(self)
        pizza_width, pizza_height = pizza.rect.size
        available_space_x = self.settings.screen_width - (2 * pizza_width)
        number_pizzas_x = available_space_x // (2 * pizza_width)

        eater_height = self.eater.rect.height
        available_space_y = (self.settings.screen_height -
                             pizza_height - eater_height)
        number_rows = available_space_y // (2 * pizza_height)

        for row_number in range(number_rows):
            for pizza_number in range(number_pizzas_x):
                self._create_pizza(pizza_number, row_number)

    def _create_pizza(self, pizza_number, row_number):
        pizza = Pizza(self)
        pizza_width, pizza_height = pizza.rect.size
        pizza.x = pizza_width + 2 * pizza_width * pizza_number
        pizza.rect.x = pizza.x
        pizza.rect.y = pizza.rect.height + 2 *pizza.rect.height * row_number
        self.pizzas.add(pizza)

    def _check_batch_edges(self):
        for pizza in self.pizzas.sprites():
            if pizza.check_edges():
                self._change_batch_direction()
                break

    def _change_batch_direction(self):
        for pizza in self.pizzas.sprites():
            pizza.rect.y += self.settings.batch_drop_speed
        self.settings.batch_direction *= -1

    def _update_pizzas(self):
        self._check_batch_edges()
        self.pizzas.update()
        if pygame.sprite.spritecollideany(self.eater, self.pizzas):
            print("+ 100 cal")
        self._check_eater_pizza_collision()
        self._check_pizza_bottom()

    def _check_eater_pizza_collision(self):
        collisions = pygame.sprite.spritecollide(
            self.eater, self.pizzas, True)
        if collisions:
            self.stats.calories += self.settings.pizza_calories
            self.cal.prep_calories()

        if not self.pizzas:
            self.pizzas.empty()
            self._create_batch()
            self.settings.increase_speed()

    def _check_pizza_bottom(self):
        screen_rect = self.screen.get_rect()
        for pizza in self.pizzas.sprites():
            if pizza.rect.bottom >= screen_rect.bottom:
                if self.stats.attempts_left > 0:
                    self.stats.attempts_left -= 1
                    self.cal.prep_eaters()
                    self.pizzas.empty()
                    self._create_batch()
                    self.eater.center_eater()
                    sleep(0.5)
                    break
                else:
                    self.stats.game_active = False
                    pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.eater.blitme()
        self.pizzas.draw(self.screen)
        self.cal.show_calories()
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    pt = PizzaTime()
    pt.run_game()



