# -*- coding: utf-8 -*-
from Scripts.tile_elements.dirt import Dirt
from Scripts.tile_elements.ethan import Ethan
from Scripts.tile_elements.wall import Wall


class Map:

    def __init__(self):
        self.tile_map: list = []

    def load(self, file_path: str):
        with open(file_path) as map_logic:
            all_lines = map_logic.readlines()
            for i, line in enumerate(all_lines):
                self.tile_map.append(list())
                for j, sign in enumerate(line):
                    if sign == '1':
                        self.tile_map[i].append(Wall(j, i))
                    if sign == '2':
                        self.tile_map[i].append(Dirt(j, i))
                    if sign == 'e':
                        self.tile_map[i].append(Ethan(j, i))
        return self
