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
        random.shuffle(self.tiles)
        return tiles_taken

    def put(self, tiles):
        self.tiles.extend(tiles)
        random.shuffle(self.tiles)


class Board():
    # La secuencia seria imprimir el tablero luego de haber hecho todas las acciones

    def add_tile(self, tile, row, column):
        if isinstance(self.board[row][column].letter, Tile):
            return "Celda ocupada"
        else:
            self.board[row][column].letter = tile

    def __init__(self):
        self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
        init(autoreset=True)
        for tipo, valores in coordenadas_multiplicadores.items():
            for i, j in valores:
                if i == 7 and j == 7:
                    self.board[i][j].add_letter = Tile("*", 0)
                self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])

    def get_tile(self, row, column):
        return self.board[row][column]

    def remove_tile(self, row, column):
        if (self.board[row][column].letter is not None):
            self.board[row][column].letter = None
        else:
            return "No hay ficha en la celda"

    def print_board(self):
        print(Fore.GREEN + "+---------" * 15 + "+")
        for row in self.board:
            formatted_row = []
            for cell in row:
                if isinstance(cell.letter, Tile):
                    # Si hay una letra asignada a la celda
                    if cell.letter is not None:
                        if len(cell.letter.letter) == 1:
                            formatted_row.append(f"{Fore.GREEN}|   {Fore.YELLOW}{cell.letter.letter}{cell.letter.value:2d}   ")
                        else:
                            formatted_row.append(f"{Fore.GREEN}|  {Fore.YELLOW}{cell.letter.letter}{cell.letter.value:2d}   ")
                # Si hay multiplicadores
                elif cell.multiplier != 1:
                    formatted_row.append(f"{Fore.CYAN}| x{(cell.multiplier)}{(cell.multiplier_type):^6}")
                else:
                    formatted_row.append(f"{Fore.GREEN}|{Fore.WHITE:^14}")
            formatted_row.append(Fore.GREEN + "|")
            print("".join(formatted_row))
            print(Fore.GREEN + "+---------" * 15 + "+")


class Dictionary():

    def __init__(self) -> None:
        self.dictionary = set()
        with open('game/dictionary.txt', 'r') as f:
            for line in f:
                self.dictionary.add(line.strip())

    def is_valid_word(self, word):
        return word.lower() in self.dictionary


dictionary = Dictionary()


class Player:
    def __init__(self, name):
        self.tiles = []
        self.name = name
        self.points = 0
        self.next_word = ""

    def get_tile_from_tilebag(self, tilebag, count):
        tiles_recived = tilebag.take(count)
        if isinstance(tiles_recived, str):
            return tiles_recived
        else:
            self.tiles.extend(tiles_recived)

    def create_word(self, tiles):
        self.next_word = "".join(tile.letter for tile in tiles)
        if self.next_word.lower() in dictionary.dictionary:
            self.next_word = self.next_word
            return True
        else:
            return 'Palabra inválida'

    def get_player_tile_index(self, letter):
        for tile in self.tiles:
            if letter == tile.letter:
                return self.tiles.index(tile)
        return None

    def put_tiles_on_board(self, row, column, direction, board):
        if direction == "v":
            for i, letter in enumerate(self.next_word):
                tile_index = self.get_player_tile_index(letter.upper())
                tile_to_add = self.tiles[tile_index]
                board.add_tile(tile_to_add, row + i, column)
                self.tiles.pop(tile_index)
        elif direction == "h":
            for i, letter in enumerate(self.next_word):
                tile_index = self.get_player_tile_index(letter.upper())
                tile_to_add = self.tiles[tile_index]
                board.add_tile(tile_to_add, row, column + i)
                self.tiles.pop(tile_index)
        self.next_word = ""

    def calculate_word_value(self, word):
        value = 0
        for letter in word:
            for tile in self.tiles:
                if tile.letter == letter:
                    value += tile.value
                    break
        return value

