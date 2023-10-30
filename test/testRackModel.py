import unittest

from game.JugadaDTO.jugada_dto import JugadaDto
from game.modelsNew.RackModel import Rack
from game.modelsNew.TileBagModel import TilesBag
from game.modelsNew.TileModel import Tile
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
import pdb  # noqa


tiles_test = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]
class TestRack(unittest.TestCase):

    def setUp(self):

        self.tilebag = TilesBag(    tiles_test)
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
        self.assertIn(returned_tiles[0].letter, Tile1.letter)
        self.assertIn(returned_tiles[1].letter, Tile2.letter)
        self.assertIn(returned_tiles[2].letter, Tile3.letter)

    def test_returnTilesMissing(self):
        word = 'BAD'
        initial_tile_count = len(self.rack.tiles)
        returned_tiles = self.rack.returnTiles(word)
        self.assertLessEqual(len(returned_tiles), len(word))
        self.assertEqual(len(self.rack.tiles), initial_tile_count - len(returned_tiles))

    def test_getTilesOnRack(self):
        self.rack.tiles = [Tile('B', 3), Tile('E', 1), Tile('E', 1), Tile('F', 4), Tile('G', 2)]
        self.assertEqual(len(self.rack.getTilesOnRack()), 5)

    def test_isEmpy(self):
        self.assertFalse(self.rack.isEmpty())
        self.rack.tiles = []
        self.assertTrue(self.rack.isEmpty())

    def test_add_tiles_to_player(self):
        self.rack.addTileToPlayer()
        self.assertEqual(len(self.rack.tiles), 7)
        self.rack.tiles = []
        self.rack.addTileToPlayer()
        self.assertEqual(len(self.rack.tiles), 7)

    def test_change_tiles_with_valid_letters(self):
        tilebag = TilesBag([Tile('B', 1), Tile('B', 2), Tile('Z', 10), Tile('Z', 10)])
        rack = Rack(tilebag)
        rack.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3), Tile('D', 4)]
        dto_cambio = JugadaDto(cambiarFichas=True, tilesACambiar=['A', 'C'])
        result = rack.changeTiles(dto_cambio)

        self.assertNotIn('A', [tile.letter for tile in rack.tiles])
        self.assertNotIn('C', [tile.letter for tile in rack.tiles])

        self.assertTrue(result.cambiarFichas)

    def test_change_tiles_with_invalid_letters(self):
        tilebag = TilesBag([Tile('A', 1), Tile('B', 2), Tile('C', 3)])
        rack = Rack(tilebag)
        rack.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3)]
        dto_cambio = JugadaDto(cambiarFichas=True, tilesACambiar=['X'])
        result = rack.changeTiles(dto_cambio)
        self.assertEqual(['A', 'B', 'C'], [tile.letter for tile in rack.tiles])
        self.assertTrue(result.cambiarFichas)

if __name__ == '__main__':
    unittest.main()
