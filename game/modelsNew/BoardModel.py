from .configuration import coordenadas_multiplicadores, multiplicadores_valores
from .CellModel import Cell
from .TileModel import Tile
from colorama import init, Fore


class Board():

    def __init__(self):
        self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
        init(autoreset=True)
        for tipo, valores in coordenadas_multiplicadores.items():
            for i, j in valores:
                if i == 7 and j == 7:
                    self.board[i][j].add_letter = Tile("*", 0)
                self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])

    def __str__(self) -> str:
        return f"{self.board}"

    def getTilesOnCell(self, row, column):
        return self.board[row][column].letter

    def addTileOnCell(self, tile, row, column):
        if isinstance(self.board[row][column].letter, Tile):
            return "Celda ocupada"
        else:
            self.board[row][column].letter = tile

    def checkIfWordCanBePlaced(self, word, row, column, direction):
        len_word_to_be_played = len(word)
        if direction == "h":
            if column + (len_word_to_be_played - 1) <= 14:
                for i in range(len_word_to_be_played):
                    if self.board[row][column + i].letter is not None:
                        return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque hay una ficha en la posición {position[0]},{position[1] + i}"  # noqa
            else:
                return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque no hay espacio suficiente"  # noqa
        elif direction == "v":
            if row + (len_word_to_be_played - 1) <= 14:
                for i in range(len_word_to_be_played):
                    if self.board[row + i][column].letter is not None:
                        return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque hay una ficha en la posición {position[0] + i},{position[1]}"  # noqa
            else:
                return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque no hay espacio suficiente"  # noqa
        return True

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
                            formatted_row.append(f"{Fore.GREEN}|   {Fore.YELLOW}{cell.letter.letter}{cell.letter.value:2d}   ")
                        else:
                            formatted_row.append(f"{Fore.GREEN}|  {Fore.YELLOW}{cell.letter.letter}{cell.letter.value:2d}   ")
                # Si hay multiplicadores
                elif cell.multiplier != 1:
                    formatted_row.append(f"{Fore.CYAN}| x{(cell.multiplier)}{(cell.multiplier_type):^6}")
                else:
                    formatted_row.append(f"{Fore.GREEN}|{Fore.WHITE:^14}")
            formatted_row.append(Fore.GREEN + "|")
            print("".join(formatted_row))
            print(Fore.GREEN + "+---------" * 15 + "+")
