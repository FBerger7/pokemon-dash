# -*- coding: utf-8 -*-

import pygame

from Scripts import MAP1
from Scripts.map import Map
from Scripts.music import Music
from Scripts.sound import Sound
from Scripts.music_player import MusicPlayer
from config import SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE, PROJECT_ROOT

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
        self.door = None
        self.map = None

        self.music_player = None

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self.map = Map().load(MAP1)
        self.ethan = self.map.get_ethan()

        # Load music and sounds
        self.music_player = MusicPlayer.get_instance()
        self.music_player.play_music(Music.MUSIC_START_1)

        # self.player_dig_sound = pygame.mixer.Sound(DIG_SOUND_ASSET)
        # self.player_move_sound = pygame.mixer.Sound(MOVE_SOUND)
        # self.gem_sound = pygame.mixer.Sound(GEM_SOUND)
        # pygame.mixer.music.play(0)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.move_delay += 1 if self.move_delay < 5 else self.move_delay
        move_allowed = self.move_delay > 4
        if keys := pygame.key.get_pressed():
            if keys[pygame.K_RIGHT] and move_allowed:
                self.map.move_ethan_right()
                print(Music.MUSIC_START_1.__class__.__name__)
                print(Music.MUSIC_START_1.value)
                # self.music_player.play(Music.MUSIC_START)
                # pygame.mixer.Sound.play(pygame.mixer.Sound(Sound.DIG_SOUND.value))
                self.music_player.play_sound(self.music_player.DIG_SOUND)
                # pygame.mixer.Sound.play('D:\PYTHON_GAME\pokemon-dash\Music/collect_gem.mp3')
                #pygame.mixer.music.stop()
                self.move_delay = 0
                move_allowed = False
            if keys[pygame.K_LEFT] and move_allowed:
                self.map.move_ethan_left()
                # pygame.mixer.Sound.play(self.player_dig_sound)
                pygame.mixer.music.stop()
                self.move_delay = 0
                move_allowed = False
            if keys[pygame.K_UP] and move_allowed:
                self.map.move_ethan_up()
                # pygame.mixer.Sound.play(self.player_dig_sound)
                pygame.mixer.music.stop()
                self.move_delay = 0
                move_allowed = False
            if keys[pygame.K_DOWN] and move_allowed:
                self.map.move_ethan_down()
                # pygame.mixer.Sound.play(self.player_dig_sound)
                pygame.mixer.music.stop()
                self.move_delay = 0

    def on_render(self):
        self._display_surf.fill(BLACK)
        for row in self.map.tile_map:
            for item in row:
                self._display_surf.blit(item.sprite, (item.posx, item.posy))

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
