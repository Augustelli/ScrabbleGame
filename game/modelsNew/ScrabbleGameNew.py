from .BoardModel import Board
from .TileBagModel import TilesBag
from .PlayerModel import Player
from .TileModel import Tile
from .configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class Scrabble(object):
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
        - Index: {self.current_player_index} | {self.current_player.name}

    * Jugador Actual :
    {players_info}

    * Veces que se pasó el turno: {self.skippedTimes}

    * Juego terminado: {self.gameFinished}
"""

    def nextTurn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]

    def passTurn(self):
        print("Paso turno")
        self.skippedTimes += 1
        self.nextTurn()

    def endGame(self):
        if (not self.tiles_bags.tiles) or (self.skippedTimes == 2*len(self.players) - 1):
            self.gameFinished = True
            print("Juego terminado")

    def changeTiles(self):
        print("ENTRO A CAMBIAR FICHAS")
        self.skippedTimes = 0
        while True:
            print("ENTRO A WHILE")
            result = self.current_player.changeTiles()
            if result is not False:
                print("YA CAMBIO LAS FICHAS")
                self.nextTurn()
                print("PASO DE TURNO")
                break
            else:
                print("La entrada es inválida. Por favor, ingrese las letras de las fichas que desea cambiar nuevamente.")


class TerminalInfo(Scrabble):

    def __init__(self, players_count):
        super().__init__(players_count)

    def showTurnInfo(self):
        pass