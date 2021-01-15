# -*- coding: utf-8 -*-
from Scripts.tile_elements.dirt import Dirt
from Scripts.tile_elements.empty import Empty
from Scripts.tile_elements.ethan import Ethan
from Scripts.tile_elements.gem import Gem
from Scripts.tile_elements.wall import Wall
from Scripts.tile_elements.boulder import Boulder


class Map:

    def __init__(self, score):
        self.tile_map: list = []
        self.score = score

    def load(self, file_path: str):
        with open(file_path) as map_logic:
            all_lines = map_logic.readlines()
            for i, line in enumerate(all_lines):
                for j, sign in enumerate(line):
                    self.tile_map.append(list())
                    if sign == '1':
                        self.tile_map[j].append(Wall(j, i))
                    elif sign == '2':
                        self.tile_map[j].append(Dirt(j, i))
                    elif sign == 'e':
                        self.tile_map[j].append(Ethan(j, i))
                    elif sign == '3':
                        self.tile_map[j].append(Boulder(j, i))
                    elif sign == '4':
                        self.tile_map[j].append(Gem(j, i))
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
            self.swap_tiles(self.tile_map[ethan.tile_x + 1][ethan.tile_y], ethan)

            if isinstance(self.tile_map[ethan.tile_x - 1][ethan.tile_y - 1], Boulder):
                self.tile_map[ethan.tile_x - 1][ethan.tile_y - 1].start_fall(self)

            self.check_neighbours(ethan.tile_x - 1, ethan.tile_y)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_x += 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_left(self):
        ethan = self.get_ethan()
        ethan.go_left()
        if not self.tile_map[ethan.tile_x - 1][ethan.tile_y].collision(self, ethan):
            self.swap_tiles(self.tile_map[ethan.tile_x - 1][ethan.tile_y], ethan)

            if isinstance(self.tile_map[ethan.tile_x + 1][ethan.tile_y - 1], Boulder):
                self.tile_map[ethan.tile_x + 1][ethan.tile_y - 1].start_fall(self)

            self.check_neighbours(ethan.tile_x + 1, ethan.tile_y)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_x -= 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_up(self):
        ethan = self.get_ethan()
        ethan.go_up()
        if not self.tile_map[ethan.tile_x][ethan.tile_y - 1].collision(self, ethan):
            self.swap_tiles(self.tile_map[ethan.tile_x][ethan.tile_y - 1], ethan)

        self.check_neighbours(ethan.tile_x, ethan.tile_y + 1)
        # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
        # ethan.tile_y -= 1
        # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_down(self):
        ethan = self.get_ethan()
        ethan.go_down()
        if not self.tile_map[ethan.tile_x][ethan.tile_y + 1].collision(self, ethan):
            self.swap_tiles(self.tile_map[ethan.tile_x][ethan.tile_y + 1], ethan)

            if isinstance(self.tile_map[ethan.tile_x][ethan.tile_y - 2], Boulder):
                self.tile_map[ethan.tile_x][ethan.tile_y - 2].start_fall(self)

            self.check_neighbours(ethan.tile_x, ethan.tile_y - 1)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_y += 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def swap_tiles(self, tile1, tile2):
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

    def check_neighbours(self, x, y):
        if isinstance(self.tile_map[x - 1][y], Boulder):
            self.tile_map[x - 1][y].start_fall(self)
        if isinstance(self.tile_map[x + 1][y], Boulder):
            self.tile_map[x + 1][y].start_fall(self)
