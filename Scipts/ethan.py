# -*- coding: utf-8 -*-
import os

import pygame

from Scipts import ETHAN_STANDING, ETHAN_RIGHT, ETHAN_LEFT, ETHAN_UP


class Ethan(pygame.sprite.Sprite):
    """
    Class representing the main character
    """

    def __init__(self):
        super().__init__()
        self.image = self._load_image(ETHAN_STANDING)
        self.size = self.image.get_size()
        self.sprite = pygame.transform.scale(self.image, (int(self.size[0] * 2.15), int(self.size[1] * 2.15)))
        self.posx = 100
        self.posy = 100
        self.step = 5

    @staticmethod
    def _load_image(file_path):
        try:
            image = pygame.image.load(file_path)
        except pygame.error as message:
            raise ValueError('Cannot load image: ', os.path.basename(file_path))

        return image

    def _load_new_sprite(self, sprite_path):
        self.image = self._load_image(sprite_path)
        self.size = self.image.get_size()
        self.sprite = pygame.transform.scale(self.image, (int(self.size[0] * 2.15), int(self.size[1] * 2.15)))

    def go_right(self):
        self._load_new_sprite(ETHAN_RIGHT)
        self.posx += self.step

    def go_left(self):
        self._load_new_sprite(ETHAN_LEFT)
        self.posx -= self.step

    def go_up(self):
        self._load_new_sprite(ETHAN_UP)
        self.posy -= self.step

    def go_down(self):
        self._load_new_sprite(ETHAN_STANDING)
        self.posy += self.step
