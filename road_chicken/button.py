import pygame.font

class Button:
    """Create a class to make and label a button"""

    def __init__(self, rc_game, msg):
        """Initialize button attributes"""
        self.screen = rc_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set dimensions and properties of a button
        self.width, self.height = 150, 50
        self.button_color = (52, 156, 52)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Prepare button label
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Define a button label and center on button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Create a button and add a label"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        