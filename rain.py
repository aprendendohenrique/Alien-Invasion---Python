import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A class to represent a single raindrop in the rain"""

    def __init__(self, ai_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the raindrop image and set its rect attribute.
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = 0

        # Store the raindrop's exact position.
        self.x = float(self.rect.y)
        self.start_y = float(self.rect.y)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if raindrop is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom

    def update(self):
        """Move the raindrop downwards"""
        self.y += 8
        self.rect.y = self.y

