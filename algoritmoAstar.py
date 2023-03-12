import random
from collections import deque
from heapq import *
import pygame as pg

# Clase del algoritmo A* para encontrar la ruta
class PathFinding:
    # Creamos el constructor, creando el juego, el mini mapa, y los caminos que podemos recorrer
    # Creamos la gráfica del mini mapa.
    def __init__(self, game):
        self.game = game
        self.map = game.map.mini_map_cost
        self.ways = [-1, 0], [0, -1], [1, 0], [0, 1]  # , [-1, -1], [1, -1], [1, 1], [-1, 1] EVITAR MOVIMIENTOS EN DIAGONAL
        self.graph = {}
        self.get_graph()

    # Método para determinar la heurística.
    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Método que devuelve el camino a seguir para llegar al objetivo (Ya una vez ejecutado el A*).
    def get_path(self, start, goal):
        # Usamos una variable para guardar obtener el nodo visitado.
        self.visited = self.algoritmoAstar(start, goal, self.graph)

        path = [goal]
        step = self.visited.get(goal, start)

        # Recorremos los pasos y los vamos agregando al camino a seguir (path).
        while step and step != start:
            path.append(step)
            step = self.visited[step]

        # Mostramos en pantalla la siguiente posición.
        font = pg.font.SysFont(None, 24)
        img = font.render('Sig. Pos: ' + str(path[-1]), True, "WHITE")
        self.game.screen.blit(img, (910, 300))

        # Regresamos el camino a seguir
        return path[-1]

    def algoritmoAstar(self, start, goal, graph):

        # Variables que usaremos en el algoritmo.
        queue = []
        heappush(queue, (0, start))
        visited = {start: None}
        cost_visited = {start: 0}

        # Pintamos en pantalla información.
        font = pg.font.SysFont(None, 24)
        img = font.render('Información', True, "WHITE")
        self.game.screen.blit(img, (910, 260))
        img = font.render('--------------------------------------------', True, "WHITE")
        self.game.screen.blit(img, (910, 280))

        # Ciclo que recorre la cola, donde vamos a realizar toda la logica.
        while queue:
            # Variables que almacenan el costo y nodo actual.
            cur_cost, cur_node = heappop(queue)

            # Si el nodo es igual a la meta, vaciamos la cola para salir del ciclo, y regresar los nodos visitados.
            if cur_node == goal:
                queue = []
                continue

            # Variable con los nodos disponibles a los que podemos avanzar.
            next_nodes = graph[cur_node]

            # Guardamos el costo y nodo.
            for next_node in next_nodes:
                neigh_cost, neigh_node = next_node
                new_cost = cost_visited[cur_node] + neigh_cost

                # Si el nodo no lo hemos visitado, o el nodo es mas barato.
                if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                    print(neigh_node)
                    # Aplicamos la heurística, asignamos el nuevo costo de visita
                    priority = new_cost + self.heuristic(neigh_node, goal)
                    heappush(queue, (priority, neigh_node))
                    cost_visited[neigh_node] = new_cost
                    # Agregamos el nodo al arreglo visited (los nodos y ya visitamos y son correctos).
                    visited[neigh_node] = cur_node

        return visited

    # Método para obtener los nodos a los que nos podemos mover (Que no choquen con un muro).
    def get_next_nodes(self, x, y):
        return [(self.map[y + dy][x + dx], (x + dx, y + dy)) for dx, dy in self.ways if (x + dx, y + dy)
                not in self.game.map.world_map]

    # Método que nos regresa el mapa con las posiciones validar para caminar.
    def get_graph(self):
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                # Validamos que tengamos renglón y columna (Que no sea un muro).
                if row and col:
                    self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y)


