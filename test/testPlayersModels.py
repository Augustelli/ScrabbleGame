import unittest

from game.modelsNew.PlayerModel import Player
from game.modelsNew.TileModel import Tile
from game.modelsNew.TileBagModel import TilesBag
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestPlayers(unittest.TestCase):

    def setUp(self):

        self.player = Player("PLAYER 1", TilesBag(tilesTesting))
        self.player2 = Player("PLAYER 2", TilesBag(tilesTesting))


    def test_add_tiles(self):
        self.assertEqual(len(self.player.rack.tiles), 7)
        self.player.rack.tiles = []
        self.player.addTiles()
        self.assertEqual(len(self.player.rack.tiles), 7)
        self.player.rack.tiles = [Tile("A", 1)]
        self.player.addTiles()
        self.assertEqual(len(self.player.rack.tiles), 7)


if __name__ == '__main__':
    unittest.main()
