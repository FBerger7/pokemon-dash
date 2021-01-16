# -*- coding: utf-8 -*-
import threading
from datetime import time

import pygame

from Scripts import BOULDER_TILE
from Scripts.tile_elements.empty import Empty
from Scripts.tile_elements.movable import Movable


class Boulder(Movable):

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.load_new_sprite(BOULDER_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]
        self.fall_thread = None


    def collision(self, map, ethan):
        direction = self.tile_x - ethan.tile_x
        if direction != 0 and isinstance(map.tile_map[self.tile_x + direction][self.tile_y], Empty):
            map.swap_tiles(map.tile_map[self.tile_x + direction][self.tile_y], self)
            self.start_fall(map)
            return False
        else:
            return True


