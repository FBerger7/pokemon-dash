# -*- coding: utf-8 -*-
from Scripts.dirt import Dirt
from Scripts.door import Door


class Map:

    def __init__(self):
        self.tile_map = []

    def load(self, file_path: str):
        with open(file_path) as map_logic:
            all_lines = map_logic.readlines()
            for i, line in enumerate(all_lines):
                self.tile_map.append([])
                for j, sign in enumerate(line):
                    if sign == '1':
                        self.tile_map[i].append(Door(j, i))
                    if sign == '2':
                        self.tile_map[i].append(Dirt(j, i))
        return self
