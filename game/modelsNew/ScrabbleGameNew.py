from .validate_word_on_rae import validate_word_on_rae

from .BoardModel import Board
from .TileBagModel import TilesBag
from .PlayerModel import Player
from .TileModel import Tile
from .configuration import puntaje_por_letra, cantidad_de_fichas_por_letra


tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class Scrabble(object):
    def __init__(self, players_count, tiles):
        self.board = Board()
        self.tiles_bags = TilesBag(tiles)
        self.players = [Player(None, self.tiles_bags) for _ in range(players_count)]
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]
        self.skippedTimes = 0
        self.gameFinished = False
        self.firstPlay = True

    def setPlayerName(self, name, index):
        self.players[index].name = name

    # 1 Validar palabra RAE
    # 2 Validar que el jugador tiene las fichas necesarias
    # 3 Validar que la palabra entre en el tablero
    # 4 Calcular puntos
    def wordCanBePlayed(self, playedWord, row, column, direction):
        if not self.firstPlay:
            wordCanBePlaced = self.board.checkIfWordCanBePlaced(playedWord, row, column, direction)
        else:
            wordCanBePlaced = (
                    (direction == "h" and column + len(playedWord) - 1 <= 14)
                    or (direction == "v" and row + len(playedWord) - 1 <= 14)
            )
        return wordCanBePlaced

    def checkForMissingTiles(self, playedWord, row, column, direction):
        tilesOnBoard = [Tile(letter, puntaje_por_letra[letter]) for letter in self.board.getLettersInRowColumn((row, column), direction)]
        playerWordTiles = self.current_player.rack.returnTiles(playedWord)
        tilesPlayedWord = [Tile(letter, puntaje_por_letra[letter]) for letter in playedWord.upper()]
        lettersToPlay = []
        missingLetters = tilesPlayedWord.copy()

        for letter in tilesOnBoard:
            if letter in tilesPlayedWord:
                missingLetters.remove(letter)

        for letter in tilesPlayedWord:
            if letter in playerWordTiles:
                lettersToPlay.append(letter)
                playerWordTiles.remove(letter)
                missingLetters.remove(letter)

        self.current_player.rack.addTiles(playerWordTiles)

        return lettersToPlay, missingLetters
    def playWord(self, playedWord):
        if not validate_word_on_rae(playedWord):
            print("La palabra no existe en la RAE.")
            return False

        positionAndDirection = input("Ingrese la posición y dirección de la palabra  COLUMNA  FILA  DIRECCIÓN : (ej: 1 1 h): ").split()

        column = int(positionAndDirection[0]) - 1
        row = int(positionAndDirection[1]) - 1
        direction = positionAndDirection[2].lower()
        wordCanBePlaced = self.wordCanBePlayed(playedWord, row, column, direction)
        if wordCanBePlaced is False:
            print("La palabra no cabe en el tablero")
            return False

        lettersToPlay, missingLetters = self.checkForMissingTiles(playedWord, row, column, direction)
        if missingLetters:
            print("No tiene las fichas necesarias para jugar la palabra.")
            return False
        # Poner las fichas en el tablero
        self.current_player.points += self.board.addTilesToBoard(lettersToPlay, [row, column, direction], self.board, playedWord)
        self.current_player.addTiles()
        self.nextTurn()
        self.skippedTimes = 0
        self.firstPlay = False

    def nextTurn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]

    def passTurn(self):
        self.skippedTimes += 1
        self.nextTurn()

    def endGame(self):
        if (self.tiles_bags.isTileBagEmpty()) or (self.skippedTimes == 2*len(self.players)):
            self.gameFinished = True
            print("Juego terminado")

    def changeTiles(self):
        self.skippedTimes = 0
        while True:
            result = self.current_player.changeTiles()
            if result is not False:
                self.nextTurn()
                break
            else:
                print("La entrada es inválida. Por favor, ingrese las letras de las fichas que desea cambiar nuevamente.")

    def showTurnInfo(self):
        self.showBoard()
        print("\n")
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
        for i, row in enumerate(self.board.board, start=1):
            self.printRowNumber(i)
            self.printCells(row)

    def printRowNumber(self, row_number):
        print(f"{row_number:2d} ", end=" ")

    def printCells(self, cells) :
        for cell in cells:
            if cell.letter:
                self.printLetterCell(cell)
            else:
                self.printMultiplierCell(cell)
        print()

    def printLetterCell(self, cell):
        print(f"| {cell.letter.letter} {cell.letter.value}  ", end="")

    def printMultiplierCell(self, cell):
        if cell.multiplier_type == "word":
            print(f"| {cell.multiplier}W   ", end="")
        elif cell.multiplier_type == "letter":
            print(f"| {cell.multiplier}L   ", end="")
        else:
            print("|      ", end="")



