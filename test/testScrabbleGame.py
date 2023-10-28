import unittest
from game.modelsNew.PlayerModel import Player
from game.modelsNew.TileModel import Tile
from game.modelsNew.TileBagModel import TilesBag
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

        # Captura la salida generada y comprueba si es la esperada
        output = mock_stdout.getvalue()
        expected_output = "Puntajes:\n -> Jugador1: 15 pts\n -> Jugador2: 20 pts\n\n"
        self.assertEqual(output, expected_output)
    def test_set_name(self):
        self.game.setPlayerName("NAME", 0)
        self.assertEqual(self.game.players[0].name, "NAME")

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
        self.board = Scrabble(2, tilesTesting).board
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
        self.player = Player("Augusto", TilesBag(tilesTesting))


class TestScrabbleNextTurn(unittest.TestCase):
    def setUp(self):
        self.players = [Player("Player 1", TilesBag(tilesTesting)), Player("Player 2", TilesBag(tilesTesting)), Player("Player 3", TilesBag(tilesTesting))]
        self.scrabble = Scrabble(len(self.players), tilesTesting)

    def test_next_turn_first_player(self):
        self.assertEqual(self.scrabble.current_player_index, 0)
        self.assertEqual(self.scrabble.current_player_index, 0)
        self.scrabble.nextTurn()
        self.assertEqual(self.scrabble.current_player_index, 1)

    def test_next_turn_last_player(self):
        self.scrabble.current_player_index = len(self.players) - 1
        self.assertEqual(self.scrabble.current_player_index, len(self.players) - 1)
        self.scrabble.nextTurn()
        self.assertEqual(self.scrabble.current_player_index, 0)

    def test_pass_turn_increment_skip_count(self):
        self.assertEqual(self.scrabble.skippedTimes, 0)
        self.scrabble.passTurn()
        self.assertEqual(self.scrabble.skippedTimes, 1)

    def test_pass_turn_next_player(self):
        initial_player_index = self.scrabble.current_player_index
        self.scrabble.passTurn()
        self.assertEqual(self.scrabble.current_player_index, (initial_player_index + 1) % len(self.players))

    # def test_end_game_empty_tile_bag(self):
    #     self.scrabble.tiles_bags.tiles = []
    #     self.scrabble.endGame()
    #     self.assertEqual(self.scrabble.gameFinished, True)
    #
    # def test_end_game_skipped_turns_limit_reached(self):
    #     self.scrabble.skippedTimes = 2 * len(self.players)
    #     self.scrabble.endGame()
    #     self.assertEqual(self.scrabble.gameFinished,True)

    def test_end_game_not_finished(self):
        self.scrabble.tiles_bags.tiles = ["A", "B", "C"]
        self.scrabble.endGame()
        self.assertEqual(self.scrabble.gameFinished, False)
if __name__ == '__main__':
    unittest.main()
