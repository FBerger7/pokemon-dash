# -*- coding: utf-8 -*-
from Scripts.tile_elements.dirt import Dirt
from Scripts.tile_elements.empty import Empty
from Scripts.tile_elements.ethan import Ethan
from Scripts.tile_elements.wall import Wall
from Scripts.tile_elements.boulder import Boulder


class Map:

    def __init__(self):
        self.tile_map: list = []

    def load(self, file_path: str):
        with open(file_path) as map_logic:
            all_lines = map_logic.readlines()
            for i, line in enumerate(all_lines):
                for j, sign in enumerate(line):
                    self.tile_map.append(list())
                    if sign == '1':
                        self.tile_map[j].append(Wall(j, i))
                    if sign == '2':
                        self.tile_map[j].append(Dirt(j, i))
                    if sign == 'e':
                        self.tile_map[j].append(Ethan(j, i))
                    if sign == '3':
                        self.tile_map[j].append(Boulder(j, i))
        return self

    def get_ethan(self) -> Ethan:
        for row in self.tile_map:
            for item in row:
                if item.name == 'Ethan':
                    return item
        raise ValueError('Ethan not in tilemap!')

    def move_ethan_right(self):
        ethan = self.get_ethan()
        ethan.go_right()
        if not self.tile_map[ethan.tile_x + 1][ethan.tile_y].collision(self, ethan):
            self.swapTiles(self.tile_map[ethan.tile_x + 1][ethan.tile_y], ethan)

            if isinstance(self.tile_map[ethan.tile_x - 1][ethan.tile_y-1], Boulder):
                self.tile_map[ethan.tile_x - 1][ethan.tile_y-1].startFall(self)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_x += 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_left(self):
        ethan = self.get_ethan()
        ethan.go_left()
        if not self.tile_map[ethan.tile_x - 1][ethan.tile_y].collision(self, ethan):
            self.swapTiles(self.tile_map[ethan.tile_x - 1][ethan.tile_y], ethan)

            if isinstance(self.tile_map[ethan.tile_x + 1][ethan.tile_y-1], Boulder):
                self.tile_map[ethan.tile_x + 1][ethan.tile_y-1].startFall(self)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_x -= 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_up(self):
        ethan = self.get_ethan()
        ethan.go_up()
        if not self.tile_map[ethan.tile_x][ethan.tile_y - 1].collision(self, ethan):
            self.swapTiles(self.tile_map[ethan.tile_x][ethan.tile_y - 1], ethan)

            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_y -= 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_down(self):
        ethan = self.get_ethan()
        ethan.go_down()
        if not self.tile_map[ethan.tile_x][ethan.tile_y + 1].collision(self, ethan):
            self.swapTiles(self.tile_map[ethan.tile_x][ethan.tile_y + 1], ethan)

            if isinstance(self.tile_map[ethan.tile_x][ethan.tile_y - 2], Boulder):
                self.tile_map[ethan.tile_x][ethan.tile_y - 2].startFall(self)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_y += 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def swapTiles(self, tile1, tile2):
        x = tile2.tile_x
        y = tile2.tile_y
        tile2.tile_x = tile1.tile_x
        tile2.tile_y = tile1.tile_y
        tile1.tile_x = x
        tile1.tile_y = y

        self.tile_map[tile2.tile_x][tile2.tile_y] = tile2
        self.tile_map[tile1.tile_x][tile1.tile_y] = tile1

        tile1.scalePos()
        tile2.scalePos()
