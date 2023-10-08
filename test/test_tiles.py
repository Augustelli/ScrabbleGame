# import unittest
# from game.models.model_tile import Tile
# from modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra

# tiles_testing = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


# class TestTiles(unittest.TestCase):

#     def setUp(self):
#         self.tile = Tile('A', 1)
#         self.tiles = tiles_testing

#     def test_tile(self):
#         self.assertEqual(self.tile.letter, 'A')
#         self.assertEqual(self.tile.value, 1)

#     def test__str__(self):
#         self.assertEqual(str(self.tile), 'A (1)')

#     def test_tile_count(self):
#         expected_total_tiles = sum(cantidad_de_fichas_por_letra.values())
#         self.assertEqual(len(self.tiles), expected_total_tiles, f"La cantidad de fichas generadas no coincide con el total esperado {expected_total_tiles}")

#     def test_tile_values(self):
#         for tile in self.tiles:
#             self.assertEqual(tile.value, puntaje_por_letra[tile.letter], f"El valor de la ficha '{tile.letter}' no coincide con el puntaje esperado")


# if __name__ == '__main__':
#     unittest.main()
