import unittest

from game.modelsNew.PlayerModel import Player
from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileBagModel import TilesBag
from game.modelsNew.TileModel import Tile
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra

tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]

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

    def test_end_game_not_finished(self):
        self.scrabble.tiles_bags.tiles = ["A", "B", "C"]
        self.scrabble.endGame()
        self.assertEqual(self.scrabble.gameFinished, False)

    def test_word_can_be_played_first_play(self):
        self.scrabble.firstPlay = True
        self.assertTrue(self.scrabble.wordCanBePlayed("HELLO", 7, 7, "h"))
        self.assertTrue(self.scrabble.wordCanBePlayed("WORLD", 7, 7, "v"))  # Debería poder colocar "WORLD" en el centro verticalmente

    def test_word_can_be_played_subsequent_play(self):
        # Prueba si una palabra puede ser jugada en una jugada que no es la primera (firstPlay es False)
        self.scrabble.firstPlay = False
        self.scrabble.board.board[7][7].letter = "A"  # Simulamos una letra "A" en el centro del tablero
        self.assertTrue(self.scrabble.wordCanBePlayed("HELLO", 7, 6, "h"))  # Debería poder colocar "HELLO" hacia la izquierda
        self.assertFalse(self.scrabble.wordCanBePlayed("WORLD", 7, 11, "h"))  # No debería poder colocar "WORLD" hacia la derecha
        self.assertTrue(self.scrabble.wordCanBePlayed("HELLO", 6, 7, "v"))  # Debería poder colocar "HELLO" hacia arriba
        self.assertFalse(self.scrabble.wordCanBePlayed("WORLD", 11, 7, "v"))  # No debería poder colocar "WORLD" hacia abajo

    # def test_checkForMissingTiles_horizontal(self):
    #     scrabble = Scrabble(2, [Tile("A", 1), Tile("B", 3), Tile("C", 3)])
    #     scrabble.board.board[7][7].letter = Tile("A", 1)
    #     scrabble.board.board[7][8].letter = Tile("B", 3)
    #     scrabble.current_player.rack.tiles = [Tile("A", 3), Tile("B", 3)]
    #     lettersToPlay, missingLetters = scrabble.checkForMissingTiles("ABC", 7, 7, "h")
    #     expected_letters_to_play = [Tile("A", 3), Tile("B", 3)]
    #     expected_missing_letters = []
    #
    #     self.assertEqual(lettersToPlay, expected_letters_to_play)
    #     self.assertEqual(missingLetters, expected_missing_letters)
    #
    # def test_checkForMissingTiles_vertically(self):
    #     scrabble = Scrabble(2, [Tile("A", 1), Tile("B", 3), Tile("C", 3)])
    #     scrabble.board.board[7][7].letter = Tile("A", 1)
    #     scrabble.board.board[8][7].letter = Tile("B", 3)
    #     scrabble.current_player.rack.tiles = [Tile("A", 3), Tile("B", 3)]
    #     lettersToPlay, missingLetters = scrabble.checkForMissingTiles("ABC", 7, 7, "v")
    #     expected_letters_to_play = [Tile("A", 3), Tile("B", 3)]
    #     expected_missing_letters = []
    #
    #     self.assertEqual(lettersToPlay, expected_letters_to_play)
    #     self.assertEqual(missingLetters, expected_missing_letters)

if __name__ == '__main__':
    unittest.main()
