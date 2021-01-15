from enum import Enum

import pygame

# from Scripts import MUSIC_START_ASSET, DIG_SOUND_ASSET, MOVE_SOUND_ASSET, GEM_SOUND_ASSET
from Scripts.music import Music
from Scripts.sound import Sound


def play_sound(sound):
    pygame.mixer.Sound.play(sound)


class MusicPlayer:
    __instance__ = None

    # DIG_SOUND = pygame.mixer.Sound(DIG_SOUND_ASSET)
    # MOVE_SOUND = pygame.mixer.Sound(MOVE_SOUND_ASSET)
    # GEM_SOUND = pygame.mixer.Sound(GEM_SOUND_ASSET)



    # crash_sound = pygame.mixer.Sound("crash.wav")
    # pygame.mixer.Sound.play(crash_sound)


    def __init__(self):

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
        # self.load_all_music()

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not MusicPlayer.__instance__:
            MusicPlayer()
        return MusicPlayer.__instance__

    # @staticmethod
    # def load_all_music():
    #     for m in Music.list():
    #         #print("Halo to ja i: " + m)
    #         pygame.mixer.music.load(m)
    #     # for s in Sound.list():
    #     #     s.value = pygame.mixer.Sound()

    @staticmethod
    def play_music(melody: Enum):
        # if isinstance(melody, Music):
        pygame.mixer.music.load(melody.value)
        pygame.mixer.music.play(0)
        # if isinstance(melody, Sound):
        #

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

