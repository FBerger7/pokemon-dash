# -*- coding: utf-8 -*-
from Scripts import DOOR_OPEN_TILE, DOOR_CLOSED_TILE
from Scripts.tile_elements.tile import Tile


class Door(Tile):

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.name = 'Door'
        self._door_sprites = [DOOR_OPEN_TILE, DOOR_CLOSED_TILE]
        self._sprite_iter = 0
        self.load_new_sprite(DOOR_CLOSED_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]

    def collision(self, map, ethan):
        map.game_won = True
        return False

    def change_sprite(self):
        self.load_new_sprite(self._door_sprites[self._sprite_iter % len(self._door_sprites)], self.scale)
        self._sprite_iter += 1
