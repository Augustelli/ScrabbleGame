import unittest
from unittest.mock import patch, Mock
from game.models import *
from game.models import TilesBag
from io import StringIO
import sys
import re
import pdb


tiles_testing = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]
tile_bag_testing = TilesBag(tiles_testing)


class TestTiles(unittest.TestCase):

    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
        self.assertEqual(str(tile), 'A (1)')


class TestTileGeneration(unittest.TestCase):
    def setUp(self):
        # Generar las fichas usando las configuraciones
        self.tiles = tiles_testing

    def test_tile_count(self):
        expected_total_tiles = sum(cantidad_de_fichas_por_letra.values())
        self.assertEqual(len(self.tiles), expected_total_tiles, f"La cantidad de fichas generadas no coincide con el total esperado {expected_total_tiles}")

    def test_tile_values(self):
        for tile in self.tiles:
            self.assertEqual(tile.value, puntaje_por_letra[tile.letter], f"El valor de la ficha '{tile.letter}' no coincide con el puntaje esperado")


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


class TestCells(unittest.TestCase):

    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(cell.multiplier,2)

        self.assertEqual(cell.multiplier_type,'letter')
        self.assertIsNone(cell.letter)
        self.assertEqual(cell.calculate_value(),0)

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),6)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.calculate_value(),3)


class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.dictionary = Dictionary()

    def test_load_dictionary(self):
        self.assertTrue(isinstance(self.dictionary.dictionary, set))
        self.assertGreater(len(self.dictionary.dictionary), 0)
        self.assertEqual(len(self.dictionary.dictionary), 88)

    def test_is_valid_word_valid(self):
        self.assertTrue(self.dictionary.is_valid_word("hombre"))
        self.assertTrue(self.dictionary.is_valid_word("cama"))
        self.assertTrue(self.dictionary.is_valid_word("Hombre"))

    def test_is_valid_word_invalid(self):
        self.assertFalse(self.dictionary.is_valid_word("xyz"))
        self.assertFalse(self.dictionary.is_valid_word("invalid"))
        
        
class TestPlayer(unittest.TestCase):


    def setUp(self):
        self.player = Player("Augusto")
        self.mock_board = Mock()


    def test_create_word_valid(self):
        valid_tiles = [Tile("H",1), Tile("O",1), Tile("L",3), Tile("A",4)]
        result = self.player.create_word(valid_tiles)
        self.assertTrue(result)

    def test_create_word_invalid(self):
        invalid_tiles = [Tile("X", 10), Tile("Y",2), Tile("Z", 6)]
        result = self.player.create_word(invalid_tiles)
        self.assertEqual(result, "Palabra inválida")


if __name__ == '__main__':

    unittest.main()
