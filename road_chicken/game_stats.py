
class GameStats:
    """Track statistics for Road Chicken"""

    def __init__(self, rc_game):
        """Initialize Statistics"""
        self.settings = rc_game.settings
        self. reset_stats()
        #self.game_active = True

        # Start game in inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize dynamic statistics"""
        self.chickens_left = self.settings.chicken_lives
        self.score = 0
        self.level = 1    
