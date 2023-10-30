import unittest
import parameterized
from game.modelsNew.BoardModel import Board
from game.modelsNew.TileModel import Tile

## Realentiza los test
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


    # ### Este test causa que se tarde al cerrar el test "
    # def test_get_tiles_on_cell(self):
     # @parameterized.parameterized.expand([("AAAA", 7, 7, 'h', True)])
    #     ("AAAA", 7, 7, 'v', True),
    #     ("AAAA", 11, 7, 'v', True),
    #     ("AAAA", 7, 11, 'h', True),
    #     ("AAAA", 0, 0, 'v', True),
    #     ("AAAA", 0, 0, 'h', True),
    #     ("AAAA", 8, 0, 'h', False),
    #     ("AAAA", 0, 8, 'v', False),
    #     ("AAAA", 14, 0, 'v', False),
    #     ("AAAA", 0, 14, 'h', False),
    #     ("AAAA", 0, 0, 'h', True),

    #def test_check_if_word_can_be_placed(self, word, row, column, direction, response):
    #    self.assertEqual(self.board.checkIfWordCanBePlaced(word, row, column, direction), response)


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
        cell = self.board.board[0][0]
        multiplier = 1
        points = 0
        points, multiplier = self.board.calculateLettersPoints(cell, multiplier, points)
        expected_points = 1
        self.assertEqual(points, expected_points)
    def test_checkCanBePlacedHorizontal_last_character(self):
        # Prueba cuando el último carácter se encuentra en el tablero.
        word = "SCRABBLE"
        row = 15
        column = 15  # El último carácter 'E' de 'SCRABBLE'
        result = self.board.checkCanBePlacedHorizontal(word, row, column)
        self.assertFalse(result)

    def test_checkCanBePlacedVertical_last_character(self):
        word = "BINGO"
        row = 15
        column = 15
        result = self.board.checkCanBePlacedVertical(word, row, column)
        self.assertFalse(result)


if __name__ == '__main__':
     unittest.main()
