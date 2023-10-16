import unittest
from game.modelsNew.PlayerModel import Player
from game.modelsNew.TileModel import Tile

from game.modelsNew.ScrabbleGameNew import Scrabble
import sys
from io import StringIO
import re
from unittest.mock import patch


class TestScrabbleMessages(unittest.TestCase):
    def setUp(self):
        # Configura un jugador y una selección de fichas
        self.game = Scrabble(2)
        self.game.players[0].points = 15
        self.game.players[1].name = "Jugador2"
        self.game.players[1].points = 20
        self.game.players[0].name = "Jugador1"
        self.game.players[0].rack.tiles = [
            Tile("A", 1), Tile("B", 3), Tile("C", 3),
            Tile("D", 2), Tile("E", 1), Tile("F", 4),
            Tile("G", 2)]
        self.game.players[1].rack.tiles = [
            Tile("A", 1), Tile("B", 3), Tile("C", 3),
            Tile("D", 2), Tile("E", 1), Tile("F", 4),
            Tile("G", 2)]
        self.board = self.game.board

    @patch('sys.stdout', new_callable=StringIO)
    def test_showPlayerPoints(self, mock_stdout):
        # Ejecuta el método showPlayerPoints del juego
        self.game.showPlayerPoints()

        # Captura la salida generada y comprueba si es la esperada
        output = mock_stdout.getvalue()
        expected_output = "Puntajes:\n -> Jugador1: 15 pts\n -> Jugador2: 20 pts\n\n"
        self.assertEqual(output, expected_output)

    #
    # def test_showPlayerTiles(self):
    #     # Redirige la salida estándar a un objeto StringIO para capturarla
    #     import sys
    #     from io import StringIO
    #     original_stdout = sys.stdout
    #     sys.stdout = StringIO()
    #
    #     # Ejecuta el método showPlayerTiles
    #     self.game.showPlayerTiles()
    #
    #     # Restaura la salida estándar
    #     sys.stdout = original_stdout
    #
    #     # Captura la salida generada y comprueba si es la esperada
    #     output = sys.stdout.getvalue()
    #     expected_output = "| A 1 | B 3 | C 3 | D 2 | E 1 | F 4 | G 2 | H 4 | I 1 | J 8 | K 5 | L 1 |\n"
    #     self.assertEqual(output, expected_output)


class TestPrintBoard(unittest.TestCase):

    def setUp(self):
        self.board = Scrabble(2).board
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
        self.player = Player("Augusto")

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

    def test_horizontal_words(self):
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.create_word("HOLA")
        self.player.put_tiles_on_board(7, 7, "h", self.board)
        result = self.board.find_all_valid_words_on_board(self.board.board)
        self.assertEqual(["HOLA"], result)

    def test_vertical_words(self):
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.create_word("HOLA")
        self.player.put_tiles_on_board(7, 7, "v", self.board)
        result = self.board.find_all_valid_words_on_board(self.board.board)
        self.assertEquals(["HOLA"], result)

    def test_no_words(self):
        words = self.board.find_all_valid_words_on_board(self.board.board)
        self.assertEqual(words, [])

    def test_vertical_and_horizontal_words(self):
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.create_word("HOLA")
        result = self.player.put_tiles_on_board(7, 7, "h", self.board)

        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4), Tile("S", 5)]
        self.player.create_word("HOLAS")
        self.player.put_tiles_on_board(0, 0, "v", self.board)
        result = self.board.find_all_valid_words_on_board(self.board.board)
        self.assertEquals(["HOLA", "HOLAS"], sorted(result))

if __name__ == '__main__':
    unittest.main()
