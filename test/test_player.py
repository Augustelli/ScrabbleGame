import unittest
from game.models.model_player import Player
from game.models.model_tile import Tile
from game.models.model_tilebag import TilesBag
from game.models.model_board import Board
from game.models.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tiles_testing = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Augusto")
        self.tilebag = TilesBag(tiles_testing)
        self.board = Board()
        self.player.tiles = [Tile("H", 4), Tile("O", 1), Tile("L", 1), Tile("A", 1), Tile("S", 5), Tile("C", 2), Tile("B", 3)]

    def tearDown(self) -> None:
        del self.board

    def test_create_word(self):
        self.player.create_word("CASA")
        self.assertEqual(self.player.next_word, "CASA")

        self.player.create_word("")
        self.assertIsNone(self.player.next_word)

    def test_get_tiles_from_tilebag(self):
        self.player.tiles = []
        self.assertEqual(len(self.player.tiles), 0)
        self.player.get_tile_from_tilebag(self.tilebag, 7)
        self.assertEqual(len(self.player.tiles), 7)
        self.assertEqual(len(self.tilebag.tiles), 93)
        error_message = self.player.get_tile_from_tilebag(self.tilebag, 120)
        self.assertEqual(error_message, "No hay suficientes fichas en la bolsa")

    def test_get_tile_index(self):
        tile = Tile("A", 1)
        self.player.tiles.append(tile)
        self.assertEqual(self.player.get_player_tile_index("A"), 3)

    def test_get_tile_index_empty(self):
        tile = Tile("A", 1)
        self.assertEqual(self.player.get_player_tile_index(tile), None)

    def test_put_tiles_on_board_vertically(self):
        self.player.next_word = "HOLA"
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.put_tiles_on_board(0, 0, "v", self.board)
        self.assertEqual(self.player.next_word, "")
        self.assertEqual(len(self.player.tiles), 0)
        self.assertEqual(self.board.get_tile(0, 0).letter.letter, "H")
        self.assertEqual(self.board.get_tile(1, 0).letter.letter, "O")
        self.assertEqual(self.board.get_tile(2, 0).letter.letter, "L")
        self.assertEqual(self.board.get_tile(3, 0).letter.letter, "A")

    def test_put_tiles_on_board_horizontally(self):
        self.player.next_word = "HOLA"
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.put_tiles_on_board(0, 0, "h", self.board)
        self.assertEqual(self.player.next_word, "")
        self.assertEqual(len(self.player.tiles), 0)
        self.assertEqual(self.board.get_tile(0, 0).letter.letter, "H")
        self.assertEqual(self.board.get_tile(0, 1).letter.letter, "O")
        self.assertEqual(self.board.get_tile(0, 2).letter.letter, "L")
        self.assertEqual(self.board.get_tile(0, 3).letter.letter, "A")


if __name__ == '__main__':
    unittest.main()
