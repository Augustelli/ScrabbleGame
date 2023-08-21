import random
import json


with open('game/config.json', 'r') as f:
    config_data = json.load(f)

cantidad_letras = config_data['cantidad_letras']
cantidad_fichas = config_data['cantidad_letras']
cantidad_de_fichas_por_letra = config_data['cantidad_de_fichas_por_letra']
puntaje_por_letra = config_data['valores_letras']
cantidad_fichar_jugador = config_data['cantidad_fichas_jugador']
coordenadas_multiplicadores = config_data['coordenadas_multiplicadores']
colores_multiplicadores = config_data['colores_multiplicadores']
multiplicadores = config_data['multiplicadores']


class Tile:
    def __init__(self, letter, value):

        self.letter = letter
        self.value = value

    def __str__(self):
        return f"{self.letter} ({self.value})"


# Creo las 100 fichas con sus respectivos puntajes, las especificaciones vienen dadas por el archivo config.json
tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


# Administrar las fichas disponibles para los jugadores
# Da fichas a los jugadores y recibe fichar para intercambiar por otras
class TilesBag:
    def __init__(self, tiles):
        self.tiles = list(tiles)
        random.shuffle(self.tiles)

    def take(self, count):
        tiles_taken = []
        if count <= len(self.tiles):
            for _ in range(count):
                tiles_taken.append(self.tiles.pop())
        else:
            return "No hay suficientes fichas en la bolsa"  # Debe ser un raise
        return tiles_taken

    def put(self, tiles):
        self.tiles.extend(tiles)
        random.shuffle(self.tiles)
