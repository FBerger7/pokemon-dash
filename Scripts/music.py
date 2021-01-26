import os
from enum import Enum

import pygame

from Scripts import MUSIC_START_1_ASSET, MUSIC_START_2_ASSET, MUSIC_START_3_ASSET, MUSIC_END_ASSET, MUSIC_START_4_ASSET, \
    MUSIC_START_5_ASSET, MUSIC_VICTORY_ASSET


class Music(Enum):
    MUSIC_START_1 = MUSIC_START_1_ASSET
    MUSIC_START_2 = MUSIC_START_2_ASSET
    MUSIC_START_3 = MUSIC_START_3_ASSET
    MUSIC_START_4 = MUSIC_START_4_ASSET
    MUSIC_START_5 = MUSIC_START_5_ASSET
    MUSIC_END = MUSIC_END_ASSET
    MUSIC_VICTORY = MUSIC_VICTORY_ASSET

    @staticmethod
    def list():
        return list(map(lambda c: c.value, Music))

    @staticmethod
    def play(music_path: str):
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(0)

