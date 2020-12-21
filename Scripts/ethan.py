# -*- coding: utf-8 -*-
import os

import pygame

from Scripts import ETHAN_STANDING, ETHAN_RIGHT, ETHAN_LEFT, ETHAN_UP
from Scripts.tile import Tile


class Ethan(Tile):
    """
    Class representing the main character
    """

    def __init__(self):
        super().__init__()
        self.scale = 2.0
        self.load_new_sprite(ETHAN_STANDING, self.scale)
        self.posx = 100
        self.posy = 100
        self.step = 5

    def go_right(self):
        self.load_new_sprite(ETHAN_RIGHT, self.scale)
        self.posx += self.step

    def go_left(self):
        self.load_new_sprite(ETHAN_LEFT, self.scale)
        self.posx -= self.step

    def go_up(self):
        self.load_new_sprite(ETHAN_UP, self.scale)
        self.posy -= self.step

    def go_down(self):
        self.load_new_sprite(ETHAN_STANDING, self.scale)
        self.posy += self.step
