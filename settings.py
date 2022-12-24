class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings."""

        # Screen settings
        self.screen_width  = 600
        self.screen_height = 600
        self.bg_color      = (230, 230, 230)

        # Ship settings
        self.ship_speed = 0.5

        # Bullet settings
        self.bullet_speed    = 0.2
        self.bullet_width    = 3
        self.bullet_height   = 15
        self.bullet_color    = (255, 0, 0) # red
        self.bullets_allowed = 6