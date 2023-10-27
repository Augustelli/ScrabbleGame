import re
import sys
import unittest
from io import StringIO

from game.modelsNew.PlayerModel import Player
from game.modelsNew.RackModel import Rack
from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileModel import Tile
from game.modelsNew.TileBagModel import TilesBag
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra

tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]



class TestPrintScrabbleGameTest(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.board = Scrabble(2, tilesTesting)
        self.expected_output = [
                "+---------" * 15 + "+",
                "| x3 word |         |         | x2letter|         |         |         | x3 word |         |         |         | x2letter|         |         | x3 word |",
                "+---------" * 15 + "+",
                "|         | x2 word |         |         |         | x3letter|         |         |         | x3letter|         |         |         | x2 word |         |",
                "+---------" * 15 + "+",
                "|         |         | x2 word |         |         |         | x2letter|         | x2letter|         |         |         | x2 word |         |         |",
                "+---------" * 15 + "+",
                "| x2letter|         |         | x2 word |         |         |         | x2letter|         |         |         | x2 word |         |         | x2letter|",
                "+---------" * 15 + "+",
                "|         |         |         |         | x2 word |         |         |         |         |         | x2 word |         |         |         |         |",
                "+---------" * 15 + "+",
                "|         | x3letter|         |         |         | x3letter|         |         |         | x3letter|         |         |         | x3letter|         |",
                "+---------" * 15 + "+",
                "|         |         | x2letter|         |         |         | x2letter|         | x2letter|         |         |         | x2letter|         |         |",
                "+---------" * 15 + "+",
                "| x3 word |         |         | x2letter|         |         |         | x2 word |         |         |         | x2letter|         |         | x3 word |",
                "+---------" * 15 + "+",
                "|         |         | x2letter|         |         |         | x2letter|         | x2letter|         |         |         | x2letter|         |         |",
                "+---------" * 15 + "+",
                "|         | x3letter|         |         |         | x3letter|         |         |         | x3letter|         |         |         | x3letter|         |",
                "+---------" * 15 + "+",
                "|         |         |         |         | x2 word |         |         |         |         |         | x2 word |         |         |         |         |",
                "+---------" * 15 + "+",
                "| x2letter|         |         | x2 word |         |         |         | x2letter|         |         |         | x2 word |         |         | x2letter|",
                "+---------" * 15 + "+",
                "|         |         | x2 word |         |         |         | x2letter|         | x2letter|         |         |         | x2 word |         |         |",
                "+---------" * 15 + "+",
                "|         | x2 word |         |         |         | x3letter|         |         |         | x3letter|         |         |         | x2 word |         |",
                "+---------" * 15 + "+",
                "| x3 word |         |         | x2letter|         |         |         | x3 word |         |         |         | x2letter|         |         | x3 word |",
                "+---------" * 15 + "+"
            ]
        self.expected_output_1_tile = self.expected_output.copy()
        self.expected_output_2_tile = self.expected_output.copy()
        self.expected_output_1_tile[1] = "|   A 1   |         |         | x2letter|         |         |         | x3 word |         |         |         | x2letter|         |         | x3 word |"
        self.expected_output_2_tile[1] = "|   A 1   |  RR 1   |         | x2letter|         |         |         | x3 word |         |         |         | x2letter|         |         | x3 word |"
        self.player = Player("Augusto", TilesBag(tilesTesting))

    def remove_color_codes(self, text):
        color_pattern = re.compile(r'\x1b\[[0-9;]+m')
        return color_pattern.sub('', text)

    def test_print_board_with_empty_cells(self):

        with StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            self.board.showBoard()
            sys.stdout = sys.__stdout__

            output_lines = mock_stdout.getvalue().strip().split("\n")

        output_lines = [self.remove_color_codes(line) for line in output_lines]

        captured_lines = []
        for expected_line, actual_line in zip(self.expected_output, output_lines):
            self.assertEqual(expected_line, actual_line)
            captured_lines.append(actual_line)

    def test_print_board_1_tile(self):

        with StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            self.board.board.addTileOnCell(Tile("A", 1), 0, 0)
            self.board.showBoard()
            sys.stdout = sys.__stdout__

            output_lines = mock_stdout.getvalue().strip().split("\n")

        output_lines = [self.remove_color_codes(line) for line in output_lines]

        captured_lines = []
        for expected_line, actual_line in zip(self.expected_output_1_tile, output_lines):
            self.assertEqual(expected_line, actual_line)
            captured_lines.append(actual_line)

    def test_print_board_2_tiles(self):

        with StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            self.board.board.addTileOnCell(Tile("A", 1), 0, 0)
            self.board.board.addTileOnCell(Tile("RR", 1), 0, 1)
            self.board.showBoard()
            sys.stdout = sys.__stdout__
            output_lines = mock_stdout.getvalue().strip().split("\n")

        output_lines = [self.remove_color_codes(line) for line in output_lines]
        captured_lines = []
        for expected_line, actual_line in zip(self.expected_output_2_tile, output_lines):
            self.assertEqual(expected_line, actual_line)
            captured_lines.append(actual_line)

class TestScrabbleShowMethods(unittest.TestCase):
    def setUp(self):
        self.players = [Player("Player1", TilesBag(tilesTesting)), Player("Player2", TilesBag(tilesTesting))]
        self.scrabble = Scrabble(len(self.players), tilesTesting)
        self.rack1 = Rack(TilesBag(tilesTesting))
        self.rack2 = Rack(TilesBag(tilesTesting))
        self.players[0].rack = self.rack1
        self.players[1].rack = self.rack2

    def test_show_player_tiles(self):
        expected_output = "| A 1 | B 3 | C 3 | D 2 | E 1 | F 4 | G 2 |"
        captured_output = StringIO()
        sys.stdout = captured_output

        self.scrabble.showPlayerTiles()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

    def test_show_player_points(self):
        self.players[0].points = 10
        self.players[1].points = 15
        expected_output = "Puntajes:\n -> Player1: 10 pts\n -> Player2: 15 pts"
        captured_output = StringIO()
        sys.stdout = captured_output

        self.scrabble.showPlayerPoints()

        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), expected_output)
if __name__ == '__main__':
    unittest.main()
