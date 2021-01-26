# -*- coding: utf-8 -*-
import random

from Scripts.music_player import MusicPlayer
from Scripts.tile_elements.boulder import Boulder
from Scripts.tile_elements.dirt import Dirt
from Scripts.tile_elements.door import Door
from Scripts.tile_elements.empty import Empty
from Scripts.tile_elements.enemy import Enemy
from Scripts.tile_elements.ethan import Ethan
from Scripts.tile_elements.gem import Gem
from Scripts.tile_elements.movable import Movable
from Scripts.tile_elements.wall import Wall


class Map:

    def __init__(self, score):
        self._door_anim_delay: int = 0
        self.tile_map: list = []
        self.score = score
        self.music_player = MusicPlayer.get_instance()
        self.enemies: list = []
        self.ethan_is_alive = True
        self.game_won = False
        self.door_is_present: bool = False

    def load(self, file_path: str):
        with open(file_path) as map_logic:
            all_lines = map_logic.readlines()
            for i, line in enumerate(all_lines):
                for j, sign in enumerate(line):
                    self.tile_map.append(list())
                    if sign == '0':
                        self.tile_map[j].append(Empty(j, i))
                    elif sign == '1':
                        self.tile_map[j].append(Wall(j, i))
                    elif sign == '2':
                        self.tile_map[j].append(Dirt(j, i))
                    elif sign == 'e':
                        self.tile_map[j].append(Ethan(j, i))
                    elif sign == '3':
                        self.tile_map[j].append(Boulder(j, i))
                    elif sign == '4':
                        self.tile_map[j].append(Gem(j, i))
                    elif sign == '5':
                        e = Enemy(j, i)
                        self.tile_map[j].append(e)
                        self.enemies.append(e)
                        # self.tile_map[j].append(Enemy(j, i))
                        # self.enemies.append(Enemy(j, i))
        return self

    def get_ethan(self) -> Ethan:
        for row in self.tile_map:
            for item in row:
                if item.name == 'Ethan':
                    return item
        raise ValueError('Ethan not in tilemap!')

    def move_ethan_right(self):
        ethan = self.get_ethan()
        ethan.go_right()
        if not self.tile_map[ethan.tile_x + 1][ethan.tile_y].collision(self, ethan):

            # if isinstance(self.tile_map[ethan.tile_x + 1][ethan.tile_y], Empty):
            #     self.music_player.play_sound(self.music_player.MOVE_SOUND)
            # elif isinstance(self.tile_map[ethan.tile_x + 1][ethan.tile_y], Dirt):
            #     self.music_player.play_sound(self.music_player.DIG_SOUND)

            self.swap_tiles(self.tile_map[ethan.tile_x + 1][ethan.tile_y], ethan)

            if isinstance(self.tile_map[ethan.tile_x - 1][ethan.tile_y - 1], Movable):
                self.tile_map[ethan.tile_x - 1][ethan.tile_y - 1].start_fall(self)

            self.check_neighbours(ethan.tile_x - 1, ethan.tile_y)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_x += 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_left(self):
        ethan = self.get_ethan()
        ethan.go_left()
        if not self.tile_map[ethan.tile_x - 1][ethan.tile_y].collision(self, ethan):
            self.swap_tiles(self.tile_map[ethan.tile_x - 1][ethan.tile_y], ethan)

            if isinstance(self.tile_map[ethan.tile_x + 1][ethan.tile_y - 1], Movable):
                self.tile_map[ethan.tile_x + 1][ethan.tile_y - 1].start_fall(self)

            self.check_neighbours(ethan.tile_x + 1, ethan.tile_y)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_x -= 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_up(self):
        ethan = self.get_ethan()
        ethan.go_up()
        if not self.tile_map[ethan.tile_x][ethan.tile_y - 1].collision(self, ethan):
            self.swap_tiles(self.tile_map[ethan.tile_x][ethan.tile_y - 1], ethan)

        self.check_neighbours(ethan.tile_x, ethan.tile_y + 1)
        # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
        # ethan.tile_y -= 1
        # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_ethan_down(self):
        ethan = self.get_ethan()
        ethan.go_down()
        if not self.tile_map[ethan.tile_x][ethan.tile_y + 1].collision(self, ethan):
            self.swap_tiles(self.tile_map[ethan.tile_x][ethan.tile_y + 1], ethan)

            if isinstance(self.tile_map[ethan.tile_x][ethan.tile_y - 2], Movable):
                self.tile_map[ethan.tile_x][ethan.tile_y - 2].start_fall(self)

            self.check_neighbours(ethan.tile_x, ethan.tile_y - 1)
            # self.tile_map[ethan.tile_x][ethan.tile_y] = Empty(ethan.tile_x, ethan.tile_y)
            # ethan.tile_y += 1
            # self.tile_map[ethan.tile_x][ethan.tile_y] = ethan

    def move_enemy_right(self, enemy: Enemy):
        if self.check_if_tile_ethan(enemy.tile_x + 1, enemy.tile_y) \
                or self.check_if_tile_ethan(enemy.tile_x, enemy.tile_y - 1):
            return True
        if self.check_if_tile_empty(enemy.tile_x, enemy.tile_y - 1):
            self.swap_tiles(self.tile_map[enemy.tile_x][enemy.tile_y - 1], enemy)
            enemy.direction = 0
        elif self.check_if_tile_empty(enemy.tile_x + 1, enemy.tile_y):
            self.swap_tiles(self.tile_map[enemy.tile_x + 1][enemy.tile_y], enemy)
        else:
            enemy.direction = 2
        return False

    def move_enemy_left(self, enemy: Enemy):
        if self.check_if_tile_ethan(enemy.tile_x - 1, enemy.tile_y) \
                or self.check_if_tile_ethan(enemy.tile_x, enemy.tile_y + 1):
            return True
        if self.check_if_tile_empty(enemy.tile_x, enemy.tile_y + 1):
            self.swap_tiles(self.tile_map[enemy.tile_x][enemy.tile_y + 1], enemy)
            enemy.direction = 2
        elif self.check_if_tile_empty(enemy.tile_x - 1, enemy.tile_y):
            self.swap_tiles(self.tile_map[enemy.tile_x - 1][enemy.tile_y], enemy)
        else:
            enemy.direction = 0
        return False

    def move_enemy_up(self, enemy: Enemy):
        if self.check_if_tile_ethan(enemy.tile_x, enemy.tile_y - 1) \
                or self.check_if_tile_ethan(enemy.tile_x - 1, enemy.tile_y):
            return True
        if self.check_if_tile_empty(enemy.tile_x - 1, enemy.tile_y):
            self.swap_tiles(self.tile_map[enemy.tile_x - 1][enemy.tile_y], enemy)
            enemy.direction = 3
        elif self.check_if_tile_empty(enemy.tile_x, enemy.tile_y - 1):
            self.swap_tiles(self.tile_map[enemy.tile_x][enemy.tile_y - 1], enemy)
        else:
            enemy.direction = 1
        return False

    def move_enemy_down(self, enemy: Enemy):
        if self.check_if_tile_ethan(enemy.tile_x, enemy.tile_y + 1) \
                or self.check_if_tile_ethan(enemy.tile_x + 1, enemy.tile_y):
            return True
        if self.check_if_tile_empty(enemy.tile_x + 1, enemy.tile_y):
            self.swap_tiles(self.tile_map[enemy.tile_x + 1][enemy.tile_y], enemy)
            enemy.direction = 1
        elif self.check_if_tile_empty(enemy.tile_x, enemy.tile_y + 1):
            self.swap_tiles(self.tile_map[enemy.tile_x][enemy.tile_y + 1], enemy)
        else:
            enemy.direction = 3
        return False

    def check_if_tile_ethan(self, tile_x, tile_y):
        if isinstance(self.tile_map[tile_x][tile_y], Ethan):
            return True
        return False

    def check_if_tile_empty(self, tile_x, tile_y):
        if isinstance(self.tile_map[tile_x][tile_y], Empty):
            return True
        return False

    def move_enemy_angry(self, enemy: Enemy):
        x = random.randint(0, 3)
        if x == 0:
            return self.move_enemy_up(enemy)
        elif x == 1:
            return self.move_enemy_right(enemy)
        elif x == 2:
            return self.move_enemy_down(enemy)
        elif x == 3:
            return self.move_enemy_left(enemy)

    def move_enemy(self, enemy: Enemy):
        if enemy.direction == 0:
            # enemy.direction = 1
            return self.move_enemy_up(enemy)
        elif enemy.direction == 1:
            # enemy.direction = 2
            return self.move_enemy_right(enemy)
        elif enemy.direction == 2:
            # enemy.direction = 3
            return self.move_enemy_down(enemy)
        elif enemy.direction == 3:
            # enemy.direction = 0
            return self.move_enemy_left(enemy)

    def gemization(self, x, y):
        self.create_gem(x, y)
        self.create_gem(x - 1, y - 1)
        self.create_gem(x - 1, y)
        self.create_gem(x - 1, y + 1)
        self.create_gem(x + 1, y - 1)
        self.create_gem(x + 1, y)
        self.create_gem(x + 1, y + 1)
        self.create_gem(x, y - 1)
        self.create_gem(x, y + 1)

    def create_gem(self, x, y):
        if isinstance(self.tile_map[x][y], Ethan):
            self.tile_map[x][y].die(self)
        elif not isinstance(self.tile_map[x][y], Wall):
            self.tile_map[x][y] = Gem(x, y)
            self.tile_map[x][y].start_fall(self)

    def swap_tiles(self, tile1, tile2):
        x = tile2.tile_x
        y = tile2.tile_y
        tile2.tile_x = tile1.tile_x
        tile2.tile_y = tile1.tile_y
        tile1.tile_x = x
        tile1.tile_y = y

        self.tile_map[tile2.tile_x][tile2.tile_y] = tile2
        self.tile_map[tile1.tile_x][tile1.tile_y] = tile1

        tile1.scalePos()
        tile2.scalePos()

    def check_neighbours(self, x, y):
        if isinstance(self.tile_map[x - 1][y], Movable):
            self.tile_map[x - 1][y].start_fall(self)
        if isinstance(self.tile_map[x + 1][y], Movable):
            self.tile_map[x + 1][y].start_fall(self)

    def make_door(self):
        if not self.door_is_present:
            self.tile_map[28][17] = Door(28, 17)
            self.door_is_present = True
        if self._door_anim_delay > 30 and self.door_is_present:
            self.tile_map[28][17].change_sprite()
            self._door_anim_delay = 0
        if self.door_is_present:
            self._door_anim_delay += 1
