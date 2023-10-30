# import unittest
# from unittest.mock import patch
#
# from game.modelsNew.PlayerModel import Player
# from game.modelsNew.TileBagModel import TilesBag
# from game.modelsNew.TileModel import Tile
# from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
#
# tiles_test = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]
#
# class TestPlayerExchangeTiles(unittest.TestCase):
#
#
#     @patch('builtins.input', side_effect=["A"])
#     def test_exchange_valid_tiles(self, mock_input):
#         self.player = Player("Jugador1", TilesBag(tiles_test))
#         self.player.rack = [Tile("A", 1), Tile("B", 1), Tile("C", 1)]
#         initial_rack = self.player.getTilesOnRack()
#         self.player.exchangeTiles()
#         final_rack = self.player.getTilesOnRack()
#         self.assertNotEqual(initial_rack, final_rack)
#         self.assertEqual(len(final_rack), len(initial_rack))
#
#     #Demora
#     @patch('builtins.input', side_effect=["P", "A"])
#     def test_exchange_invalid_tiles(self, mock_input):
#         self.player = Player("Jugador1", TilesBag(tiles_test))
#         self.player.rack = [Tile("A", 1), Tile("B", 1), Tile("C", 1)]
#         self.player.exchangeTiles()
#         final_rack = self.player.rack.getTilesOnRack()
#         self.assertEqual(self.player.rack, final_rack)
#
#     #Demora
#     @patch('builtins.input', side_effect=["A B C"])
#     def test_exchange_all_tiles(self, mock_input):
#         self.player = Player("Jugador1", TilesBag(tiles_test))
#         self.player.rack = [Tile("A", 1), Tile("B", 1), Tile("C", 1)]
#
#         initial_rack = self.player.rack.getTilesOnRack()
#         self.player.exchangeTiles()
#         final_rack = self.player.rack.getTilesOnRack()
#         self.assertNotEqual(initial_rack, final_rack)
#         self.assertEqual(len(final_rack), len(initial_rack))
#
# if __name__ == '__main__':
#     unittest.main()
