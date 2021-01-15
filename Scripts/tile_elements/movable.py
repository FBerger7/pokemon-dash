# -*- coding: utf-8 -*-
import threading
from datetime import time

import pygame

from Scripts.tile_elements.empty import Empty
from Scripts.tile_elements.ethan import Ethan
from Scripts.tile_elements.tile import Tile


class Movable(Tile):

    def __init__(self):
        super().__init__()


    def collision(self, map, ethan):
        # direction = self.tile_x - ethan.tile_x
        # if direction != 0 and isinstance(map.tile_map[self.tile_x + direction][self.tile_y], Empty):
        #     map.swap_tiles(map.tile_map[self.tile_x + direction][self.tile_y], self)
        #     self.start_fall(map)
        #     return False
        # else:
        return True

    def start_fall(self, map):
        self.fall_thread = threading.Thread(target=self.fall, args=(map,))
        x = map.tile_map[self.tile_x][self.tile_y - 1]
        if isinstance(x, Movable):
            x.start_fall(map=map)
        x = map.tile_map[self.tile_x - 1][self.tile_y - 1]
        if isinstance(x, Movable):
            x.start_fall(map=map)
            x = map.tile_map[self.tile_x + 1][self.tile_y - 1]
        if isinstance(x, Movable):
            x.start_fall(map=map)
        if self.fall_thread is not None:
            self.fall_thread.start()

    def fall(self, map):
        i = 0
        while True:
            loop, x, y = self.can_fall(map)
            if not loop:
                break
            if x >= 0 or y >= 0:
                map.swap_tiles(map.tile_map[x][y], self)
                i += 1
            pygame.time.wait(80)
        self.fall_thread = None
        if isinstance(map.tile_map[self.tile_x][self.tile_y + 1], Ethan) and i > 1:
            map.tile_map[self.tile_x][self.tile_y + 1].die()
        return

    def can_fall(self, map):
        # fall
        if isinstance(map.tile_map[self.tile_x][self.tile_y + 1], Empty):
            return True, self.tile_x, self.tile_y + 1
        # slip
        elif isinstance(map.tile_map[self.tile_x][self.tile_y + 1], Movable):

            # waiting for other Movables
            if map.tile_map[self.tile_x][self.tile_y + 1].fall_thread is not None:
                return True, -1, -1

            # left
            elif isinstance(map.tile_map[self.tile_x - 1][self.tile_y], Empty) and isinstance(
                    map.tile_map[self.tile_x - 1][self.tile_y + 1], Empty):
                return True, self.tile_x - 1, self.tile_y + 1
            # waiting for other Movables
            elif isinstance(map.tile_map[self.tile_x - 1][self.tile_y + 1], Movable) and map.tile_map[self.tile_x - 1][
                self.tile_y + 1].fall_thread is not None:
                return True, -1, -1
            # right
            elif isinstance(map.tile_map[self.tile_x + 1][self.tile_y], Empty) and isinstance(
                    map.tile_map[self.tile_x + 1][self.tile_y + 1], Empty):
                return True, self.tile_x + 1, self.tile_y + 1
            # waiting for other Movables
            elif isinstance(map.tile_map[self.tile_x + 1][self.tile_y + 1], Movable) and map.tile_map[self.tile_x + 1][
                self.tile_y + 1].fall_thread is not None:
                return True, -1, -1

        return False, -1, -1
