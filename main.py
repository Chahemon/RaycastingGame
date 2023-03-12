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

    # Constructor de la clase Game
    def __init__(self):
        # Inicializamos el pygame, asignamos la pantalla con la resolución, y configuramos el tiempo
        # Creamos el juego
        pg.init()
        self.screen = pg.display.set_mode(REAL_RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    # Metodo para crear los objetos que necesitatemos en el juego, como el jugador, el mapa, el algoritmo,
    # el raycasting (proyeccion en 3D), el objeto a buscar, etc.
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self, pos = self.rand_pos())
        self.pathfinding = PathFinding(self)

    # Metodo que actualiza las instancias del juego, para poder ver en tiempo real todas las modificaciones en pantalla.
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.static_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    # Metodo para dibujar en pantalla todos los objetos, cada objeto tiene su metodo draw implementado en su clase.
    def draw(self):
        self.screen.fill('black')
        self.object_renderer.draw()
        self.map.draw()
        self.player.draw()
        self.static_sprite.draw()

    # Metodo para cerrar el juego.
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    # Metodo para checar la colisión de muros.
    def check_wall(self, x, y):
        return (x, y) not in self.map.world_map

    # Metodo para elegir una posicion valida al azar en el mapa.
    def rand_pos(self):
        x = random.randrange(1, 10)
        y = random.randrange(1, 10)
        while not self.check_wall(x, y):
            x = random.randrange(1, 10)
            y = random.randrange(1, 10)
        return x+0.5, y+0.5

    # Metodo que corre un ciclo infinito donde se ejecutara el juego.
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            # Si llegamos al objetivo, reiniciamos el juego.
            if round(self.player.x, 1) == self.static_sprite.x and round(self.player.y, 1) == self.static_sprite.y:
                self.new_game()
                #self.map.change_map()
                #self.pathfinding = PathFinding(self)
                self.player.x, self.player.y = self.rand_pos()
                self.static_sprite.x, self.static_sprite.y = self.rand_pos()

# Main para ejecutar el juego.
if __name__ == '__main__':
    game = Game()
    game.run()
