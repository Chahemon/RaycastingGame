from settings import *
import pygame as pg
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        #print(self.game.pathfinding.get_path(self.map_pos, (self.game.static_sprite.x-0.5, self.game.static_sprite.y-0.5)))
        #print(self.map_pos)
        #print((self.game.static_sprite.x, self.game.static_sprite.y))

        next_pos = self.game.pathfinding.get_path(self.map_pos, (self.game.static_sprite.x-0.5, self.game.static_sprite.y-0.5))
        next_x, next_y = next_pos
        self.angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
        speed = PLAYER_SPEED/2 * self.game.delta_time

        pg.draw.rect(self.game.screen, 'blue', (900 + next_x * 20, next_y * 20, 20, 20))

        dx = math.cos(self.angle) * speed
        dy = math.sin(self.angle) * speed

        self.check_wall_collision(dx, dy)

        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
            # print(self.x, self.y)
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
            # print(self.x, self.y)
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
            # print(self.x, self.y)
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos
            # print(self.x, self.y)

        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'green', (900 + self.x * 20, self.y * 20), 5)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)