import random
import json
from colorama import init, Fore
import pdb


with open('game/config.json', 'r') as f:
    config_data = json.load(f)

cantidad_letras = config_data['cantidad_letras']
cantidad_fichas = config_data['cantidad_letras']
cantidad_de_fichas_por_letra = config_data['cantidad_de_fichas_por_letra']
puntaje_por_letra = config_data['valores_letras']
cantidad_fichar_jugador = config_data['cantidad_fichas_jugador']
coordenadas_multiplicadores = config_data['coordenadas_multiplicadores']
colores_multiplicadores = config_data['colores_multiplicadores']
multiplicadores_valores = config_data['multiplicadores_valores']
cantidad_multiplicadores = config_data['cantidad_multiplicadores']


class Tile:
    def __init__(self, letter, value):

        self.letter = letter
        self.value = value

    def __str__(self):
        return f"{self.letter} ({self.value})"


# Creo las 100 fichas con sus respectivos puntajes, las especificaciones vienen dadas por el archivo config.json
tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class Cell:

    def __init__(self, multiplier, multiplier_type):

        self.multiplier = multiplier
        self.multiplier_type = multiplier_type  # word / letter
        self.letter = None  # Instancia de Tile

    def add_letter(self, letter):
        self.letter = letter

    def calculate_value(self):
        # Calcula el valor por letra
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value


# Crear las celdas con los multiplicadores de config.json

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


class Board():
    # La secuencia seria imprimir el tablero luego de haber hecho todas las acciones
    def __init__(self):
        self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
        init(autoreset=True)
        for tipo, valores in coordenadas_multiplicadores.items():
            for i, j in valores:
                if i == 7 and j == 7:
                    continue
                self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])
        self.board[7][7] = Cell(1, "word")

    def get_tile(self, row, column):
        return self.board[row][column]

    def add_tile(self, tile, row, column):
        if isinstance(self.board[row][column], Tile):
            return "Celda ocupada"
        else:
            self.board[row][column] = tile

    def remove_tile(self, row, column):
        if (self.board[row][column].letter is not None):
            self.board[row][column].letter = None
        else:
            return "No hay ficha en la celda"
