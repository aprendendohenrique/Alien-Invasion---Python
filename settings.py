class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Game settings
        self.framerate = 60

        # Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 5