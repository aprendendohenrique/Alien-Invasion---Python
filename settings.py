class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Game settings
        self.framerate = 60

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

    def initialize_easy_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2
        self.bullet_speed = 7
        self.alien_speed = 1.0
        self.speedup_scale = 1.15

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def initialize_medium_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.75
        self.bullet_speed = 6
        self.alien_speed = 1.0
        self.speedup_scale = 1.3

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def initialize_hard_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 5
        self.alien_speed = 1.1
        self.speedup_scale = 1.4

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= 1.02
        self.alien_speed *= self.speedup_scale