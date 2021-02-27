import sys
from time import sleep
import pygame
import random
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from chicken import Chicken
from vehicle import Vehicle
from button import Button

class RoadChicken:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game, create window, create game resources"""
        # Initialize game background settings
        pygame.init()
        self.settings = Settings()

        # Create game window
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))
        pygame.display.set_caption("Road Chicken")

        # Instantiate statistics and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.chicken = Chicken(self)
        self.vehicles = pygame.sprite.Group()

        # Create and draw lanes of vehicles
        self._create_traffic()

        # Create a Start button
        self.start_button = Button(self, "Start")

        # Make lists available to all methods for multidimensional interating
        #self.number_lanes = 0
        #self.number_vehicles_x = 0

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Query event listener & process updates
            self._check_events()
            if self.stats.game_active:
                self.chicken.update()
                self._update_vehicles()
            
            """THIS BLOCK FOR TESTING CONTINUAL FLOW OF TRAFFIC  # NOT WORKING; DELETES ALL VEHICLES
            # Create new traffic as sprite group empties
            if self.vehicles.empty():
                self._create_traffic()
            """
            
            self._update_screen()

    def _check_events(self):
        """Event Handler"""
        for event in pygame.event.get():
            # Event handler
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_start_button(mouse_pos)

    def _check_start_button(self, mouse_pos):
        """Start a new game when player clicks Start"""
        button_clicked = self.start_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True

            # Remove remaining traffice
            self.vehicles.empty()

            # Create new traffice and center chicken
            self._create_traffic()
            self.chicken.center_chicken()
            
            # Hide cursor during play
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Keypress event handler"""
        if event.key == pygame.K_RIGHT:
            self.chicken.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.chicken.moving_left = True
        elif event.key == pygame.K_UP:
            self.chicken.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.chicken.moving_down = True
        
        # Allow player to use 'q' to end game
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Key release event handler"""
        if event.key == pygame.K_RIGHT:
            self.chicken.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.chicken.moving_left = False
        elif event.key == pygame.K_UP:
            self.chicken.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.chicken.moving_down = False

    def _create_traffic(self):
        """Create a fleet of vehicles to be traffic"""
        # Create a vehicles & find the number of vehicles in a row
        # Spacing between vehicles = width of one vehicle
        vehicle = Vehicle(self)
        vehicle_width, vehicle_height = vehicle.rect.size
        available_lane_length = self.settings.screen_width
        
        # HOW TO ADD RANDOM SPACE BETWEEN???
        #space_between = random.randrange(1, 4)

        #number_vehicles_x = available_lane_length // (space_between * vehicle_width)

        # Calculate # of lanes that will fit on game screen
        #number_lanes = self.number_lanes
        chicken_height = self.chicken.rect.height
        available_space_y = (self.settings.screen_height -
                    (2 * vehicle_height) - chicken_height)
        number_lanes = available_space_y // int((1.75 * vehicle_height))        # IN INIT

        # Populate lanes of traffic
        for lane_number in range(number_lanes):
            # ADDS VARIABLE NUMBER OF CARS IN EACH LANE
            space_between = random.randrange(1, 4)
            #number_vehicles_x = self.number_vehicles_x
            number_vehicles_x = available_lane_length // (space_between * vehicle_width)    # IN INIT 

            for vehicle_number in range(number_vehicles_x):
                self._create_vehicle(vehicle_number, lane_number)

    def _create_vehicle(self, vehicle_number, lane_number):
        # Create a vehicle and place it in a row
        vehicle = Vehicle(self)
        vehicle_width, vehicle_height = vehicle.rect.size
        vehicle.x = vehicle_width + 2 * vehicle_width * vehicle_number
        vehicle.rect.x = vehicle.x
        vehicle.rect.y = vehicle.rect.height + 2 * vehicle.rect.height * lane_number
        self.vehicles.add(vehicle)

    def _remove_offscreen_vehicle(self):
        """Delete vehicles when they move off screen on the left"""
        for vehicle in self.vehicles.sprites():
            if vehicle.check_left_edge():
                pygame.sprite.Sprite.remove(self)

    def _update_vehicles(self):
        """Update position of all vehicles in traffic"""
        # Remove vehicles that have moved off-screen, then update all vehicle positions
        #self._remove_offscreen_vehicle()
        self.vehicles.update()

        # Check for collisions with chickens
        if pygame.sprite.spritecollideany(self.chicken, self.vehicles):
            self._chicken_hit()
            print("SPLAT!")  

    def _chicken_hit(self):
        #Respond to chicken being hit by a vehicle
        if self.stats.chickens_left > 0:
            # Decrement chicken_lives
            self.stats.chickens_left -= 1

            # Remove existing vehicles
            self.vehicles.empty()

            # Create new traffic & chicken
            self._create_traffic()
            self.chicken.center_chicken()
        
            # Pause briefly for user to prepare new round
            sleep(1.0)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    

    def _update_screen(self):
        """Update images on screen & flip to new screen"""
        # Redraw screen during each loop
        self.screen.fill(self.settings.bg_color)
        self.chicken.blitme()
        self.vehicles.draw(self.screen)
        self.sb.show_score()

        # Draw Start button if game inactive
        if not self.stats.game_active:
            self.start_button.draw_button()

        # Refresh with new screen
        pygame.display.flip()

if __name__ == "__main__":
    # Make a game instance and run the game
    rc = RoadChicken()
    rc.run_game()
