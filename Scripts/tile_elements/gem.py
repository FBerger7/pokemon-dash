# -*- coding: utf-8 -*-

from Scripts import GEM_TILE
from Scripts.tile_elements.empty import Empty
from Scripts.tile_elements.movable import Movable


class Gem(Movable):

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.load_new_sprite(GEM_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]
        self.fall_thread = None

    def collision(self, map, ethan):
        map.tile_map[self.tile_x][self.tile_y] = Empty(self.tile_x, self.tile_y)
        map.score.increment()
        return False
