import pdb

from .configuration import coordenadas_multiplicadores, multiplicadores_valores
from .CellModel import Cell
from .TileModel import Tile
from colorama import init
from .configuration import puntaje_por_letra


class Board:

    def __init__(self):
        self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
        init(autoreset=True)
        for tipo, valores in coordenadas_multiplicadores.items():
            for i, j in valores:
                if i == 7 and j == 7:
                    self.board[i][j].letter = Tile("*", 0)
                self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])

    def getTilesOnCell(self, row, column):
        return self.board[row][column].letter

    def addTileOnCell(self, tile, row, column):
        if isinstance(self.board[row][column].letter, Tile):
            pass
        else:
            self.board[row][column].letter = tile

    def checkIfWordCanBePlaced(self, word, row, column, direction):
        len_word_to_be_played = len(word)
        if direction == "h":
            if column + (len_word_to_be_played - 1) <= 14:
                for i in range(len_word_to_be_played):
                    if self.board[row][column + i].letter is not None:
                        return True  # noqa
                    elif i == len_word_to_be_played - 1:
                        return False
            else:
                return f"La palabra {word} no puede ser jugada en la posición con la orientación {direction} porque no hay espacio suficiente"  # noqa
        elif direction == "v":
            if row + (len_word_to_be_played - 1) <= 14:
                for i in range(len_word_to_be_played):
                    if self.board[row + i][column].letter is not None:
                        return True  # noqa
                    elif i == len_word_to_be_played - 1:
                        return False
            else:
                return f"La palabra {word} no puede ser jugada en la posición con la orientación {direction} porque no hay espacio suficiente"  # noqa
    def getLettersInRowColumn(self, position, orientation):
        letters = ""
        x, y = position
        if orientation == "h":
            for i in range(15):
                if self.board[x][i].letter is not None:
                    letters += self.board[x][i].letter.letter
                else:
                    letters += "_"
        elif orientation == "v":
            for i in range(15):
                if self.board[i][y].letter is not None:
                    letters += self.board[i][y].letter.letter
                else:
                    letters += "_"
        word_left = letters[:position[1]][::-1].split("_")[0][::-1]
        word_right = letters[position[1]:].split("_")[0]
        full_word = word_left + word_right
        return ([letter for letter in full_word])

    # Tile tiene que llegar ordenado de como va en la palabra
    # [row, column, direction] -> specs
    def addTilesToBoard(self, letterToPlay, specs, board, playedWord):
        row, column, direction = specs
        lenWord = len(playedWord)
        if direction == 'h':
            for i in range(lenWord):
                if board.getTilesOnCell(row, column + i) is None:
                    board.addTileOnCell(letterToPlay[0], row, column + i)
                    letterToPlay.pop(0)

        elif direction == 'v':
            for i in range(lenWord):
                if board.getTilesOnCell(row + i, column) is None:
                    board.addTileOnCell(letterToPlay[0], row + i, column)
                    letterToPlay.pop(0)

        return self.calculateWordPoints([row, column], direction, board, lenWord)

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
        return  points*multiplier

    def calculateWordPoints(self, position, direction, board, lengWord):
        points = 0
        if direction == 'h':
            points = self.calculateHorizontalPoints(position, board, lengWord)
        elif direction == 'v':
            points = self.calculateVertical(position, board, lengWord)
        return points


