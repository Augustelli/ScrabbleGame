import unittest
from unittest.mock import patch

from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileModel import Tile
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra

tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestScrabblePlayWord(unittest.TestCase):

    def setUp(self):
        self.scrabble = Scrabble(2, tilesTesting)
        self.player1 = self.scrabble.players[0]
        self.player1.rack.tiles = [Tile("A", 1), Tile("U", 3), Tile("T", 3), Tile("O", 2), Tile("E", 1), Tile("F", 4), Tile("G", 2)]
        self.player2 = self.scrabble.players[1]

    @patch('builtins.input', side_effect=["8 8 h"])  # Simula la entrada del usuario
    def test_play_invalid_word(self, mock_input):
        initial_points = self.scrabble.current_player.points
        self.scrabble.playWord("sadasfar")
        final_points = self.scrabble.current_player.points
        self.assertEqual(final_points, initial_points)

    @patch('builtins.input', side_effect=["15 15 h"])
    def test_play_word_word_does_not_fit(self, mock_input):
        self.scrabble.firstPlay = False
        # Simula que la palabra no cabe en el tablero
        with patch.object(self.scrabble, 'wordCanBePlayed', return_value=False):
            initial_points = self.scrabble.current_player.points
            self.scrabble.playWord("auto")
            final_points = self.scrabble.current_player.points
            self.assertEqual(final_points, initial_points)  # Los puntos no deben cambiar

    @patch('builtins.input', side_effect=["8 8 h"])
    def test_play_word_missing_letters(self, mock_input):
        with patch.object(self.scrabble, 'checkForMissingTiles', return_value=([Tile("A", 1), Tile("U", 3), Tile("T", 3), Tile("O", 2)], [Tile("S", 2)])):
            initial_points = self.scrabble.current_player.points
            self.scrabble.playWord("autos")
            final_points = self.scrabble.current_player.points
            self.assertEqual(final_points, initial_points)  # Los puntos no deben cambiar

    @patch('builtins.input', side_effect=["8 8 h"])  # Simula la entrada del usuario
    def test_play_valid_word(self, mock_input):
        current_player_index = self.scrabble.current_player_index
        initial_points = self.scrabble.current_player.points
        self.scrabble.playWord("auto")
        final_points = self.scrabble.current_player.points
        self.assertEqual(final_points, initial_points)
        self.assertEqual(self.scrabble.skippedTimes, 0)
        self.assertNotEqual(self.scrabble.current_player_index, current_player_index)
        self.assertFalse(self.scrabble.firstPlay)

if __name__ == '__main__':
    unittest.main()
