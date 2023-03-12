from settings import *
import pygame as pg
import math

class Player:

    # Constructor de la clase.
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.path = []

    def movement(self):
        # Movimiento automático para encontrar el objetivo.
        next_pos = self.game.pathfinding.get_path(self.map_pos, (self.game.static_sprite.x-0.5, self.game.static_sprite.y - 0.5))
        next_x, next_y = next_pos
        self.path.append((next_x, next_y))
        self.angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
        speed = PLAYER_SPEED/2 * self.game.delta_time

        # Pintamos en el mini mapa la siguiente casilla a ir.
        pg.draw.rect(self.game.screen, 'blue', (900 + next_x * 20, next_y * 20, 20, 20))

        # Ajustamos las variable de movimiento.
        dx = math.cos(self.angle) * speed
        dy = math.sin(self.angle) * speed

        # Si no hay un muro, avanzamos.
        self.check_wall_collision(dx, dy)

        # Ajustamos el ángulo de visión.
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        # Movimiento manual del jugador (Ya no es necesario).
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    # Verificar si hay un muro.
    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    # Método para checar las colisiones con los muros.
    def check_wall_collision(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    # Dibujamos al jugador en el mini mapa.
    def draw(self):
        for next_x, next_y in self.path:
            pg.draw.rect(self.game.screen, 'blue', (900 + next_x * 20, next_y * 20, 20, 20))

        pg.draw.circle(self.game.screen, 'green', (900 + self.x * 20, self.y * 20), 5)

    # Actualizamos el movimiento del jugador.
    def update(self):
        self.movement()

    # Posición en el mapa exacta (decimal).
    @property
    def pos(self):
        return self.x, self.y

    # Nos da la posición en el mapa del jugador (entera).
    @property
    def map_pos(self):
        return int(self.x), int(self.y)