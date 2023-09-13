import unittest
from game.scrabble import ScrabbleGame


class TestScrabbleGame(unittest.TestCase):
    def setUp(self):
        self.game = ScrabbleGame(2)

    def test_next_turn(self):
        current_player1 = self.game.players[0]
        self.game.next_turn()
        current_player2 = self.game.players[1]
        self.assertNotEqual(current_player1, current_player2)
        self.assertEqual(self.game.current_player_index, 1)

    def test_end_game(self):
        self.assertFalse(self.game.end_game())
        # Simulo como si hubiera sacado todas las fichas
        self.game.bag_tiles.tiles = []
        self.assertTrue(self.game.end_game())

    def test_initial_player_turn(self):
        # Verifica que el primer jugador es el que comienza el juego
        self.assertEqual(self.game.current_player_index, 0)

    def test_next_turn_wrap_around(self):
        self.assertEqual(self.game.current_player_index, 0)
        # Verifica que el turno pase al primer jugador después del último
        last_player = self.game.players[-1]
        self.game.current_player = last_player
        self.game.next_turn()
        self.assertEqual(self.game.current_player_index, 1)


if __name__ == '__main__':
    unittest.main()
