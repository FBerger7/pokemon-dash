# -*- coding: utf-8 -*-
import os

import pygame
from pygame.sprite import AbstractGroup


class Tile(pygame.sprite.Sprite):

    def __init__(self, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = None
        self.size = None
        self.name = None
        self.sprite = None
        self.scale = 2.5
        self.tile_x = 0
        self.tile_y = 0
        self.posx = 0
        self.posy = 0

    @staticmethod
    def load_image(file_path: str) -> pygame.Surface:
        try:
            image = pygame.image.load(file_path)
        except pygame.error as message:
            raise ValueError('Cannot load image: ', os.path.basename(file_path))

        return image

    def load_new_sprite(self, sprite_path: str, scale: float):
        self.image = self.load_image(sprite_path)
        self.size = self.image.get_size()
        self.sprite = pygame.transform.scale(self.image, (int(self.size[0] * scale), int(self.size[1] * scale)))

    def collision(self, map, ethan):
        return False

    def scalePos(self):
        self.posx = self.tile_x * self.scale * self.size[0]
        self.posy = self.tile_y * self.scale * self.size[1]
