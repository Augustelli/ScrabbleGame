import unittest
from unittest.mock import Mock
from game.models import *


tiles_testing = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestPlayer(unittest.TestCase):

    # @classmethod
    # def setUp(cls):
    #     cls.tile_bag = TilesBag(tiles_testing)

    def setUp(self):
        self.player = Player("Augusto")
        self.mock_board = Mock()

    # @classmethod
    # def tearDown(cls):
    #     cls.tile_bag = None

    # def test_get_tiles(self):
    #     self.player.get_tiles(3)
    #     self.assertEqual(len(self.player.tiles), 3)

    # def test_create_word_valid(self):
    #     valid_tiles = [Tile("H",1), Tile("O",1), Tile("L",3), Tile("A",4)]
    #     result = self.player.create_word(valid_tiles)
    #     self.assertTrue(result)

    # def test_create_word_invalid(self):
    #     invalid_tiles = [Tile("X", 10), Tile("Y",2), Tile("Z", 6)]
    #     result = self.player.create_word(invalid_tiles)
    #     self.assertEqual(result, "Palabra inválida")

    def test_put_tiles_on_board_vertical(self):
        self.player.tiles = [Tile("A",1),Tile("B",1),Tile("C",1),Tile("D",1)]
        self.player.next_word = "ABCD"

        self.player.put_tiles_on_board(0, 0, "v")

        self.assertEqual(self.player.tiles, [])
        self.assertEqual(self.player.next_word, "")
        self.mock_board.add_tile.assert_called_with(0, 0, 0)
        self.mock_board.add_tile.assert_called_with(1, 1, 0)
        self.mock_board.add_tile.assert_called_with(2, 2, 0)
        self.mock_board.add_tile.assert_called_with(3, 3, 0)

    def test_put_tiles_on_board_horizontal(self):
        self.player.tiles = [Tile("A",1),Tile("B",1),Tile("C",1),Tile("D",1)]
        self.player.next_word = "ABCD"
        self.mock_board.add_tile.side_effect = [0, 1, 2, 3]

        self.player.put_tiles_on_board(0, 0, "h")

        self.assertEqual(self.player.tiles, ["D"])
        self.assertEqual(self.player.next_word, "")
        self.mock_board.add_tile.assert_called_with(0, 0, 0)
        self.mock_board.add_tile.assert_called_with(1, 0, 1)
        self.mock_board.add_tile.assert_called_with(2, 0, 2)
        self.mock_board.add_tile.assert_called_with(3, 0, 3)