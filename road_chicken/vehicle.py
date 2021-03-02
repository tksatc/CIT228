import pygame
from pygame.sprite import Sprite

class Vehicle(Sprite):
    """A class to manage a vehicle in traffic"""

    def __init__(self, rc_game):
        """Initialize a vehicle and set its starting position"""
        super().__init__()
        self.screen = rc_game.screen
        self.settings = rc_game.settings

        """ List of graphics to create vehicle
        images = ["road_chicken/images/hawaiian_shirt.png", "road_chicken/images/honda_fit.png", "road_chicken/images/trabant.png",
            "road_chicken/images/xmas_vw.png", "road_chicken/images.cadillac.png", "road_chicken/images/halloween.png",
            "road_chicken/images.pickup.png", "road_chicken/images.vw_van.png"]
        """
        
        # Load vehicle image and set rect attributes
        self.image = pygame.image.load("road_chicken/images/xmas_vw.png")
        self.image = pygame.transform.scale(self.image, (125, 75))
        #self.image = self.image.convert()
        self.rect = self.image.get_rect()

        # Start vehicle near top left of screen     CHANGE TO TOP RIGHT
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store vehicle's exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_left_edge(self):
        """Return True if when vehicle is at left edge of screen"""
        #screen_rect = self.screen.get_rect()
        if not self.screen.get_rect().contains(self.rect):      # DOES THIS IDENTIFY VEHICLES OFF SCREEN?
            return True

    def update(self):
        """Move the vehicle to the left"""
        self.x -= self.settings.vehicle_speed
        self.rect.x = self.x
