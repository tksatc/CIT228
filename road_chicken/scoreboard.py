import pygame.font
from pygame.sprite import Group
from chicken import Chicken

class Scoreboard:
    """A class to present scoring info"""

    def __init__(self, rc_game):
        """Initialize scorekeeping attributes"""
        self.rc_game = rc_game
        self.screen = rc_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = rc_game.settings
        self.stats = rc_game.stats

        # Font settings for scoreboard
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare initial score images
        self.prep_score()
        self.prep_high_score()

        # Prepare level image           
        self.prep_level()

    def prep_score(self):
        """Render text into image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                    self.text_color, self.settings.bg_color)

        # Display score at top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Render high score image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                    self.text_color, self.settings.bg_color)

        # Center high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check for new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw score & level to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        #self.chickens.draw(self.screen)

    def prep_level(self):
        """Render level image"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, 
                    self.text_color, self.settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        