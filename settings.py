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
        # How quickly the alien point values increase
        self.score_scale = 1.5

    def initialize_easy_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3
        self.bullet_speed = 7
        self.alien_speed = 1.2
        self.speedup_scale = 1.15
        self.score_scale = 1.1

        # Scoring settings
        self.alien_points = 35

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def initialize_medium_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3.2
        self.bullet_speed = 8
        self.alien_speed = 1.4
        self.speedup_scale = 1.3
        self.score_scale = 1.3

        # Scoring settings
        self.alien_points = 40

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def initialize_hard_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 4
        self.bullet_speed = 10
        self.alien_speed = 1.6
        self.speedup_scale = 1.4
        self.score_scale = 1.5

        # Scoring settings
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= 1.02
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)