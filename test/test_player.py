import unittest
from game.models.model_player import Player
from game.models.model_tile import Tile
from game.models.model_tilebag import TilesBag
from game.models.model_board import Board
from game.models.model_dictionary import Dictionary
from game.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tiles_testing = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Augusto", Dictionary())
        self.tilebag = TilesBag(tiles_testing)
        self.board = Board()

    def tearDown(self) -> None:
        del self.board

    def test_create_word_valid(self):
        valid_tiles = [Tile("H", 1), Tile("O", 1), Tile("L", 3), Tile("A", 4)]
        result = self.player.create_word(valid_tiles)
        self.assertTrue(result)
        self.assertEqual(self.player.next_word, "HOLA")

    def test_create_word_invalid(self):
        invalid_tiles = [Tile("X", 10), Tile("Y", 2), Tile("Z", 6)]
        result = self.player.create_word(invalid_tiles)
        self.assertEqual(result, "Palabra inválida")

    def test_get_tiles_from_tilebag(self):
        self.assertEqual(len(self.player.tiles), 0)
        self.player.get_tile_from_tilebag(self.tilebag, 7)
        self.assertEqual(len(self.player.tiles), 7)
        self.assertEqual(len(self.tilebag.tiles), 93)
        error_message = self.player.get_tile_from_tilebag(self.tilebag, 120)
        self.assertEqual(error_message, "No hay suficientes fichas en la bolsa")

    def test_get_tile_index(self):
        tile = Tile("A", 1)
        self.player.tiles.append(tile)
        self.assertEqual(self.player.get_player_tile_index("A"), 0)

    def test_get_tile_index_empty(self):
        tile = Tile("A", 1)
        self.assertEqual(self.player.get_player_tile_index(tile), None)

    def test_put_tiles_on_board_vertically(self):
        self.player.next_word = "HOLA"
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.put_tiles_on_board(0, 0, "v", self.board)
        self.assertEqual(self.player.next_word, "")
        self.assertEquals(len(self.player.tiles), 0)
        self.assertEquals(self.board.get_tile(0, 0).letter.letter, "H")
        self.assertEquals(self.board.get_tile(1, 0).letter.letter, "O")
        self.assertEquals(self.board.get_tile(2, 0).letter.letter, "L")
        self.assertEquals(self.board.get_tile(3, 0).letter.letter, "A")

    def test_put_tiles_on_board_horizontally(self):
        self.player.next_word = "HOLA"
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.put_tiles_on_board(0, 0, "h", self.board)
        self.assertEqual(self.player.next_word, "")
        self.assertEquals(len(self.player.tiles), 0)
        self.assertEquals(self.board.get_tile(0, 0).letter.letter, "H")
        self.assertEquals(self.board.get_tile(0, 1).letter.letter, "O")
        self.assertEquals(self.board.get_tile(0, 2).letter.letter, "L")
        self.assertEquals(self.board.get_tile(0, 3).letter.letter, "A")

    def test_calculate_word_value_single_letter(self):
        # Prueba el cálculo de valor para una sola letra
        player = Player("Jugador", Dictionary())
        player.tiles = [Tile("A", 1), Tile("B", 2), Tile("C", 3)]

        word_value = player.calculate_word_value("A")
        self.assertEqual(word_value, 1)

    def test_calculate_word_value_multiple_letters(self):
        # Prueba el cálculo de valor para una palabra con múltiples letras
        player = Player("Jugador", Dictionary())
        player.tiles = [Tile("A", 1), Tile("B", 2), Tile("C", 3)]

        word_value = player.calculate_word_value("ABC")
        self.assertEqual(word_value, 6)

    def test_calculate_word_value_empty_word(self):
        # Prueba el cálculo de valor para una palabra vacía
        player = Player("Jugador", Dictionary())
        player.tiles = [Tile("A", 1), Tile("B", 2), Tile("C", 3)]

        word_value = player.calculate_word_value("")
        self.assertEqual(word_value, 0)

    def test_calculate_word_value_missing_tiles(self):
        # Prueba el cálculo de valor cuando faltan fichas para las letras de la palabra
        player = Player("Jugador", Dictionary())
        player.tiles = [Tile("A", 1), Tile("B", 2), Tile("C", 3)]

        word_value = player.calculate_word_value("XYZ")
        self.assertEqual(word_value, 0)

    def test_horizontal_words(self):
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.create_word(self.player.tiles)
        self.player.put_tiles_on_board(7, 7, "h", self.board)
        result = self.player.find_all_valid_words_on_board(self.board.board)
        self.assertEqual(["HOLA"], result)

    def test_vertical_words(self):
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.create_word(self.player.tiles)
        self.player.put_tiles_on_board(7, 7, "v", self.board)
        result = self.player.find_all_valid_words_on_board(self.board.board)
        self.assertEquals(["HOLA"], result)

    def test_no_words(self):
        words = self.player.find_all_valid_words_on_board(self.board.board)
        self.assertEqual(words, [])

    def test_vertical_and_horizontal_words(self):
        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4)]
        self.player.create_word(self.player.tiles)
        result = self.player.put_tiles_on_board(7, 7, "h", self.board)

        self.player.tiles = [Tile('H', 1), Tile('O', 1), Tile('L', 3), Tile('A', 4), Tile("S", 5)]
        self.player.create_word(self.player.tiles)
        self.player.put_tiles_on_board(0, 0, "v", self.board)
        result = self.player.find_all_valid_words_on_board(self.board.board)
        self.assertEquals(["HOLA", "HOLAS"], sorted(result))


if __name__ == '__main__':
    unittest.main()
