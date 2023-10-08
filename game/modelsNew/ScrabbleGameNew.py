from .BoardModel import Board
from .TileBagModel import TilesBag
from .PlayerModel import Player
from .TileModel import Tile
from .configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class Scrabble:
    def __init__(self, players_count):
        self.board = Board()
        self.tiles_bags = TilesBag(tiles)
        self.players = [Player(None, self.tiles_bags) for _ in range(players_count)]
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]
        self.skippedTimes = 0
        self.gameFinished = False

    def setPlayerName(self, name, index):
        self.players[index].name = name

    def __str__(self) -> str:
        players_info = "\n".join([f"- {player}" for player in self.players])

        return f"""
    * TileBag:
        - Cantidad de fichas: {len(self.tiles_bags.tiles)}
        - Fichas: {self.tiles_bags}

    * Jugadores:
        - Cantidad: {len(self.players)}
        - Index: {self.current_player_index}

    * Jugador Actual :
    {players_info}

    * Veces que se pasó el turno: {self.skippedTimes}

    * Juego terminado: {self.gameFinished}
"""

    def nextTurn(self):
        # Avanza al siguiente jugador en turno
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def passTurn(self):
        print("Paso turno")
        self.skippedTimes += 1
        self.nextTurn()

    def endGame(self):
        # Devuelve True si el juego terminó
        return (not self.tiles_bags.tiles) or (self.skippedTimes == 2*len(self.players))

    def changeTiles(self):
        print("Cambiar TIles")
        pass
