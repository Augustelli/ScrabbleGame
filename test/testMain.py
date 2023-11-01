import unittest

import unittest
from io import StringIO
from unittest import mock
from unittest.mock import patch, MagicMock, Mock, call

from game.main import get_num_players, is_valid_num_players, get_player_names, display_info, change_tiles, \
    set_player_names, main, load_or_create_game
from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileModel import Tile
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra

tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]

class TestMain(unittest.TestCase):

    def setUp(self):
        self.scrabble = Scrabble(2, tilesTesting)  # Ajusta los parámetros según tu implementación
        self.scrabble.players[0].name = "Player 1"
        self.scrabble.players[1].name = "Player 2"

    @patch('builtins.input', side_effect=["Player 3", "Player 4"])
    def test_set_player_names(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            set_player_names(self.scrabble, 2, ["Player 3", "Player 4"])
            output = mock_stdout.getvalue()

        expected_output = "Jugador 1: Player 3\nJugador 2: Player 4\n"
        self.assertEqual(output, expected_output)
        self.assertEqual(self.scrabble.players[0].name, "Player 3")
        self.assertEqual(self.scrabble.players[1].name, "Player 4")

    @patch('builtins.input', side_effect=["2"])
    def test_get_num_players_valid(self, mock_input):
        result = get_num_players()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=["5", "3"])
    def test_get_num_players_multiple_attempts(self, mock_input):
        result = get_num_players()
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=["1", "6", "2"])
    def test_get_num_players_invalid_then_valid(self, mock_input):
        result = get_num_players()
        self.assertEqual(result, 2)

    def test_is_valid_num_players_valid(self):
        result = is_valid_num_players("3")
        self.assertTrue(result)

    def test_is_valid_num_players_invalid(self):
        result = is_valid_num_players("1")
        self.assertFalse(result)

    def test_is_valid_num_players_non_integer(self):
        result = is_valid_num_players("two")
        self.assertFalse(result)

    @patch('builtins.input', side_effect=["Alice", "Bob"])
    def test_get_player_names_valid(self, mock_input):
        result = get_player_names(2)
        self.assertEqual(result, ["Alice", "Bob"])

    @patch('builtins.input', side_effect=["Player1", "Player2", "Player3"])
    def test_get_player_names_multiple_players(self, mock_input):
        result = get_player_names(3)
        self.assertEqual(result, ["Player1", "Player2", "Player3"])

    @patch('builtins.input', side_effect=["Player1", "2"])
    def test_get_player_names_invalid_then_valid(self, mock_input):
        result = get_player_names(2)
        self.assertEqual(result, ["Player1", "2"])


    @patch('game.main.load_or_create_game')
    @patch('game.main.display_info')
    @patch('game.main.clear_screen')
    @patch('game.main.saveScrabble')
    @patch('builtins.input', side_effect=["", "skip", "save", "test_game"])
    @patch('builtins.print')
    @patch('os.system')
    def test_main(self, mock_system, mock_print, mock_input, mock_save_scrabble, mock_clear_screen, mock_display_info, mock_load_or_create_game):
        mock_game = MagicMock()
        mock_game.gameFinished = False
        mock_load_or_create_game.return_value = mock_game

        main()

        mock_print.assert_any_call("¡Bienvenido a Scrabble!")
        mock_input.assert_any_call("¿Tienes una partida guardada? Retómala con su nombre, sino presiona ENTER: ")
        mock_load_or_create_game.assert_called_once_with("")
        mock_display_info.assert_called()
        mock_save_scrabble.assert_called_once_with(mock_game, "test_game")
        mock_clear_screen.assert_called()
        mock_game.endGame.assert_called()

    @patch('game.modelsNew.PlayerModel.Player.exchangeTiles')
    @patch('game.modelsNew.ScrabbleGameNew.Scrabble.nextTurn')
    def test_change_tiles(self, mock_next_turn, mock_exchange_tiles):
        # Crea una instancia de juego de Scrabble
        scrabble = Scrabble(2, [])

        # Llama a la función change_tiles
        change_tiles(scrabble)

        # Verifica que los métodos se llamen una vez cada uno
        mock_exchange_tiles.assert_called_once()
        mock_next_turn.assert_called_once()




if __name__ == '__main__':
    unittest.main()
