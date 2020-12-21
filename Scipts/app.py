# -*- coding: utf-8 -*-

import pygame

from Scipts.ethan import Ethan
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(GAME_TITLE)

        self.ethan = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.ethan = Ethan()
        # self.all_sprites.add(self.ethan)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_RIGHT:
        #         self.ethan.go_right()
        #     if event.key == pygame.K_LEFT:
        #         self.ethan.go_left()
        #     if event.key == pygame.K_UP:
        #         self.ethan.go_up()
        #     if event.key == pygame.K_DOWN:
        #         self.ethan.go_down()

    def on_loop(self):
        keys = pygame.key.get_pressed()
        if keys:
            if keys[pygame.K_RIGHT]:
                self.ethan.go_right()
            if keys[pygame.K_LEFT]:
                self.ethan.go_left()
            if keys[pygame.K_UP]:
                self.ethan.go_up()
            if keys[pygame.K_DOWN]:
                self.ethan.go_down()

    def on_render(self):
        self._display_surf.fill(BLACK)
        self._display_surf.blit(self.ethan.sprite, (self.ethan.posx, self.ethan.posy))

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        self.on_init()

        while self._running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.flip()
        self.on_cleanup()
