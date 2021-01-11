# -*- coding: utf-8 -*-
import threading
from datetime import time

import pygame

from Scripts import BOULDER_TILE
from Scripts.tile_elements.empty import Empty
from Scripts.tile_elements.ethan import Ethan
from Scripts.tile_elements.tile import Tile


class Boulder(Tile):

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.load_new_sprite(BOULDER_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]
        self.fallThread = None

    def collision(self, map, ethan):
        direction = self.tile_x - ethan.tile_x
        if direction != 0 and isinstance(map.tile_map[self.tile_x + direction][self.tile_y], Empty):
            map.swap_tiles(map.tile_map[self.tile_x + direction][self.tile_y], self)
            # map.tile_map[self.tile_x][self.tile_y] = Empty(self.tile_x, self.tile_y)
            # self.tile_x += direction
            # self.posx = self.tile_x * self.scale * self.size[0]
            # map.tile_map[self.tile_x][self.tile_y] = self
            self.start_fall(map)
            return False
        else:
            return True

    def start_fall(self, map):
        self.fallThread = threading.Thread(target=self.fall, args=(map,))
        x = map.tile_map[self.tile_x][self.tile_y - 1]
        if isinstance(x, Boulder):
            x.start_fall(map=map)
        self.fallThread.start()

    def fall(self, map):
        i = 0
        while isinstance(map.tile_map[self.tile_x][self.tile_y + 1], Empty) or (
                isinstance(map.tile_map[self.tile_x][self.tile_y + 1], Boulder)):
            map.swap_tiles(map.tile_map[self.tile_x][self.tile_y + 1], self)
            i += 1
            pygame.time.wait(80)
            self.boulder_stack(map)
        self.fallThread = None
        if isinstance(map.tile_map[self.tile_x][self.tile_y + 1], Ethan) and i > 1:
            map.tile_map[self.tile_x][self.tile_y + 1].die()
        return

    def boulder_stack(self, map):
        if isinstance(map.tile_map[self.tile_x][self.tile_y + 1], Boulder) and map.tile_map[self.tile_x][
            self.tile_y + 1].fallThread is None and isinstance(
            map.tile_map[self.tile_x - 1][self.tile_y], Empty) and isinstance(
            map.tile_map[self.tile_x - 1][self.tile_y + 1], Empty):
            map.swap_tiles(self, map.tile_map[self.tile_x - 1][self.tile_y + 1])
        elif isinstance(map.tile_map[self.tile_x][self.tile_y + 1], Boulder) and map.tile_map[self.tile_x][
            self.tile_y + 1].fallThread is None and isinstance(
            map.tile_map[self.tile_x + 1][self.tile_y], Empty) and isinstance(
            map.tile_map[self.tile_x + 1][self.tile_y + 1], Empty):
            map.swap_tiles(self, map.tile_map[self.tile_x + 1][self.tile_y + 1])
