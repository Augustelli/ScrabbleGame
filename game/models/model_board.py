from colorama import init, Fore
from .configuration import coordenadas_multiplicadores, multiplicadores_valores, puntaje_por_letra
from .model_cell import Cell
from .model_dictionary import Dictionary
from .model_tile import Tile


class Board():

    def __init__(self):
        self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
        init(autoreset=True)
        for tipo, valores in coordenadas_multiplicadores.items():
            for i, j in valores:
                if i == 7 and j == 7:
                    self.board[i][j].add_letter = Tile("*", 0)
                self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])
        self.dictionary = Dictionary()

    def get_tile(self, row, column):
        return self.board[row][column]

    def add_tile(self, tile, row, column):
        if isinstance(self.board[row][column].letter, Tile):
            return "Celda ocupada"
        else:
            self.board[row][column].letter = tile

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

    def validate_word(self, word):
        return self.dictionary.is_valid_word(word)

    def calculate_word_points(self, word, row, column, direction):
        word_points = 0
        word_multiplier = 1

        for i, letter in enumerate(word):
            if direction == "h":
                cell = self.board[row][column + i]
            elif direction == "v":
                cell = self.board[row + i][column]

            letter_value = puntaje_por_letra[letter]

            if cell.multiplier_type == "word":
                word_multiplier *= cell.multiplier
            word_points += letter_value

        word_points *= word_multiplier
        return word_points

    # Tengo que llamar solo a esta funcion para cada jugador en el turno
    def calculate_turn_points(self, player, played_word, row, column, direction):
        main_word_points = self.calculate_word_points(played_word, row, column, direction)
        player.points += main_word_points

        return main_word_points

    def find_all_valid_words_on_board(self, board):
        words_found = set()

        for row in board:
            word = ""
            for cell in row:
                if cell.letter is not None:
                    word += cell.letter.letter
                elif len(word) > 1:
                    words_found.add(word)
                    word = ""
            if len(word) > 1:
                words_found.add(word)

        num_columns = len(board[0])
        for col in range(num_columns):
            word = ""
            for row in range(len(board)):
                cell = board[row][col]
                if cell.letter is not None:
                    word += cell.letter.letter
                elif len(word) > 1:
                    words_found.add(word)
                    word = ""
            if len(word) > 1:
                words_found.add(word)

        return list(words_found)