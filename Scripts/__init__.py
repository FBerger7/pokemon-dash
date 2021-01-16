# -*- coding: utf-8 -*-
import os

from config import PROJECT_ROOT

ETHAN_SPRITE_SHEET = os.path.join(PROJECT_ROOT, 'Assets/EthanSpritesheet.png')
BACKGROUND_SPRITE_SHEET = os.path.join(PROJECT_ROOT, 'Assets/bg_sprites.png')

# Maps
MAP1 = os.path.join(PROJECT_ROOT, 'Assets/map.txt')

# Backgrounds
DOOR_TILE = os.path.join(PROJECT_ROOT, 'Assets/door.png')
DIRT_TILE = os.path.join(PROJECT_ROOT, 'Assets/dirt.png')
EMPTY_TILE = os.path.join(PROJECT_ROOT, 'Assets/empty.png')
BOULDER_TILE = os.path.join(PROJECT_ROOT, 'Assets/boulder.png')
GEM_TILE = os.path.join(PROJECT_ROOT, 'Assets/gem.png')

# Right idle and animation
ETHAN_RIGHT = os.path.join(PROJECT_ROOT, 'Assets/ethan_right.png')
ETHAN_W1_RIGHT = os.path.join(PROJECT_ROOT, 'Assets/ethan_w1_right.png')
ETHAN_W2_RIGHT = os.path.join(PROJECT_ROOT, 'Assets/ethan_w2_right.png')

# Left idle and animation
ETHAN_LEFT = os.path.join(PROJECT_ROOT, 'Assets/ethan_left.png')

# Up idle and animation
ETHAN_UP = os.path.join(PROJECT_ROOT, 'Assets/ethan_up.png')

# Down idle and animation
ETHAN_STANDING = os.path.join(PROJECT_ROOT, 'Assets/ethan_standing.png')

# Enemy sprites
ENEMY_TILE = os.path.join(PROJECT_ROOT, 'Assets/enemy.png')

# Music and sounds
MUSIC_START_1_ASSET = os.path.join(PROJECT_ROOT, 'Music/start_1.mp3')
MUSIC_START_2_ASSET = os.path.join(PROJECT_ROOT, 'Music/start_2.mp3')
MUSIC_START_3_ASSET = os.path.join(PROJECT_ROOT, 'Music/start_3.mp3')
MUSIC_END_ASSET = os.path.join(PROJECT_ROOT, 'Music/ending.mp3')
DIG_SOUND_ASSET = os.path.join(PROJECT_ROOT, 'Music/player_dig.mp3')
MOVE_SOUND_ASSET = os.path.join(PROJECT_ROOT, 'Music/player_move.mp3')
GEM_SOUND_ASSET = os.path.join(PROJECT_ROOT, 'Music/collect_gem.mp3')
BOULDER_SOUND_ASSET = os.path.join(PROJECT_ROOT, 'Music/boulder.mp3')

# Fonts
DEFAULT_FONT = os.path.join(PROJECT_ROOT, 'Assets/default_game_font.ttf')
