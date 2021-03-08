import pygame
from pygame import mixer

class SoundEffects:
    """A class to manage sound files in the game"""

    def __init__(self):
        """Instantiate sound effects object"""
        self.chicken_sound = pygame.mixer.Sound("road_chicken/audio/chicken_cluck.wav")
        pygame.mixer.Sound.set_volume(self.chicken_sound, 0.8)

        self.background_music = pygame.mixer.Sound("road_chicken/audio/background.mp3")
        pygame.mixer.Sound.set_volume(self.background_music, 0.2)

    def play_music(self):
        """Method to play music"""
        pygame.mixer.Sound.play(self.background_music, loops=-1)

    def play_audio_clip(self):
        """Method to play sound effect"""
        pygame.mixer.Sound.play(self.chicken_sound)
