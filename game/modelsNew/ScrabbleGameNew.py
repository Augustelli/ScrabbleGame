from colorama import Fore
from game.validate_word.validate_word_on_rae import validate_word_on_rae

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
    # 1 Validar palabra RAE
    # 2 Validar que el jugador tiene las fichas necesarias
    # 3 Validar que la palabra entre en el tablero
    # 4 Calcular puntos
    # 5 Pasar de turno
    def playWord(self, playedWord):
        print("ENTRO A PLAY WORD: "+playedWord)
        validWord = validate_word_on_rae(playedWord)
        if not validWord:
            print("La palabra no existe en la RAE.")
            return False  # Ver qué devolver
        positionAndDirection = input("Ingrese la posición y dirección de la palabra (ej: 1 1 h): ").split()

        row = int(positionAndDirection[0]) - 1
        column = int(positionAndDirection[1]) - 1
        direction = positionAndDirection[2]

        # Corroborar que la palabra entre en el tablero
        wordCanBePlaced = self.board.checkIfWordCanBePlaced(playedWord, row, column, direction)
        if wordCanBePlaced is not True:  # Checkear qué devolver para el user.
            print(wordCanBePlaced)
            return False
        # Ver qué tiles debo poner en el tablero para formar la palabra con los que tengo.
        tilesOnBoard = self.board.getLettersInRowColumn((row, column), direction)
        playerWordTiles=self.current_player.rack.returnTiles(playedWord)  # Tiles que tiene el jugador sobre la palabra jugada
        tilesPlayedWord = list()
        for letter in tilesOnBoard:
            for index in range(len(playerWordTiles)):
                if letter == tilesPlayedWord[index]:
                    tilesPlayedWord.pop(index)
                    break

        letterToPlay = []
        # Busca si tengo los tiles necesarios, sino devulevo False
        for tile in playerWordTiles:
            if tile.letter in tilesPlayedWord:
                letterToPlay.append(tile)
                tilesPlayedWord.remove(tile)
        if tilesPlayedWord:
            return False

        # Poner las fichas en el tablero
        self.board.addTilesToBoard(letterToPlay, row, column, direction)




    def nextTurn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]

    def passTurn(self):
        print("Paso turno")
        self.skippedTimes += 1
        self.nextTurn()

    def endGame(self):
        if (not self.tiles_bags.tiles) or (self.skippedTimes == 2*len(self.players)):
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

    def showTurnInfo(self):
        self.showBoard()
        self.showPlayerTiles()
        self.showPlayerPoints()

    def showPlayerTiles(self):
        tile_info = " | ".join([f"{tile.letter} {tile.value}" for tile in self.current_player.rack.tiles])
        print(f"| {tile_info} |")
        print()

    def showPlayerPoints(self):
        print("Puntajes:")
        for player in self.players:
            print(f" -> {player.name}: {player.points} pts")
        print()
    def showBoard(self):
        print(Fore.GREEN + "+---------" * 15 + "+")
        for row in self.board.board:
            formatted_row = []
            for cell in row:
                if isinstance(cell.letter, Tile):
                    # Si hay una letra asignada a la celda
                    if cell.letter is not None:
                        if len(cell.letter.letter) == 1:
                            formatted_row.append(
                                f"{Fore.GREEN}|   {Fore.YELLOW}{cell.letter.letter}{cell.letter.value:2d}   ")
                        else:
                            formatted_row.append(
                                f"{Fore.GREEN}|  {Fore.YELLOW}{cell.letter.letter}{cell.letter.value:2d}   ")
                # Si hay multiplicadores
                elif cell.multiplier != 1:
                    formatted_row.append(f"{Fore.CYAN}| x{(cell.multiplier)}{cell.multiplier_type :^6}")
                else:
                    formatted_row.append(f"{Fore.GREEN}|{Fore.WHITE:^14}")
            formatted_row.append(Fore.GREEN + "|")
            print("".join(formatted_row))
            print(Fore.GREEN + "+---------" * 15 + "+")
        print()
