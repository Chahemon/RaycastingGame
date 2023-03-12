import pygame as pg
from settings import *

class ObjectRenderer:
    # Constructor de la clase
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    # Método para dibujar en el mapa las paredes con sus respectivos sprites.
    def draw(self):
        self.render_game_objets()

    # Renderizamos el render de los objetos.
    def render_game_objets(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    # Método para obtener la textura.
    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    # Dependiendo del muro que tenga el mapa, le asignaremos alguna textura.
    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/1.png')
        }
