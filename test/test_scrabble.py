import unittest
from game.models.model_tile import Tile
from game.scrabble import ScrabbleGame
from game.models.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestScrabbleGame(unittest.TestCase):

    def setUp(self):
        self.scrabble_game = ScrabbleGame(players_count=2)
        self.scrabble_game.current_player.tiles = [Tile("H", 1), Tile("A", 1), Tile("L", 1), Tile("O", 1)]
        self.scrabble_game.board.add_tile(Tile("H", 1), 0, 0)
        self.scrabble_game.board.add_tile(Tile("O", 1), 0, 1)
        self.scrabble_game.board.add_tile(Tile("L", 1), 0, 2)
        self.scrabble_game.board.add_tile(Tile("A", 1), 0, 3)

    def test_validate_word(self):
        result = self.scrabble_game.validate_word("CASA", (0, 0), "h")
        self.assertEqual(result, 'Faltan tiles.')

        result = self.scrabble_game.validate_word("HALO", (1, 0), "v")
        self.assertTrue(result)

        result = self.scrabble_game.validate_word("XYZ", (0, 0), "v")
        self.assertEqual(result, 'Palabra no existe en la RAE')

        result = self.scrabble_game.validate_word("HALO", (12, 12), "v")
        self.assertFalse(result)

    def test_next_turn(self):
        self.assertEqual(self.scrabble_game.current_player_index, 0)
        self.assertEqual(self.scrabble_game.current_player, self.scrabble_game.players[0])

        self.scrabble_game.next_turn()

        self.assertEqual(self.scrabble_game.current_player_index, 1)
        self.assertEqual(self.scrabble_game.current_player, self.scrabble_game.players[1])

        self.scrabble_game.next_turn()
        self.scrabble_game.next_turn()
        self.scrabble_game.next_turn()

        self.assertEqual(self.scrabble_game.current_player_index, 0)
        self.assertEqual(self.scrabble_game.current_player, self.scrabble_game.players[0])


class TestScrabbleGame2(unittest.TestCase):
    def setUp(self):
        # Configura el juego o cualquier configuración necesaria para los tests
        self.game = ScrabbleGame(players_count=2)

    def test_get_words_horizontal(self):
        # Prueba para obtener palabras en dirección horizontal
        word = "VALOR"
        location = (7, 7)
        orientation = "h"

        result = self.game.get_words(word, location, orientation)
        self.assertIsInstance(result, list)

    def test_get_words_vertical(self):
        # Prueba para obtener palabras en dirección vertical
        word = "PALABRA"
        location = (7, 7)
        orientation = "v"

        result = self.game.get_words(word, location, orientation)
        self.assertIsInstance(result, list)

    def test_get_words_empty_word(self):
        word = ""
        location = (7, 7)
        orientation = "h"

        result = self.game.get_words(word, location, orientation)
        self.assertIsInstance(result, list)

    def test_get_words_wrong_orientation(self):
        word = "HOLA"
        location = (7, 7)
        orientation = "d"  # Orientación incorrecta

        result = self.game.get_words(word, location, orientation)
        self.assertIsInstance(result, list)

    def test_get_word_in_direction_horizontal(self):
        # Prueba para obtener una palabra en dirección horizontal
        word = "HOLA"
        location = (7, 7)
        orientation = "h"

        result = self.game.get_word_in_direction(word, location, orientation)
        self.assertIsInstance(result, str)

    def test_get_word_in_direction_vertical(self):
        # Prueba para obtener una palabra en dirección vertical
        word = "MUNDO"
        location = (7, 7)
        orientation = "v"

        result = self.game.get_word_in_direction(word, location, orientation)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
