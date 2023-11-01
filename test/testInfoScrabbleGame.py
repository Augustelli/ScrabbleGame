from unittest.mock import Mock, patch
import unittest

from game.modelsNew.BoardModel import Board
from game.modelsNew.CellModel import Cell
from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileModel import Tile


class TestScrabbleShowTurnInfo(unittest.TestCase):
    @patch('game.modelsNew.ScrabbleGameNew.Scrabble.showBoard')
    @patch('game.modelsNew.ScrabbleGameNew.Scrabble.showPlayerTiles')
    @patch('game.modelsNew.ScrabbleGameNew.Scrabble.showPlayerPoints')
    def test_showTurnInfo(self, mock_showPlayerPoints, mock_showPlayerTiles, mock_showBoard):
        scrabble = Scrabble(2, [])  # Asegúrate de pasar los valores adecuados
        scrabble.showTurnInfo()

        mock_showBoard.assert_called_once()
        mock_showPlayerTiles.assert_called_once()
        mock_showPlayerPoints.assert_called_once()


    @patch('builtins.print')
    def test_printLetterCell(self, mock_print):
        scrabble = Scrabble(2, [])
        cell = Cell(1,"")
        tile = Tile("A", 1)  # Crea una ficha para la celda
        cell.letter = (tile)

        scrabble.printLetterCell(cell)

        mock_print.assert_called_once_with(f"| {tile.letter} {tile.value}  ", end="")
if __name__ == '__main__':
    unittest.main()
