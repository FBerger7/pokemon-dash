# -*- coding: utf-8 -*-


from Scripts import BOULDER_TILE
from Scripts.tile_elements.empty import Empty
from Scripts.tile_elements.tile import Tile


class Boulder(Tile):

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.load_new_sprite(BOULDER_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]

    def collision(self, map, ethan):
        direction = self.tile_x - ethan.tile_x
        if direction != 0 and isinstance(map.tile_map[self.tile_x + direction][self.tile_y], Empty):
            map.swapTiles(map.tile_map[self.tile_x + direction][self.tile_y], self)
            # map.tile_map[self.tile_x][self.tile_y] = Empty(self.tile_x, self.tile_y)
            # self.tile_x += direction
            # self.posx = self.tile_x * self.scale * self.size[0]
            # map.tile_map[self.tile_x][self.tile_y] = self
            return False
        else:
            return True


