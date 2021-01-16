# -*- coding: utf-8 -*-
from Scripts import ENEMY_TILE
from Scripts.tile_elements.tile import Tile


class Enemy(Tile):
    """
    Class representing the enemy
    """

    def __init__(self, posx: int, posy: int):
        super().__init__()
        self.scale = 2.0
        self.load_new_sprite(ENEMY_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * 20 + 5
        self.posy = posy * self.scale * 20 - 2
        self.step = 40

    def collision(self, map, ethan):
        return True

    def die(self):
        #mechanika śmierci
        return