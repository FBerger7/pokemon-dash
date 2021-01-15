# -*- coding: utf-8 -*-

import pygame

from Scripts import MAP1, MUSIC_START, DIG_SOUND, MOVE_SOUND, GEM_SOUND
from Scripts.map import Map
from Scripts.score import Score
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE

WHITE = (255, 255, 255)
BLACK = (9, 12, 41)
FPS = 60


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = SCREEN_WIDTH, SCREEN_HEIGHT
        self.clock = pygame.time.Clock()
        self.move_delay = 0
        pygame.display.set_caption(GAME_TITLE)

        self.ethan = None
        self.score = None
        self.door = None
        self.map = None

        self.player_dig_sound = None
        self.player_move_sound = None
        self.gem_sound = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.score = Score()
        self.map = Map(self.score).load(MAP1)
        self.ethan = self.map.get_ethan()


        # Load music and sounds
        pygame.mixer.music.load(MUSIC_START)
        self.player_dig_sound = pygame.mixer.Sound(DIG_SOUND)
        self.player_move_sound = pygame.mixer.Sound(MOVE_SOUND)
        self.gem_sound = pygame.mixer.Sound(GEM_SOUND)
        pygame.mixer.music.play(0)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.move_delay += 1 if self.move_delay < 5 else self.move_delay
        move_allowed = self.move_delay > 4
        if keys := pygame.key.get_pressed():
            if keys[pygame.K_RIGHT] and move_allowed:
                self.map.move_ethan_right()
                pygame.mixer.Sound.play(self.player_dig_sound)
                pygame.mixer.music.stop()
                self.move_delay = 0
                move_allowed = False
            if keys[pygame.K_LEFT] and move_allowed:
                self.map.move_ethan_left()
                pygame.mixer.Sound.play(self.player_dig_sound)
                pygame.mixer.music.stop()
                self.move_delay = 0
                move_allowed = False
            if keys[pygame.K_UP] and move_allowed:
                self.map.move_ethan_up()
                pygame.mixer.Sound.play(self.player_dig_sound)
                pygame.mixer.music.stop()
                self.move_delay = 0
                move_allowed = False
            if keys[pygame.K_DOWN] and move_allowed:
                self.map.move_ethan_down()
                pygame.mixer.Sound.play(self.player_dig_sound)
                pygame.mixer.music.stop()
                self.move_delay = 0

    def on_render(self):
        self._display_surf.fill(BLACK)
        for row in self.map.tile_map:
            for item in row:
                self._display_surf.blit(item.sprite, (item.posx, item.posy))
        self.score.update(self._display_surf)
        if not self.score.is_time_left():
            self.on_init()

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
