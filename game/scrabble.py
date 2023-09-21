from game.models.model_tilebag import TilesBag
from game.models.model_board import Board
from game.models.model_player import Player
from game.models.model_tile import Tile
from game.models.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
from game.validate_word_on_rae.validate_word_on_rae import validate_word_on_rae
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
