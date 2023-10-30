import unittest

from game.modelsNew.BoardModel import Board
from game.modelsNew.TileModel import Tile


class TestBoardLettersInRowColumn(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_get_letters_in_row_empty(self):
        result = self.board.getLettersInRowColumn([0,0], "h")
        self.assertEqual(result, [])

    def test_get_letters_in_row_with_letters(self):
        self.board.board[0][0].letter = Tile("A", 1)
        self.board.board[0][3].letter = Tile("B", 2)
        self.board.board[0][8].letter = Tile("C", 3)
        result = self.board.getLettersInRowColumn([0,0], "h")
        self.assertEqual(result, ["A"])

if __name__ == '__main__':
    unittest.main()
