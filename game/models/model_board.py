from colorama import init, Fore
from game.configuration import coordenadas_multiplicadores, multiplicadores_valores
from .model_cell import Cell
from .model_tile import Tile


class Board():
    # La secuencia seria imprimir el tablero luego de haber hecho todas las acciones

    def add_tile(self, tile, row, column):
        if isinstance(self.board[row][column].letter, Tile):
            return "Celda ocupada"
        else:
            self.board[row][column].letter = tile

    def __init__(self):
        self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
        init(autoreset=True)
        for tipo, valores in coordenadas_multiplicadores.items():
            for i, j in valores:
                if i == 7 and j == 7:
                    self.board[i][j].add_letter = Tile("*", 0)
                self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])

    def get_tile(self, row, column):
        return self.board[row][column]

    def remove_tile(self, row, column):
        if (self.board[row][column].letter is not None):
            self.board[row][column].letter = None
        else:
            return "No hay ficha en la celda"

    def print_board(self):
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
