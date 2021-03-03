import pygame
from pygame.sprite import Sprite

class Chicken(Sprite):
    """A class to manage chicken attributes and behaviors"""
    
    def __init__(self, rc_game):
        """Initialize a chicken and set its starting position"""
        super().__init__()
        self.screen = rc_game.screen
        self.settings = rc_game.settings
        self.screen_rect = rc_game.screen.get_rect()

        # Load the chicken image and get its rect
        self.image = pygame.image.load("road_chicken/images/chicken-3412665_640.png")
        self.image = pygame.transform.scale(self.image, (65, 65))           
        self.rect = self.image.get_rect()

        # Start each new chicken at the bottom center position
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the chicken's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update chicken's position based on movement flags"""
        # Update chicken's x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.chicken_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.chicken_speed
        
        # Update chicken's y value
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.chicken_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y +=  self.settings.chicken_speed

        # Update rect object from self.x and self.y
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw a chicken at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_chicken(self):
        """Center chicken on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y  = float(self.rect.y)
        