from enum import Enum

import pygame

from Scripts.sound import Sound
from Scripts.music import Music
import random


def play_sound(sound):
    pygame.mixer.Sound.play(sound)


class MusicPlayer:
    __instance__ = None

    def __init__(self):

        self.random_number = random.randint(1,3)

        self.DIG_SOUND = pygame.mixer.Sound(Sound.DIG_SOUND.value)
        self.MOVE_SOUND = pygame.mixer.Sound(Sound.MOVE_SOUND.value)
        self.GEM_SOUND = pygame.mixer.Sound(Sound.GEM_SOUND.value)
        self.BOULDER_SOUND = pygame.mixer.Sound(Sound.BOULDER_SOUND.value)

        """ Constructor."""
        if MusicPlayer.__instance__ is None:
            MusicPlayer.__instance__ = self
        else:
            raise Exception("You cannot create another Singleton class")

        self.channel_main = pygame.mixer.Channel(0)
        self.channel_background = pygame.mixer.Channel(1)

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not MusicPlayer.__instance__:
            MusicPlayer()
        return MusicPlayer.__instance__

    def play_music_at_start(self):
        if self.random_number == 1:
            pygame.mixer.music.load(Music.MUSIC_START_1.value)
            pygame.mixer.music.play(-1)
        elif self.random_number == 2:
            pygame.mixer.music.load(Music.MUSIC_START_2.value)
            pygame.mixer.music.play(-1)
        elif self.random_number == 3:
            pygame.mixer.music.load(Music.MUSIC_START_3.value)
            pygame.mixer.music.play(-1)

    @staticmethod
    def play_music(melody: Enum):
        pygame.mixer.music.load(melody.value)
        pygame.mixer.music.play(0)

    @staticmethod
    def play_sound(sound):
        pygame.mixer.Sound.play(sound)

    @staticmethod
    def play_music_loop(melody: Enum):
        pygame.mixer.music.load(melody.value)
        pygame.mixer.music.play(-1, 0, 5000)

    @staticmethod
    def pause():
        pygame.mixer.music.pause()

    @staticmethod
    def unpause():
        pygame.mixer.music.unpause()
