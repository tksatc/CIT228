import pygame
from pygame import mixer

class SoundEffects:
    """A class to manage sound files in the game"""

    def __init__(self):
        """Instantiate sound effects object"""

    def play_music(self):
        """Method to play music"""
        pygame.mixer.init()
        pygame.mixer.music.load("road_chicken/audio/background.mp3")
        pygame.mixer.music.play(-1)

    def play_audio_clip(self):
        """Method to play sound effect"""
        self.chicken_sound = pygame.mixer.Sound("road_chicken/audio/chicken_cluck.wav")
        pygame.mixer.Sound.play(self.chicken_sound)
