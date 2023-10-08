import unittest
from game.modelsNew.RackModel import Rack
from game.modelsNew.TileBagModel import TilesBag
from game.modelsNew.TileModel import Tile
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
import pdb


class TestRack(unittest.TestCase):  
    tiles_test = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]

    def setUp(self):

        self.tilebag = TilesBag(self.tiles_test)
        self.rack = Rack(self.tilebag)

    def test_addTiles(self):
        self.assertEqual(len(self.rack.tiles), 7)
        initial_tile_count = len(self.rack.tiles)
        new_tiles = [Tile('F', 4), Tile('G', 2)]
        self.rack.addTiles(new_tiles)
        self.assertEqual(len(self.rack.tiles), initial_tile_count + len(new_tiles))

    def test_returnTiles(self):
        word = 'BEE'
        self.rack.tiles = [Tile('B', 3), Tile('E', 1), Tile('E', 1), Tile('F', 4), Tile('G', 2)]
        initial_tile_count = len(self.rack.tiles)
        returned_tiles = self.rack.returnTiles(word)
        self.assertEqual(len(returned_tiles), len(word))
        self.assertEqual(len(self.rack.tiles), initial_tile_count - len(word))
        self.assertEqual(len(returned_tiles), 3)
        Tile1, Tile2, Tile3 = Tile('B', 3), Tile('E', 1), Tile('E', 1)
        pdb.set_trace()
        self.assertIn(returned_tiles[0].letter, Tile1.letter)
        self.assertIn(returned_tiles[1].letter, Tile2.letter)
        self.assertIn(returned_tiles[2].letter, Tile3.letter)

    def test_returnTilesMissing(self):
        word = 'BAD'
        initial_tile_count = len(self.rack.tiles)
        returned_tiles = self.rack.returnTiles(word)
        self.assertLessEqual(len(returned_tiles), len(word))
        self.assertEqual(len(self.rack.tiles), initial_tile_count - len(returned_tiles))


if __name__ == '__main__':
    unittest.main()
