import unittest
import redis
import pickle
import os

from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileModel import Tile
from game.redisModule.redis import saveScrabble, loadScrabble, returnOrCreatePlay

class TestScrabbleRedisPersistence(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Configurar una conexión a la base de datos Redis local
        cls.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    @classmethod
    def tearDownClass(cls):
        # Detener y eliminar el contenedor de Redis cuando se completen las pruebas
        cls.redis_client.close()
        os.system("docker stop redis-scrabble-test")
        os.system("docker rm redis-scrabble-test")

    def test_save_and_load_scrabble(self):
        cantPlayers = 2
        scrabble = Scrabble(2, [Tile("A", 1)])  # Rellena con los valores adecuados
        saveScrabble(scrabble, "test_game")

        loaded_scrabble = loadScrabble("test_game")

        self.assertEqual(loaded_scrabble.current_player.name, scrabble.current_player.name)
        self.assertEqual(loaded_scrabble.current_player.points, scrabble.current_player.points)

    def test_return_or_create_play(self):
        saved_scrabble = Scrabble(2, [Tile("A", 1)])  # Rellena con los valores adecuados
        saveScrabble(saved_scrabble, "existing_game")
        saveScrabble(saved_scrabble, "test_game")
        loaded_game = returnOrCreatePlay("test_game")

        self.assertEqual(loaded_game.current_player.name, saved_scrabble.current_player.name)
        self.assertEqual(loaded_game.current_player.points, saved_scrabble.current_player.points)

    def test_loadScrabble_else(self):
        loaded_game = loadScrabble("non_existing_game")
        self.assertIsNone(loaded_game)

    def test_return_or_create_play_else(self):
        # Simular la no existencia de una partida en Redis
        loaded_game = returnOrCreatePlay("non_existing_game")
        self.assertFalse(loaded_game)

if __name__ == '__main__':
    unittest.main()
