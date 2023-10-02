from game.models.model_tilebag import TilesBag
from game.models.model_board import Board
from game.models.model_player import Player
from game.models.model_tile import Tile
from game.models.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
from .validate_word import validate_word_on_rae


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
                    break
        elif orientation == "v":
            for i in range(word_length):
                cell = self.board.board[x + i][y]
                if cell.letter is not None:
                    possible_word += cell.letter.letter
                else:
                    break

        return possible_word

    # Verificar si el jugador puede jugar una palabra
    def can_play_word(self):
        word_to_be_played, position, orientation = self.current_player.next_play
        current_player_tiles = self.current_player.tiles.copy()
        # Palabra válida en la RAE     
        valid_word = True if validate_word_on_rae(word_to_be_played) else "Palabra no existe en la RAE"

        list_letters_in_row_column = self.board.get_letters_in_row_column(position, orientation)
        # Fichas necesarias para jugar la palabra
        list_letters_word_to_be_played = list(word_to_be_played)
        list_letters_required = [letter for letter in list_letters_in_row_column if letter not in list_letters_word_to_be_played]

        for letter_requiered in list_letters_required:
            for letter_player in current_player_tiles:
                if letter_requiered == letter_player.letter:
                    list_letters_required.remove(letter_player.letter)
                    break
        if list_letters_required:
            return f"{self.current_player.name} no tiene las fichas necesarias para jugar la palabra {word_to_be_played}"
        # Jugar palabra en la posición.
        # Verificar si la palabra puede ser jugada en la posición
        x, y = position
        if orientation == "v":
            if y + len(word_to_be_played) <= 15:
                enough_space = all(self.board.board[x][y + i].letter is None for i in range(len(word_to_be_played)))
        elif orientation == "h":
            if x + len(word_to_be_played) <= 15:
                enough_space = all(self.board.board[x + i][y].letter is None for i in range(len(word_to_be_played)))
        else:
            enough_space = False
        if not enough_space:
            return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation}"

        multiple_words_created = self.board.get_multiplewords_by_given_word(word_to_be_played, position, orientation)
        # Verificar si las palabras multiples palabras son válidas en la RAE
        for word in multiple_words_created:
            if not validate_word_on_rae(word):
                return f"La palabra {word} no existe en la RAE"

        return valid_word and enough_space
