# -*- coding: utf-8 -*-
from Scripts import DIRT_TILE
from Scripts.tile_elements.tile import Tile


class Dirt(Tile):

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.load_new_sprite(DIRT_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]

    def collision(self, map, ethan):
        return False
