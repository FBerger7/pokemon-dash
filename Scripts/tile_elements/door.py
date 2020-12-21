# -*- coding: utf-8 -*-
from Scripts import DOOR_TILE
from Scripts.tile_elements.tile import Tile


class Door(Tile):

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.name = 'Door'
        self.load_new_sprite(DOOR_TILE, self.scale)
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]
