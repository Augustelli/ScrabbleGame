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
        ("AAAA", 14, 0, 'v', "La palabra AAAA no puede ser jugada en la posición con la orientación v porque no hay espacio suficiente"),
        ("AAAA", 0, 14, 'h', "La palabra AAAA no puede ser jugada en la posición con la orientación h porque no hay espacio suficiente"),
    ])
    def test_check_if_word_can_be_placed(self, word, row, column, direction, response):
        self.assertEqual(self.board.checkIfWordCanBePlaced(word, row, column, direction), response)

    def test_getLettersInRowColumn(self):
        # Verifica si se obtienen correctamente las letras en una fila/columna.
        letters = self.board.getLettersInRowColumn((7, 7), "h")
        expected_letters = "A"  # Asumiendo que hay una "A" en la celda central.
        self.assertEqual(letters, expected_letters)

    def test_addTilesToBoard(self):
        # Verifica si se añaden correctamente las fichas al tablero y se calcula el puntaje.
        letter_to_play = [Tile("X", 8), Tile("Y", 10)]
        score = self.board.addTilesToBoard(letter_to_play, 5, 5, "h", self.board, "XY")
        expected_score = 28  # El puntaje es la suma de los valores de "X" y "Y".
        self.assertEqual(score, expected_score)

    def test_calculateWordPoints(self):
        # Verifica si se calculan correctamente los puntos de una palabra.
        points = self.board.calculateWordPoints(1, 1, "v", self.board, 3)
        expected_points = 12  # Asumiendo que las celdas tienen valores correctos.
        self.assertEqual(points, expected_points)

    def test_calculateLettersPoints(self):
        # Verifica si se calculan correctamente los puntos de una celda.
        cell = self.board.board[0][0]  # Asegúrate de tener una celda configurada correctamente.
        multiplier = 1
        points = 0
        points, multiplier = self.board.calculateLettersPoints(cell, multiplier, points)
        expected_points = 1  # Asumiendo que la celda tiene un valor de 2.
        self.assertEqual(points, expected_points)
if __name__ == '__main__':
    unittest.main()
