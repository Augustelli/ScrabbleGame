import unittest
from unittest.mock import patch, Mock
from game.models.model_tile import Tile
from game.models.model_tilebag import TilesBag
from game.configuration import cantidad_letras, puntaje_por_letra, cantidad_de_fichas_por_letra

tiles_testing = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestBagTiles(unittest.TestCase):
    def setUp(self):
        self.bag = TilesBag(tiles_testing)

    def test_take(self):
        count = 3
        taken_tiles = self.bag.take(count)
        self.assertEqual(len(taken_tiles), count, "La cantidad de fichas tomadas no es la esperada")
        self.assertEqual(len(self.bag.tiles), cantidad_letras - count, "La cantidad de fichas restantes en la bolsa no es la esperada")
        self.assertEquals(self.bag.take(120), "No hay suficientes fichas en la bolsa", "La cantidad de fichas tomadas no es la esperada")

    def test_put(self):
        initial_count = len(self.bag.tiles)
        tiles_to_put = [Tile("X", 8), Tile("Y", 4)]
        self.bag.put(tiles_to_put)
        self.assertEqual(len(self.bag.tiles), initial_count + len(tiles_to_put), "La cantidad de fichas después de poner no es la esperada")

    @patch('random.shuffle')  # Mock random.shuffle
    def test_init(self, mock_shuffle):
        tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3)]
        bag = TilesBag(tiles)
        self.assertEqual(bag.tiles, tiles)
        mock_shuffle.assert_called_once_with(tiles)
        self.assertEqual(len(bag.tiles), 3)

    def test_put_called(self):

        mock_shuffle = Mock()  # Crea un mock para random.shuffle
        with patch('random.shuffle', mock_shuffle):
            tiles_to_put = [Tile('A', 1)]
            self.bag.put(tiles_to_put)

            mock_shuffle.assert_called_once()
        self.assertEqual(len(self.bag.tiles), 101)


if __name__ == '__main__':
    unittest.main()
