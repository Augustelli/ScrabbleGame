import pdb
import unittest
import parameterized
from game.modelsNew.BoardModel import Board
from game.modelsNew.TileModel import Tile


class TestBoardModel(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.board.board[0][0].letter = Tile("A", 1)
        self.board.board[7][7].letter = Tile("A", 1)
        self.board.board[11][7].letter = Tile("A", 1)
        self.board.board[7][11].letter = Tile("A", 1)

    def test_get_tiles_on_cell(self):
        self.assertEqual(self.board.getTilesOnCell(0,0), Tile("A", 1))
        self.assertEqual(self.board.getTilesOnCell(1,0), None)

    def test_add_tiles_on_cell(self):
        self.board.addTileOnCell(Tile("A", 1), 1, 1)
        self.assertEqual(Tile("A", 1), self.board.getTilesOnCell(1,1))
        self.board.addTileOnCell(Tile("B", 1), 0, 0)
        self.assertEqual(Tile("A", 1), self.board.getTilesOnCell(0,0))


    @parameterized.parameterized.expand([

        ("AAAA", 7, 7, 'h', True),
        ("AAAA", 7, 7, 'v', True),
        ("AAAA", 11, 7, 'v', True),
        ("AAAA", 7, 11, 'h', True),
        ("AAAA", 0, 0, 'v', True),
        ("AAAA", 0, 0, 'h', True),
        ("AAAA", 8, 0, 'h', False),
        ("AAAA", 0, 8, 'v', False),
        ("AAAA", 14, 0, 'v', False),
        ("AAAA", 0, 14, 'h', False),
    ])
    def test_check_if_word_can_be_placed(self, word, row, column, direction, response):
        self.assertEqual(self.board.checkIfWordCanBePlaced(word, row, column, direction), response)


    @parameterized.parameterized.expand([
        (7, 7, 'h'),
        (7, 7, 'v')
    ])
    def test_getLettersInRowColumn(self, row, column, direction):
        letters = self.board.getLettersInRowColumn((row, column), direction)
        expected_letters = ["A"]
        self.assertEqual(letters, expected_letters)

    def test_addTilesToBoard(self):
        letter_to_play = [Tile("X", 8), Tile("Y", 10)]
        score = self.board.addTilesToBoard(letter_to_play,[ 5, 5, "h"], self.board, "XY")
        expected_score = 28
        self.assertEqual(score, expected_score)

    def test_addTilesToBoard_vertical(self):
        # Configura un caso de prueba con orientación vertical.
        self.board = Board()
        letterToPlay = [Tile("A", 1), Tile("A", 1), Tile("A", 1)]  # Lista ordenada como se juegan las fichas.
        self.board.addTilesToBoard(letterToPlay, [2, 5, "v"], self.board, "AAA")
        for i, tile in enumerate([Tile("A", 1), Tile("A", 1), Tile("A", 1)]):
            self.assertEqual(self.board.getTilesOnCell(2 + i, 5), tile)

    def test_calculateWordPoints(self):
        self.board.board[1][1].letter = Tile("A", 1)
        self.board.board[2][1].letter = Tile("A", 1)
        self.board.board[3][1].letter = Tile("A", 1)
        points = self.board.calculateWordPoints([1, 1],  "v", self.board, 3)
        expected_points = 6
        self.assertEqual(points, expected_points)

    def test_calculateLettersPoints(self):
        # Verifica si se calculan correctamente los puntos de una celda.
        cell = self.board.board[0][0]
        multiplier = 1
        points = 0
        points, multiplier = self.board.calculateLettersPoints(cell, multiplier, points)
        expected_points = 1
        self.assertEqual(points, expected_points)

    class TestBoardLettersInRowColumn(unittest.TestCase):
        def setUp(self):
            self.board = Board()

        def test_get_letters_in_row_empty(self):
            row = 0
            letters = ""
            result = self.board.getLettersInRow(letters, row)
            self.assertEqual(result, "_______________")

        def test_get_letters_in_row_with_letters(self):
            row = 0
            letters = ""
            self.board.board[row][0].letter = Tile("A", 1)
            self.board.board[row][3].letter = Tile("B", 2)
            self.board.board[row][8].letter = Tile("C", 3)
            result = self.board.getLettersInRow(letters, row)
            self.assertEqual(result, "A___B____C______")

        def test_get_letters_in_row_with_mixed(self):
            row = 0
            letters = ""
            self.board.board[row][2].letter = Tile("A", 1)
            self.board.board[row][6].letter = Tile("B", 2)
            self.board.board[row][12].letter = Tile("C", 3)
            result = self.board.getLettersInRow(letters, row)
            self.assertEqual(result, "__A___B____C___")

if __name__ == '__main__':
    unittest.main()
