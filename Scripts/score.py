# -*- coding: utf-8 -*-
from timeit import default_timer as timer

import pygame.freetype

from Scripts import DEFAULT_FONT
from config import TIME_TO_PLAY


class Score:

    def __init__(self):
        self._start_time = timer()
        self._font_color = (255, 255, 255)
        self.points_for_diamond = 8
        self.score_display: int = 0
        self.time_left_display: float = TIME_TO_PLAY
        self.font = pygame.freetype.Font(DEFAULT_FONT, 24)

    def update(self, screen):
        time_elapsed = timer() - self._start_time
        self.time_left_display = self.time_left_display - time_elapsed
        self.font.render_to(screen, (15, 815), 'Time:', self._font_color)
        self.font.render_to(screen, (115, 815), str(int(self.time_left_display)), self._font_color)
        self.font.render_to(screen, (265, 815), 'Score:', self._font_color)
        self.font.render_to(screen, (400, 815), str(self.score_display), self._font_color)
        self.font.render_to(screen, (650, 815), 'Made by: Franek & Dawid & Rafal', self._font_color)


        self._start_time = timer()

    def increment(self):
        self.score_display += self.points_for_diamond

    def is_time_left(self):
        return True if self.time_left_display > 0 else False
