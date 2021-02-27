class Settings:
    """A class to store all settings for Road Chicken"""

    def __init__(self):
        """Initialize game's static settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Chicken Settings
        self.chicken_speed = 1.5
        self.chicken_lives = 5

        # Vehicle Settings
        self.vehicle_speed = 1.0

    def initialize_dynamic_settings(self):
        """Intitalize settings that change throughout the game"""
        self.chicken_speed = 1.5
        self.vehicle_speed = 0.5

        # Scoring
        self.lane_transfer_points = 50
        self.all_lanes_complete = 100

        # Traffic Direction of 1 for right, down; -1 for left, up       # DOES THIS EVEN MAKE SENSE HERE?
        self.fleet_direction = 1