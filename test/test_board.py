import unittest
from game.models.model_board import Board
from game.models.model_cell import Cell
from game.models.model_tile import Tile

import sys
from io import StringIO
import re


class TestBoard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.board = Board()

    def test_get_tile(self):
        tile = self.board.get_tile(7, 7)
        self.assertIsInstance(tile, Cell)

    def test_add_tile_empty_cell(self):
        tile = Tile("A", 1)
        result = self.board.add_tile(tile, 0, 0)
        self.assertIsNone(result)

    def test_add_tile_occupied_cell(self):
        tile = Tile("B", 2)
        self.board.add_tile(tile, 0, 0)
        result = self.board.add_tile(tile, 0, 0)
        self.assertEqual(result, "Celda ocupada")

    def test_remove_tile_with_letter(self):
        tile = Tile("C", 3)
        self.board.add_tile(tile, 0, 0)
        self.board.remove_tile(0, 0)
        self.assertIsNone(self.board.get_tile(0, 0).letter)

    def test_remove_tile_empty_cell(self):
        result = self.board.remove_tile(3, 0)
        self.assertEqual(result, "No hay ficha en la celda")


class TestPrintBoard(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.board = Board()
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

    def remove_color_codes(self, text):
        color_pattern = re.compile(r'\x1b\[[0-9;]+m')
        return color_pattern.sub('', text)

    def test_print_board_with_empty_cells(self):

        with StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            self.board.print_board()
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
            self.board.add_tile(Tile("A", 1), 0, 0)
            self.board.print_board()
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
            self.board.add_tile(Tile("A", 1), 0, 0)
            self.board.add_tile(Tile("RR", 1), 0, 1)
            self.board.print_board()
            sys.stdout = sys.__stdout__
            output_lines = mock_stdout.getvalue().strip().split("\n")

        output_lines = [self.remove_color_codes(line) for line in output_lines]
        captured_lines = []
        for expected_line, actual_line in zip(self.expected_output_2_tile, output_lines):
            self.assertEqual(expected_line, actual_line)
            captured_lines.append(actual_line)


if __name__ == '__main__':
    unittest.main()
