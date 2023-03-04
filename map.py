import pygame as pg

_ = False

mini_map_list =  [[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, _, _, _, _, _, _, 1, _, 1],
    [1, 1, 1, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, _, _, 1, 1, 1, 1, 1, 1, _, 1],
    [1, _, _, _, _, _, 1, _, _, 1, _, 1],
    [1, _, _, _, _, _, _, _, _, 1, _, 1],
    [1, _, _, 1, _, _, _, _, _, 1, _, 1],
    [1, _, 1, 1, _, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, _, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
], [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, _, _, _, _, _, _, 1, _, 1],
    [1, _, 1, _, _, _, _, _, 1, 1, _, 1],
    [1, _, 1, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, 1, 1, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, 1, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, _, 1],
    [1, _, 1, _, _, _, _, _, _, 1, _, 1],
    [1, 1, 1, 1, 1, 1, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, 1, 1, _, 1],
    [1, _, _, _, _, _, _, _, 1, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, _, _, _, _, 1, _, _, 1, _, 1],
    [1, 1, 1, 1, _, _, _, _, 1, 1, _, 1],
    [1, _, 1, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, 1, 1, 1, 1, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, 1],
    [1, _, 1, 1, _, _, _, _, 1, 1, 1, 1],
    [1, _, 1, _, _, _, _, _, _, 1, _, 1],
    [1, 1, 1, 1, 1, 1, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, 1, 1, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]]

mini_map_cost = [[
    [_, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, 2, 2, 2, 2, 2, 2, _, 2, _],
    [_, _, _, 2, 2, 2, 2, 2, 2, _, 2, _],
    [_, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _],
    [_, _, 2, 2, _, _, _, _, _, _, 2, _],
    [_, 2, 2, 2, 2, 2, _, 2, 2, _, 2, _],
    [_, 2, 2, 2, 2, 2, 2, 2, 2, _, 2, _],
    [_, 2, 2, _, 2, 2, 2, 2, 2, _, 2, _],
    [_, 2, _, _, 2, 2, 2, 2, 2, 2, 2, _],
    [_, 2, 2, _, 2, 2, 2, 2, 2, _, _, _],
    [_, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, _],
    [_, _, _, _, _, _, _, _, _, _, _, _],
], [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, _, _, _, _, _, _, 1, _, 1],
    [1, _, 1, _, _, _, _, _, 1, 1, _, 1],
    [1, _, 1, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, 1, 1, 1, 1, 1, _, _, 1],
    [1, _, _, _, _, 1, 1, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, 1, 1, _, 1],
    [1, _, 1, _, _, _, _, _, _, 1, _, 1],
    [1, 1, 1, 1, 1, 1, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, 1, 1, _, 1],
    [1, _, _, _, _, _, _, _, 1, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, _, _, _, _, 1, _, _, 1, _, 1],
    [1, 1, 1, 1, _, _, _, _, 1, 1, _, 1],
    [1, _, 1, _, _, 1, _, _, _, _, _, 1],
    [1, _, _, _, _, 1, 1, 1, 1, 1, _, 1],
    [1, _, _, _, _, _, 1, _, _, _, _, 1],
    [1, _, 1, 1, _, _, _, _, 1, 1, 1, 1],
    [1, _, 1, _, _, _, _, _, _, 1, _, 1],
    [1, 1, 1, 1, 1, 1, _, _, _, _, _, 1],
    [1, _, _, 1, _, _, _, _, 1, _, _, 1],
    [1, _, _, _, _, _, 1, 1, 1, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
],[
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]]

mini_map = mini_map_list[0]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        pg.draw.rect(self.game.screen, 'black', pg.Rect(900, 0, 1140, 725))
        [pg.draw.rect(self.game.screen, 'darkgray', (900 + pos[0] * 20, pos[1] * 20, 20, 20), 1)
         for pos in self.world_map]
