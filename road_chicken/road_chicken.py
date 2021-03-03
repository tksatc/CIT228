import sys
from time import sleep
import pygame
import random
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from chicken import Chicken
from vehicle import Vehicle
from sound_effects import SoundEffects
from button import Button

class RoadChicken:
    """Class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game, create window, create game resources"""
        # Initialize game background settings
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()
        self.sound = SoundEffects()
        self.sound.play_music()

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

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Query event listener & process updates
            self._check_events()
            if self.stats.game_active:
                self.chicken.update()
                self._update_vehicles()
                        
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
            
            # Reset game settings
            self.settings.initialize_dynamic_settings()
            
            # Reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()

            # Remove remaining traffic
            self.vehicles.empty()

            # Create new traffic and center chicken
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
        vehicle = Vehicle(self)
        vehicle_width, vehicle_height = vehicle.rect.size
        available_lane_length = self.settings.screen_width
        
        # Calculate random number of vehicles in a lane
        space_between = random.randrange(2, 5)
        number_vehicles_lane = available_lane_length // (space_between * vehicle_width)

        # Calculate # of lanes that will fit on game screen
        chicken_height = self.chicken.rect.height
        available_space_y = (self.settings.screen_height -
                    (3 * vehicle_height) - chicken_height)
        number_lanes = available_space_y // int((1.25 * vehicle_height))

        # Populate a lane of vehicles
        for lane_number in range(number_lanes):
            
            # Create random padding
            space_around_vehicle = random.randrange(2, 7)
            
            # Create continuous random flow of vehicles in lane
            number_vehicles_lane = available_lane_length // (space_around_vehicle + vehicle_width) 

            # Add a vehicle to a lane
            for vehicle_number in range(number_vehicles_lane):
                self._create_vehicle(vehicle_number, lane_number)

    def _create_vehicle(self, vehicle_number, lane_number):
        # Create a vehicle and place it in a row
        vehicle = Vehicle(self)
        vehicle_width, vehicle_height = vehicle.rect.size
        
        # Calculate random padding for vehicle
        space_around_vehicle = (random.randrange(3, 5) * vehicle_width)
        
        # Calculate total space of vehicle (vehicle + padding)
        vehicle.x = vehicle_width + space_around_vehicle * vehicle_number
        vehicle.rect.x = vehicle.x
        vehicle.rect.y = vehicle.rect.height + int(1.25 * vehicle.rect.height) * lane_number
        self.vehicles.add(vehicle)

    def _update_vehicles(self):
        """Update position of all vehicles in traffic"""
        self.vehicles.update()

        # Remove vehicles once off screen
        for vehicle in self.vehicles.copy():
            if vehicle.rect.x <= 0:
                self.vehicles.remove(vehicle)

        # Repopulate traffic for continuous flow
        if not self.vehicles:
            self._create_traffic()

        # Check for collisions with chickens
        if pygame.sprite.spritecollideany(self.chicken, self.vehicles):
            self._chicken_hit() 

    def _chicken_hit(self):        
        # Play sound effect when a chicken is hit by a car
        self.sound.play_audio_clip()
        
        #Respond to chicken being hit by a vehicle
        if self.stats.chickens_left > 0:
            # Decrement chicken_lives & update scoreboard
            self.stats.chickens_left -= 1

            # Remove existing vehicles
            self.vehicles.empty()

            # Create new traffic & chicken
            self._create_traffic()
            self.chicken.center_chicken()       
        
            # Pause briefly for user to prepare new round
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
    
    def award_points(self):
        """Allot points when chicken reach top of traffic lanes"""
        screen_rect = self.screen.get_rect()
        if self.chicken.rect.top == screen_rect.top:
            self.stats.score += self.settings.chicken_points
            self.sb.prep_score()
            self.sb.check_high_score()

            # Remove existing traffic & repopulate
            self.vehicles.empty()
            self._create_traffic()

            # Return chicken to midbottom
            self.chicken.center_chicken()
            
            # Pause briefly for user to prepare for new level
            sleep(1.0)

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

        # If traffic empty, create new traffic
        if not self.vehicles:
            self._create_traffic()
            self.settings.increase_speed()
            
    def _update_screen(self):
        """Update images on screen & flip to new screen"""
        # Redraw screen during each loop
        self.screen.fill(self.settings.bg_color)
        self.chicken.blitme()
        self.vehicles.draw(self.screen)
        self.award_points()      
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
