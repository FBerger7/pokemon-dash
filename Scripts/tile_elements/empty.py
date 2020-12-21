# -*- coding: utf-8 -*-
from Scripts import EMPTY_TILE
from Scripts.tile_elements.tile import Tile


class Empty(Tile):

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.load_new_sprite(EMPTY_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]
        self.collision = False
