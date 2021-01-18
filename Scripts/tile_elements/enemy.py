# -*- coding: utf-8 -*-
from Scripts import ENEMY_TILE
from Scripts.tile_elements.tile import Tile


class Enemy(Tile):
    """
    Class representing the enemy
    """

    def __init__(self, posx: int, posy: int):
        super().__init__()
        # self.scale = 2.0
        self.load_new_sprite(ENEMY_TILE, self.scale)
        self.tile_x = posx
        self.tile_y = posy
        self.posx = posx * self.scale * self.size[0]
        self.posy = posy * self.scale * self.size[1]
        self.step = 40
        self.direction = 0
        self.cooldown = 300

    def collision(self, map, enemy):
        return True

    def die(self):
        #mechanika śmierci
        return