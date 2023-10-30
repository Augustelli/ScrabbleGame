import re
import sys
import unittest
from io import StringIO

from game.modelsNew.PlayerModel import Player
from game.modelsNew.RackModel import Rack
from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileModel import Tile
from game.modelsNew.TileBagModel import TilesBag
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra

tilesTesting = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]

class TestScrabbleShowMethods(unittest.TestCase):
    def setUp(self):
        self.players = [Player("Player1", TilesBag(tilesTesting)), Player("Player2", TilesBag(tilesTesting))]
        self.scrabble = Scrabble(len(self.players), tilesTesting)
        self.rack1 = Rack(TilesBag(tilesTesting))
        self.rack2 = Rack(TilesBag(tilesTesting))
        self.players[0].rack = self.rack1
        self.players[1].rack = self.rack2

if __name__ == '__main__':
    unittest.main()
