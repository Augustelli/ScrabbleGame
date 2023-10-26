from models.model_tilebag import TilesBag
from models.model_board import Board
from models.model_player import Player
from models.model_tile import Tile
from modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
from game.modelsNew.validate_word_on_rae import validate_word_on_rae
import pdb


tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = TilesBag(tiles)
        self.players = [Player("") for _ in range(players_count)]
        self.current_player_index = 0
        self.current_player = self.players[self.current_player_index]

    def validate_word(self, word, location, orientation):
        valid_word = False
        enough_tiles = False
        enough_space = False

        # Validar que la palabra sea válida en la RAE
        valid_word = validate_word_on_rae(word)
        if not valid_word:

            return 'Palabra no existe en la RAE'
        # Validar que el jugador tiene las fichas necesarias
        tiles_available = self.current_player.tiles.copy()
        for letter in word:
            for i in range(len(tiles_available)):
                if tiles_available[i].letter == letter:
                    tiles_available.remove(tiles_available[i])
                    enough_tiles = True
                    break
            else:
                enough_tiles = False
                return 'Faltan tiles.'

        # Validar que la palabra entre en el tablero
        x, y = location
        if orientation == "v":
            if y + len(word) <= 15:
                enough_space = all(self.board.board[x][y + i].letter is None for i in range(len(word)))
        elif orientation == "h":
            if x + len(word) <= 15:
                enough_space = all(self.board.board[x + i][y].letter is None for i in range(len(word)))

        return valid_word and enough_tiles and enough_space

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]

    def end_game(self):
        return not self.bag_tiles.tiles

    def put_words(self, word, position, direction):
        x, y = position

        if direction == "h":
            for tile in word:
                self.board.board[x][y].letter = Tile(tile, "1")
                y += 1
        elif direction == "v":
            for tile in word:
                self.board.board[x][y].letter = Tile(tile, "1")
                x += 1

        return "Palabras colocadas con éxito."

    def get_words(self, word, location, orientation):
        x, y = location
        possible_words = []
        if orientation == "h":
            for i in range(len(word)):
                new_word = self.get_word_in_direction(word, (x + i, y), "v")
                if new_word:
                    possible_words.append(new_word)
        elif orientation == "v":
            for i in range(len(word)):
                new_word = self.get_word_in_direction(word, (x, y + i), "h")
                if new_word:
                    possible_words.append(new_word)

        return possible_words

    def get_word_in_direction(self, word, location, orientation):
        x, y = location
        word_length = len(word)
        possible_word = ""
        if orientation == "h":
            for i in range(word_length):
                cell = self.board.board[x][y + i]
                if cell.letter is not None:
                    possible_word += cell.letter.letter
                else:
                    break
        elif orientation == "v":
            for i in range(word_length):
                cell = self.board.board[x + i][y]
                if cell.letter is not None:
                    possible_word += cell.letter.letter
                else:
                    break

        return possible_word

    # Verificar si el jugador puede jugar una palabra
    def can_play_word(self):
        word_to_be_played, position, orientation = self.current_player.next_play
        current_player_tiles = self.current_player.tiles.copy()
        # Palabra válida en la RAE
        valid_word = validate_word_on_rae(word_to_be_played)
        if not valid_word:
            return f"La palabra {word_to_be_played} no existe en la RAE"
        list_letters_in_row_column = self.board.get_letters_in_row_column(position, orientation)
        # Fichas necesarias para jugar la palabra
        list_letters_word_to_be_played = list(word_to_be_played)
        list_letters_required = [letter for letter in list_letters_in_row_column if letter not in list_letters_word_to_be_played]

        for letter_requiered in list_letters_required:
            for letter_player in current_player_tiles:
                if letter_requiered == letter_player.letter:
                    list_letters_required.remove(letter_player.letter)
                    break
        if list_letters_required:
            return f"{self.current_player.name} no tiene las fichas necesarias para jugar la palabra {word_to_be_played}"
        # Verificar si la palabra puede ser jugada en la posición

        len_word_to_be_played = len(word_to_be_played)
        if orientation == "h":
            if position[0] + (len_word_to_be_played - 1) <= 14:
                for i in range(len_word_to_be_played):
                    if self.board.board[position[0]][position[1] + i].letter is not None:
                        return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque hay una ficha en la posición {position[0]},{position[1] + i}"  # noqa
            else:
                return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque no hay espacio suficiente"  # noqa
        elif orientation == "v":
            if position[0] + (len_word_to_be_played - 1) <= 14:
                for i in range(len_word_to_be_played):
                    if self.board.board[position[0] + i][position[1]].letter is not None:
                        return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque hay una ficha en la posición {position[0] + i},{position[1]}"  # noqa
            else:
                return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque no hay espacio suficiente"  # noqa
        # Verificar si al jugar la palabra, las palabras multiples palabras son válidas en la RAE
        # Añadimos provisoriamente la palabra a la posición y orientación dada
        self.put_words([word_to_be_played], position, orientation)
        multiword_list = self.board.get_multiple_words_by_played_word(word_to_be_played, position, orientation)
        for word in multiword_list:
            # Quito las letras que se añadieron provisoriamente
            if not validate_word_on_rae(word):
                return f"La palabra {word_to_be_played} no puede ser jugada en la posición {position} con la orientación {orientation} porque la palabra {word} no existe en la RAE"
        # for i in range(len_word_to_be_played):
        #     if orientation == "h":
        #         self.board.board[position[0]][position[1] + i].letter = None
        #     elif orientation == "v":
        #         self.board.board[position[0] + i][position[1]].letter = None
        # pdb.set_trace()
        return True


if __name__ == '__main__':

    juego = ScrabbleGame(2)
    jugador1 = juego.players[0]
    jugador2 = juego.players[1]
    jugador1.tiles = [Tile("H", 1), Tile("A", 1), Tile("L", 1), Tile("O", 1)]
    jugador1.next_play = ["HALO", [7, 7], "h"]
    print(juego.can_play_word() is True)
    pdb.set_trace()
