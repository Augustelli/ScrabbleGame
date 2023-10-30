import unittest
from unittest.mock import patch

from game.modelsNew.PlayerModel import Player
from game.modelsNew.TileModel import Tile
from game.modelsNew.TileBagModel import TilesBag
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestPlayers(unittest.TestCase):

    def setUp(self):

        self.player = Player("PLAYER 1", TilesBag(tilesTesting))
        self.player2 = Player("PLAYER 2", TilesBag(tilesTesting))
        self.player.rack.tiles = [Tile("A", 1), Tile("B", 3), Tile("C", 3), Tile("D", 2), Tile("E", 1), Tile("F", 4), Tile("G", 2)]


    def test_add_tiles(self):
        self.assertEqual(len(self.player.rack.tiles), 7)
        self.player.rack.tiles = []
        self.player.addTiles()
        self.assertEqual(len(self.player.rack.tiles), 7)
        self.player.rack.tiles = [Tile("A", 1)]
        self.player.addTiles()
        self.assertEqual(len(self.player.rack.tiles), 7)

    @patch('builtins.input', side_effect=["A B C"])
    def test_exchange_valid_tiles(self, mock_input):
        initial_rack = self.player.rack.getTilesOnRack()
        initial_rack = [tile.letter for tile in initial_rack]
        self.player.exchangeTiles()
        final_rack = self.player.rack.getTilesOnRack()
        final_rack = [tile.letter for tile in final_rack]
        self.assertNotEqual(initial_rack, final_rack)
        self.assertEqual(len(final_rack), len(initial_rack))

if __name__ == '__main__':
    unittest.main()
