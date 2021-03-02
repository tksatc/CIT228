class Settings:
    """A class to store all settings for Road Chicken"""

    def __init__(self):
        """Initialize game's static settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (206, 211, 212)

        # Chicken Settings
        self.chicken_speed = 1.5
        self.chicken_lives = 5

        # Vehicle Settings
        self.vehicle_speed = 0.5

        # Speed increase on successive levels
        self.speedup_scale = 1.1

        # Point value increases on successive levels
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Intitalize settings that change throughout the game"""
        self.chicken_speed = 1.5
        self.vehicle_speed = 0.5

        # Scoring
        self.chicken_points = 100

        # Traffic Direction of 1 for right, down; -1 for left, up       # DOES THIS EVEN MAKE SENSE HERE?
        self.fleet_direction = 1

    def increase_speed(self):
        """Increases speed and point values on level-up"""
        self.chicken_speed *= self.speedup_scale
        self.vehicle_speed *= self.speedup_scale
        self.chicken_points = int(self.chicken_points * self.score_scale)
