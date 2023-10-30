import unittest
from game.modelsNew.TileModel import Tile
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra

from game.modelsNew.ScrabbleGameNew import Scrabble
from io import StringIO
from unittest.mock import patch
tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestScrabbleMessages(unittest.TestCase):
    def setUp(self):
        # Configura un jugador y una selección de fichas
        self.game = Scrabble(2, tilesTesting)
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

        output = mock_stdout.getvalue()
        expected_output = "Puntajes:\n -> Jugador1: 15 pts\n -> Jugador2: 20 pts\n\n"
        self.assertEqual(output, expected_output)
    def test_set_name(self):
        self.game.setPlayerName("NAME", 0)
        self.assertEqual(self.game.players[0].name, "NAME")

    def test_word_passes_center_horizontal(self):
        # Word starts at the center (7, 7) horizontally
        self.scrabble = Scrabble(2, tilesTesting)
        result = self.scrabble.wordPassesCenter("HELLO", 7, 7, "h")
        self.assertTrue(result)

    def test_word_passes_center_horizontal_not_centered(self):
        self.scrabble = Scrabble(2, tilesTesting)
        result = self.scrabble.wordPassesCenter("PYTHON", 7, 7, "h")
        self.assertTrue(result)

    def test_word_passes_center_vertical(self):
        self.scrabble = Scrabble(2, tilesTesting)
        result = self.scrabble.wordPassesCenter("WORLD", 7, 7, "v")
        self.assertTrue(result)

    def test_word_passes_center_vertical_not_centered(self):
        self.scrabble = Scrabble(2, tilesTesting)
        result = self.scrabble.wordPassesCenter("SCRABBLE", 7, 7, "v")
        self.assertTrue(result)

    def test_word_does_not_pass_center(self):
        self.scrabble = Scrabble(2, tilesTesting)
        result = self.scrabble.wordPassesCenter("PYTHON", 3, 3, "h")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
