# import pdb
# import re
# import sys
# import unittest
# import io
# from unittest.mock import patch
# from io import StringIO
# from game.modelsNew.RackModel import Rack
# from game.modelsNew.ScrabbleGameNew import Scrabble
# from game.modelsNew.TileModel import Tile
# from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
#
# tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]
#
# class TestScrabbleShowMethods(unittest.TestCase):
#
#     maxDiff = None
#
#     def setUp(self):
#         self.scrabble = Scrabble(2, tilesTesting)
#         self.scrabble.players[0].name = "Jugador1"
#         self.scrabble.players[1].name = "Jugador2"
#         self.captured_output = io.StringIO()
#         sys.stdout = self.captured_output
#         self.expected_output = (
#     " 1  | 3W   |      |      | 2L   |      |      |      | 3W   |      |      |      | 2L   |      |      | 3W\n"
#     " 2  |      | 2W   |      |      |      | 3L   |      |      |      | 3L   |      |      |      | 2W   |\n"
#     " 3  |      |      | 2W   |      |      |      | 2L   |      | 2L   |      |      |      | 2W   |      |\n"
#     " 4  | 2L   |      |      | 2W   |      |      |      | 2L   |      |      |      | 2W   |      |      | 2L\n"
#     " 5  |      |      |      |      | 2W   |      |      |      |      |      | 2W   |      |      |      |   \n"
#     " 6  |      | 3L   |      |      |      | 3L   |      |      |      | 3L   |      |      |      | 3L   |\n"
#     " 7  |      |      | 2L   |      |      |      | 2L   |      | 2L   |      |      |      | 2L   |      |\n"
#     " 8  | 3W   |      |      | 2L   |      |      |      | 2W   |      |      |      | 2L   |      |      | 3W\n"
#     " 9  |      |      | 2L   |      |      |      | 2L   |      | 2L   |      |      |      | 2L   |      |\n"
#     "10  |      | 3L   |      |      |      | 3L   |      |      |      | 3L   |      |      |      | 3L   |\n"
#     "11  |      |      |      |      | 2W   |      |      |      |      |      | 2W   |      |      |      |   \n"
#     "12  | 2L   |      |      | 2W   |      |      |      | 2L   |      |      |      | 2W   |      |      | 2L\n"
#     "13  |      |      | 2W   |      |      |      | 2L   |      | 2L   |      |      |      | 2W   |      |\n"
#     "14  |      | 2W   |      |      |      | 3L   |      |      |      | 3L   |      |      |      | 2W   |\n"
#     "15  | 3W   |      |      | 2L   |      |      |      | 3W   |      |      |      | 2L   |      |      | 3W\n"
# )
#
#     def tearDown(self):
#         sys.stdout = sys.__stdout__
#
#         self.rules = """
#     ------------------------------------------------------------------------------------------------------------------------------------------------------
# Para realizar jugadas:
# 	- Ingrese la palabra que desea jugar.
# 	- Si desea cambiar fichas, ingrese 'change'.
# 	- Si desea pasar el turno, ingrese 'skip o  ENTER'.
# 	- Para guardar la partida y salir 'SAVE''
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#     """
#         self.points = """
#     Puntajes:
#  -> 1: 0 pts
#  -> 2: 0 pts
#     """
#     def test_show_board(self):
#         board = self.scrabble.board
#         self.scrabble.showBoard()
#         captured_lines = self.captured_output.getvalue().split('\n')
#         for captured_line, expected_line in zip(captured_lines, self.expected_output.split('\n')):
#             self.assertEqual(captured_line, expected_line)
#
#     def test_show_rack(self):
#         rack = Rack(self.tiles_bag)
#         rack.showRack()
#         self.assertTrue(True)
#
#     def test_show_tiles_bag(self):
#         tiles_bag = self.tiles_bag
#         tiles_bag.showTilesBag()
#         self.assertTrue(True)
#
#     def test_show_player(self):
#         player = self.players[0]
#         player.showPlayer()
#         self.assertTrue(True)
#
#     def test_show_players(self):
#         self.scrabble.showPlayers()
#         self.assertTrue(True)
#
#
# if __name__ == '__main__':
#     unittest.main()
