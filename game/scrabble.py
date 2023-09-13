from game.models.model_tilebag import TilesBag
from game.models.model_board import Board
from game.models.model_player import Player
from game.models.model_tile import Tile
from game.models.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = TilesBag(tiles)
        self.players = [Player("") for _ in range(players_count)]
        self.current_player_index = 0

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]

    def end_game(self):
        return not self.bag_tiles.tiles
