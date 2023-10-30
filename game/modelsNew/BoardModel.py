import pdb

from .configuration import coordenadas_multiplicadores, multiplicadores_valores
from .CellModel import Cell
from .TileModel import Tile
from colorama import init
from .configuration import puntaje_por_letra


class Board:

    def setAttr(self, tipo, valores):
        for i, j in valores:
            if i == 7 and j == 7:
                self.board[i][j].letter = Tile("*", 0)
            self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])
    def __init__(self):
        self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
        init(autoreset=True)
        for tipo, valores in coordenadas_multiplicadores.items():
            self.setAttr(tipo, valores)

    def getTilesOnCell(self, row, column):
        return self.board[row][column].letter

    def addTileOnCell(self, tile, row, column):
        if isinstance(self.board[row][column].letter, Tile):
            pass
        else:
            self.board[row][column].letter = tile

    def checkCanBePlacedHorizontal(self, word, row, column):
        len_word_to_be_played = len(word)
        if column + (len_word_to_be_played - 1) <= 14:
            for i in range(len_word_to_be_played):
                if self.board[row][column + i].letter is not None:
                    return True
                elif i == len_word_to_be_played - 1:
                    return False
        else:
            return False

    def checkCanBePlacedVertical(self,word, row, column):
        len_word_to_be_played = len(word)
        if row + (len_word_to_be_played - 1) <= 14:
            for i in range(len_word_to_be_played):
                if self.board[row + i][column].letter is not None:
                    return True  # noqa
                elif i == len_word_to_be_played - 1:
                    return False
        else:
            return False
    def checkIfWordCanBePlaced(self, word, row, column, direction):
        if direction == "h":
            return self.checkCanBePlacedHorizontal(word, row, column) is not False
        elif direction == "v":
            return self.checkCanBePlacedVertical(word, row, column) is not False

    def getLettersInRow(self, letters, row):
        for i in range(15):
            if self.board[row][i].letter is not None:
                letters += self.board[row][i].letter.letter
            else:
                letters += "_"
        return letters

    def formatLettersRowColumn(self, letters, position):
        word_left = letters[:position[1]][::-1].split("_")[0][::-1]
        word_right = letters[position[1]:].split("_")[0]
        return word_left + word_right
    def getLettersInRowColumn(self, position, orientation):
        letters = ""
        x, y = position
        if orientation == "h":
            letters = self.getLettersInRowOrColumn(letters, x, is_row=True)
        elif orientation == "v":
            letters = self.getLettersInRowOrColumn(letters, y, is_row=False)

        full_word = self.formatLettersRowColumn(letters, position)
        return ([letter for letter in full_word])

    def getLettersInRowOrColumn(self, letters, index, is_row=True):
        for i in range(15):
            cell = self.board[index][i] if is_row else self.board[i][index]
            if cell.letter is not None:
                letters += cell.letter.letter
            else:
                letters += "_"
        return letters

    def addTilesToRow(self, letterToPlay, specs, board, playedWord):
        for i in range(len(playedWord)):
            if board.getTilesOnCell(specs[0], specs[1] + i) is None:
                board.addTileOnCell(letterToPlay[0], specs[0], specs[1] + i)
                letterToPlay.pop(0)
    def addTilesToColumn(self, letterToPlay, specs, board, playedWord):
        for i in range(len(playedWord)):
            if board.getTilesOnCell(specs[0] + i, specs[1]) is None:
                board.addTileOnCell(letterToPlay[0], specs[0] + i, specs[1])
                letterToPlay.pop(0)

    # Tile tiene que llegar ordenado de como va en la palabra
    # [row, column, direction] -> specs
    def addTilesToBoard(self, letterToPlay, specs, board, playedWord):
        row, column, direction = specs
        if direction == 'h':
            self.addTilesToRow(letterToPlay, specs, board, playedWord)
        elif direction == 'v':
            self.addTilesToColumn(letterToPlay, specs, board, playedWord)
        return self.calculateWordPoints([row, column], direction, board, len(playedWord))

    def calculateLettersPoints(self, cell, multiplier, points):
        if (cell.multiplier_type == "word") and (cell.used is False):
            multiplier *= cell.multiplier
            cell.used = True
        if (cell.multiplier_type == "letter") and (cell.used is False):
            points += puntaje_por_letra[cell.letter.letter] * cell.multiplier
            cell.used = True
        else:
            points += puntaje_por_letra[cell.letter.letter]

        return points, multiplier

    def calculateHorizontalPoints(self, position, board, lengWord):
        row, column = position
        points = 0
        multiplier = 1
        for i in range(lengWord):
            cell = board.board[row][column+i]
            points, multiplier = board.calculateLettersPoints(cell, multiplier, points)
        return points*multiplier

    def calculateVertical(self, position, board, lengWord):
        row, column = position
        points = 0
        multiplier = 1
        for i in range(lengWord):
            cell = board.board[row+i][column]
            points, multiplier = board.calculateLettersPoints(cell, multiplier, points)
        return points*multiplier

    def calculateWordPoints(self, position, direction, board, lengWord):
        points = 0
        if direction == 'h':
            points = self.calculateHorizontalPoints(position, board, lengWord)
        elif direction == 'v':
            points = self.calculateVertical(position, board, lengWord)
        return points


