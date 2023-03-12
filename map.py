import random

import pygame as pg

# Crearemos una variables con el valor False, para facilitar la visualización del mini mapa.
_ = False

# Lista de los mini mapa.
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
]]

# Lista de los mini mapas pero con costos.
mini_map_cost = [[
    [_, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, 2, 2, 2, 2, 2, 2, _, 2, _],
    [_, _, _, 9, 1, 1, 1, 2, 2, _, 2, _],
    [_, 2, 9, 9, 9, 2, 1, 1, 2, 1, 1, _],
    [_, _, 9, 9, _, _, _, _, _, _, 1, _],
    [_, 2, 1, 9, 2, 2, _, 2, 2, _, 1, _],
    [_, 2, 1, 1, 1, 1, 1, 2, 1, _, 1, _],
    [_, 1, 1, _, 1, 1, 1, 1, 2, _, 1, _],
    [_, 1, _, _, 1, 5, 3, 1, 1, 1, 1, _],
    [_, 2, 2, _, 1, 1, 1, 1, 2, _, _, _],
    [_, 2, 6, 9, 6, 2, 2, 2, 1, 2, 2, _],
    [_, _, _, _, _, _, _, _, _, _, _, _],
], [
    [_, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, 1, 1, 1, 1, 1, 1, _, 1, _],
    [_, 1, _, 1, 1, 2, 2, 1, _, _, 1, _],
    [_, 1, _, 5, 1, _, 1, 1, 1, 1, 1, _],
    [_, 1, 3, 4, _, _, _, _, _, 2, 1, _],
    [_, 2, 1, 3, 1, _, _, 1, 1, 1, 1, _],
    [_, 2, 1, 1, 1, 1, 1, 1, _, _, 1, _],
    [_, 1, _, 1, 1, 3, 2, 1, 1, _, 1, _],
    [_, _, _, _, _, _, 2, 1, 5, 6, 1, _],
    [_, 1, 1, _, 1, 1, 1, 1, _, _, 1, _],
    [_, 2, 1, 1, 1, 6, 1, 1, _, 1, 1, _],
    [_, _, _, _, _, _, _, _, _, _, _, _]
]]

class Map:
    # Creamos un juego, asignamos el mini mapa y los costos
    def __init__(self, game):
        self.game = game
        num = random.randrange(0, 2)
        self.mini_map = mini_map_list[num]
        self.mini_map_cost = mini_map_cost[num]
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def change_map(self):
        num_ran = random.randrange(0, 2)
        self.mini_map = mini_map_list[num_ran]
        self.mini_map_cost = mini_map_cost[num_ran]
        self.world_map = {}
        self.get_map()

    # Dibujamos el mini mapa en las pantallas
    def draw(self):
        pg.draw.rect(self.game.screen, 'black', pg.Rect(900, 0, 1140, 725))
        [pg.draw.rect(self.game.screen, 'darkgray', (900 + pos[0] * 20, pos[1] * 20, 20, 20), 1)
         for pos in self.world_map]
