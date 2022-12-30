class GameStats:
    """Trace statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self._prep_high_score()

    def reset_stats(self):
        """Initialize statistics that can be change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score      = 0
        self.level      = 1

    def _prep_high_score(self):
        """ 
        Get the high score value from the high_score.txt file. 
        If the file does not exist, or something went wrong,
        then set the high score to 0.
        """
        try:
            with open('high_score.txt', 'r') as file:
                self.high_score = int(file.read())
        except:
                self.high_score = 0

    def save_high_score(self):
        """Save the high score value into the file."""
        with open('high_score.txt', 'w') as file:
            file.write(str(self.high_score))

