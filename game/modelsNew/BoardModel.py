import pdb

from .configuration import coordenadas_multiplicadores, multiplicadores_valores
from .CellModel import Cell
from .TileModel import Tile
from colorama import init, Fore
from .configuration import puntaje_por_letra


class Board():

    def __init__(self):
        self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
        init(autoreset=True)
        for tipo, valores in coordenadas_multiplicadores.items():
            for i, j in valores:
                if i == 7 and j == 7:
                    self.board[i][j].letter = Tile("*", 0)
                self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])

    def __str__(self) -> str:
        return f"{self.board}"

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
                return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque no hay espacio suficiente"  # noqa
        elif direction == "v":
            if row + (len_word_to_be_played - 1) <= 14:
                for i in range(len_word_to_be_played):
                    if self.board[row + i][column].letter is not None:
                        return True  # noqa
                    elif i == len_word_to_be_played - 1:
                        return False
            else:
                return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque no hay espacio suficiente"  # noqa
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

    def showBoard(self):
        print(Fore.GREEN + "+---------" * 15 + "+")
        for row in self.board:
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
                    formatted_row.append(f"{Fore.CYAN}| x{(cell.multiplier)}{(cell.multiplier_type):^6}")
                else:
                    formatted_row.append(f"{Fore.GREEN}|{Fore.WHITE:^14}")
            formatted_row.append(Fore.GREEN + "|")
            print("".join(formatted_row))
            print(Fore.GREEN + "+---------" * 15 + "+")

    # Tile tiene que llegar ordenado de como va en la palabra
    def addTilesToBoard(self, letterToPlay, row, column, direction, board):
        lenWord = len(letterToPlay)
        if direction == 'h':
            for i in range(lenWord):
                if len(letterToPlay) == 0:
                    break
                elif board.getTilesOnCell(row, column + i) is None:
                    board.addTileOnCell(letterToPlay[0], row, column + i)
                    letterToPlay.pop(0)

        elif direction == 'v':
            for i in range(lenWord):
                if len(letterToPlay) == 0:
                    break
                elif board.getTilesOnCell(row + i, column) is None:
                    board.addTileOnCell(letterToPlay[0], row + i, column)
                    letterToPlay.pop(0)

        return self.calculateWordPoints(row, column, direction, board, lenWord)
    def calculateWordPoints(self, row, column, direction, board, lengWord):
        points = 0
        multiplier = 1
        if direction == 'h':
            for i in range(lengWord):
                cell = board.board[row][column+i]
                points, multiplier = board.calculateLettersPoints(cell, multiplier, points)

        elif direction == 'v':
            for i in range(lengWord):
                cell = board.board[row + i][column]
                points, multiplier = board.calculateLettersPoints(cell, multiplier, points)

        return points*multiplier
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