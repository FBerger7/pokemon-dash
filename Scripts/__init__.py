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

# Music and sounds
MUSIC_START = os.path.join(PROJECT_ROOT, 'Music/start.mp3')
DIG_SOUND = os.path.join(PROJECT_ROOT, 'Music/player_dig.mp3')
MOVE_SOUND = os.path.join(PROJECT_ROOT, 'Music/player_move.mp3')
GEM_SOUND = os.path.join(PROJECT_ROOT, 'Music/collect_gem.mp3')