from RackModel import Rack
import random


class Player:

    def __init__(self, name, tilebag):
        self.rack = Rack(tilebag)
        self.name = name if name is not None else f"Jugador{random.randint(0, 99):02d}"
        self.points = 0

    def __str__(self):
        # Convierte cada ficha (Tile) a cadena antes de unirlas
        rack_str = ', '.join(str(tile) for tile in self.rack.tiles)
        return f"Nombre: {self.name}\n  - Puntuación: {self.points}\n  - Rack: {rack_str}"

    def play_word(self, word):
        pass

    def exchangeTiles(tiles_to_exchange, tile_bag):
        pass

    def passTurn():
        pass

    def isRackEmpty():
        pass
