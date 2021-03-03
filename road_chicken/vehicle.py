import pygame
from pygame.sprite import Sprite

class Vehicle(Sprite):
    """A class to manage a vehicle in traffic"""

    def __init__(self, rc_game):
        """Initialize a vehicle and set its starting position"""
        super().__init__()
        self.screen = rc_game.screen
        self.settings = rc_game.settings
        
        # Load vehicle image and set rect attributes
        self.image = pygame.image.load("road_chicken/images/xmas_vw.png")
        self.image = pygame.transform.scale(self.image, (125, 75))
        #self.image = self.image.convert()
        self.rect = self.image.get_rect()

        # Start vehicle near top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store vehicle's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        """Move the vehicle to the left"""
        self.x -= self.settings.vehicle_speed
        self.rect.x = self.x
