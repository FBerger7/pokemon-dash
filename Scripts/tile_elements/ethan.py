# -*- coding: utf-8 -*-

from Scripts import ETHAN_STANDING, ETHAN_RIGHT, ETHAN_LEFT, ETHAN_UP
from Scripts.tile_elements.tile import Tile


class Ethan(Tile):
    """
    Class representing the main character
    """

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.scale = 2.0
        self.name = 'Ethan'
        self.load_new_sprite(ETHAN_STANDING, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * 20 + 5
        self.posy = posy * self.scale * 20 - 2
        self.step = 40
        self.collision = True

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
