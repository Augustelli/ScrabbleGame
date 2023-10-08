# class Cell:
#     def __init__(self, row, col):
#         self.row = row
#         self.col = col
#         self.tile = None  # La ficha que se encuentra en esta casilla (si alguna)


# class Board:
#     def __init__(self, rows, cols):
#     self.board = [[Cell(1, "") for _ in range(15)] for _ in range(15)]
#     init(autoreset=True)
#     for tipo, valores in coordenadas_multiplicadores.items():
#         for i, j in valores:
#             if i == 7 and j == 7:
#                 self.board[i][j].add_letter = Tile("*", 0)
#             self.board[i][j] = Cell(multiplicadores_valores[tipo], tipo.split("_")[1])

# class Rack:
#     def __init__(self):
#         self.tiles = []
        

# class ScrabbleGame:
#     def __init__(self, num_players):
#         self.board = Board(rows=15, cols=15)
#         self.players = [Player(f"Jugador {i+1}") for i in range(num_players)]
#         self.current_player = self.players[0]  # El jugador actual
#         self.dictionary = Dictionary()  # Puedes implementar esta clase para validar palabras

#     def switch_player(self):
#         # Lógica para cambiar al siguiente jugador en turno
#         pass

# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.rack = Rack()
#         self.score = 0

#     def make_move(self, game, move):
#         # Lógica para que el jugador realice una jugada
#         pass

# class Dictionary:
#     def __init__(self):
#         # Cargar una lista de palabras válidas
#         self.word_list = set(["PALABRA1", "PALABRA2", "PALABRA3"])  # Ejemplo de lista de palabras válidas

# # Ejemplo de uso
# game = ScrabbleGame(num_players=2)
