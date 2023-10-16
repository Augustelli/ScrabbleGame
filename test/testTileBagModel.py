import unittest
from game.modelsNew.TileBagModel import TilesBag  # Asegúrate de importar la clase TilesBag desde tu módulo
from game.modelsNew.TileModel import Tile
from game.modelsNew.RackModel import Rack


class TestTilesBag(unittest.TestCase):

    def test_get_tiles(self):
        tiles = [Tile('B', 3), Tile('E', 1), Tile('E', 1), Tile('F', 4), Tile('G', 2), Tile('G', 2), Tile('G', 2)]
        tile_bag = TilesBag(tiles)
        tilesTaken = Rack(tile_bag)
        self.assertEqual(len(tilesTaken.tiles), 7)
        self.assertEqual(len(tile_bag.tiles), 0)
        self.assertEqual(tile_bag.getTiles(10), "No hay suficientes fichas en la bolsa")

    def test_put_tiles(self):
        tiles = ["A", "B", "C"]
        tile_bag = TilesBag(tiles)
        new_tiles = ["D", "E"]
        tile_bag.putTiles(new_tiles)
        for tile in new_tiles:
            self.assertIn(tile, tile_bag.tiles)


if __name__ == '__main__':
    unittest.main()