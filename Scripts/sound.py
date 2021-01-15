import os
from enum import Enum

import pygame

from Scripts import DIG_SOUND_ASSET, GEM_SOUND_ASSET, MOVE_SOUND_ASSET, BOULDER_SOUND_ASSET


class Sound(Enum):
    DIG_SOUND = DIG_SOUND_ASSET
    MOVE_SOUND = MOVE_SOUND_ASSET
    GEM_SOUND = GEM_SOUND_ASSET
    BOULDER_SOUND = BOULDER_SOUND_ASSET

    @staticmethod
    def list():
        return list(map(lambda c: c.value, Sound))

    def play(self):
        pygame.mixer.Sound.play(self)
