import pygame.font

class Scoreboard:
    """A class to present scoring info"""

    def __init__(self, rc_game):
        """Initialize scorekeeping attributes"""
        self.screen = rc_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = rc_game.settings
        self.stats = rc_game.stats

        # Font settings for scoreboard          # MOVE TO SETTINGS CLASS???
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial score image
        self.prep_score()

        # Prepare level image
        self.prep_level()

    def prep_score(self):
        """Render text into image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                    self.text_color, self.settings.bg_color)

        # Display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score & level to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)

    def prep_level(self):
        """  whatever"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, 
                    self.text_color, self.settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10