import pygame as pg
import sys

import settings
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from algoritmoAstar import *
import random


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(REAL_RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self, pos=self.rand_pos())
        self.pathfinding = PathFinding(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        self.map.draw()
        self.player.draw()
        self.static_sprite.draw()
        #font = pg.font.SysFont(None, 24)
        #img = font.render('hello', True, 'BLUE')
        #self.screen.blit(img, (20, 20))

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_t:
                    if self.check_wall(int(self.player.x), int(self.player.y - 1)):
                        self.player.y -= 1
                if event.key == pg.K_g:
                    if self.check_wall(int(self.player.x), int(self.player.y + 1)):
                        self.player.y += 1
                if event.key == pg.K_f:
                    if self.check_wall(int(self.player.x - 1), int(self.player.y)):
                        self.player.x -= 1
                if event.key == pg.K_h:
                    if self.check_wall(int(self.player.x + 1), int(self.player.y)):
                        self.player.x += 1

    def check_wall(self, x, y):
        return (x, y) not in self.map.world_map

    def rand_pos(self):
        x = random.randrange(1, 10)
        y = random.randrange(1, 10)
        while not self.check_wall(x, y):
            x = random.randrange(1, 10)
            y = random.randrange(1, 10)
        return x+0.5, y+0.5

    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.player.x + dx), int(self.player.y)):
            self.player.x += dx
        if self.check_wall(int(self.player.x), int(self.player.y + dy)):
            self.player.y += dy

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            if round(self.player.x, 1) == self.static_sprite.x and round(self.player.y, 1) == self.static_sprite.y:
                self.player.x, self.player.y = self.rand_pos()
                self.static_sprite.x, self.static_sprite.y = self.rand_pos()


if __name__ == '__main__':
    game = Game()
    game.run()
