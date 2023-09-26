from .models.model_tilebag import TilesBag
from .models.model_board import Board
from .models.model_player import Player
from .models.model_tile import Tile
from .models.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
from .validate_word_on_rae.validate_word_on_rae import validate_word_on_rae
import pdb


tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = TilesBag(tiles)
        self.players = [Player("") for _ in range(players_count)]
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]

    def validate_word(self, word, location, orientation):
        valid_word = False
        enough_tiles = False
        enough_space = False

        # Validar que la palabra sea válida en la RAE
        valid_word = validate_word_on_rae(word)
        if not valid_word:

            return 'Palabra no existe en la RAE'
        # Validar que el jugador tiene las fichas necesarias
        tiles_available = self.current_player.tiles.copy()
        for letter in word:
            for i in range(len(tiles_available)):
                if tiles_available[i].letter == letter:
                    tiles_available.remove(tiles_available[i])
                    enough_tiles = True
                    break
            else:
                enough_tiles = False
                return 'Faltan tiles.'

        # Validar que la palabra entre en el tablero
        x, y = location
        if orientation == "v":
            if y + len(word) <= 15:
                enough_space = all(self.board.board[x][y + i].letter is None for i in range(len(word)))
        elif orientation == "h":
            if x + len(word) <= 15:
                enough_space = all(self.board.board[x + i][y].letter is None for i in range(len(word)))

        return valid_word and enough_tiles and enough_space

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]

    def end_game(self):
        return not self.bag_tiles.tiles

    def put_words(self, words, locations, orientations):
        if len(words) != len(locations) != len(orientations):
            return "Las listas de palabras, ubicaciones y orientaciones deben tener la misma longitud."

        for word, location, orientation in zip(words, locations, orientations):
            if self.validate_word(word, location, orientation):
                x, y = location

                if orientation == "v":
                    for i, letter in enumerate(word):
                        self.board[x][y + i].letter = letter
                elif orientation == "h":
                    for i, letter in enumerate(word):
                        self.board[x + i][y].letter = letter
            else:
                return f"La palabra '{word}' no se puede colocar en la ubicación '{location}' con la orientación '{orientation}'."

        return "Palabras colocadas con éxito."

    def get_words(self, word, location, orientation):
        x, y = location
        possible_words = []
        if orientation == "h":
            for i in range(len(word)):
                new_word = self.get_word_in_direction(word, (x + i, y), "v")
                if new_word:
                    possible_words.append(new_word)
        elif orientation == "v":
            for i in range(len(word)):
                new_word = self.get_word_in_direction(word, (x, y + i), "h")
                if new_word:
                    possible_words.append(new_word)

        return possible_words

    def get_word_in_direction(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        possible_word = ""
        if orientation == "h":
            for i in range(word_length):
                cell = self.board.board[x][y + i]
                if cell.letter is not None:
                    possible_word += cell.letter.letter
                else:
                    break  # Deja de buscar cuando no hay más letras en la dirección
        elif orientation == "v":
            for i in range(word_length):
                cell = self.board.board[x + i][y]
                if cell.letter is not None:
                    possible_word += cell.letter.letter
                else:
                    break  # Deja de buscar cuando no hay más letras en la dirección

        return possible_word
