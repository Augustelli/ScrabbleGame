import unittest

from game.modelsNew.PlayerModel import Player
from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileModel import Tile
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra

tiles_test = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]

class TestScrabbleGameFlow(unittest.TestCase):
    def setUp(self):
        # Configurar el entorno de prueba
        self.scrabble = Scrabble(2, tiles_test)
        self.players = self.scrabble.players
        self.tiles_bag = self.scrabble.tiles_bags

    def test_next_turn(self):
        initial_player = self.scrabble.current_player
        self.scrabble.nextTurn()
        new_player = self.scrabble.current_player
        self.assertNotEqual(initial_player, new_player)

    def test_pass_turn(self):
        initial_skipped_times = self.scrabble.skippedTimes
        self.scrabble.passTurn()
        new_skipped_times = self.scrabble.skippedTimes
        self.assertEqual(new_skipped_times, initial_skipped_times + 1)

    # def test_end_game_all_skip(self):
    #     self.scrabble.players = [Player("Jugador1", self.tiles_bag), Player("Jugador2", self.tiles_bag)]
    #     self.scrabble.skippedTimes = 4
    #     self.scrabble.endGame()
    #     self.assertTrue(self.scrabble.gameFinished)

if __name__ == '__main__':
    unittest.main()
