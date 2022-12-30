import pygame.font
from pygame.sprite import Group
from ship          import Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game     = ai_game
        self.screen      = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings    = ai_game.settings
        self.stats       = ai_game.stats

        # Font settings for scoring information.
        self.text_color = (255, 128, 64)
        self.font       = pygame.font.SysFont('Arial', 15,
        italic = True, bold = True)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into render image."""
        rounded_score    = round(self.stats.score, -1)
        score_str        = 'Score: ' + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
            self.text_color, self.settings.bg_color)

        # Center the score at the top of the screen.
        self.score_rect       = self.score_image.get_rect()
        self.score_rect.left  = self.screen_rect.centerx + 10
        self.score_rect.top   = self.screen_rect.top

    def prep_high_score(self):
        """Turn the high score into a render image."""
        rounded_high_score    = round(self.stats.high_score, -1)
        high_score_str        = 'High Score: ' + "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True,
            self.text_color, self.settings.bg_color)

        # Display the high score at the top left of the screen.
        self.high_score_rect      = self.score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 5
        self.high_score_rect.top  = self.screen_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """Turn the level into a render image."""
        level_str        = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
            self.text_color, self.settings.bg_color)

        # Position the level."""
        self.level_rect       = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.centerx - 10
        self.level_rect.top   = self.screen_rect.top

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship            = Ship(self.ai_game)
            ship.rect.right = self.screen_rect.right - (ship_number * ship.rect.width)
            ship.rect.top   = self.screen_rect.top
            self.ships.add(ship)

    def show_score(self):
        """Draw scores, level and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)