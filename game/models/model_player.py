

class Player:
    def __init__(self, name, dictionary):
        self.tiles = []
        self.name = name
        self.points = 0
        self.next_word = ""
        self.dictionary = dictionary

    def get_tile_from_tilebag(self, tilebag, count):
        tiles_recived = tilebag.take(count)
        if isinstance(tiles_recived, str):
            return tiles_recived
        else:
            self.tiles.extend(tiles_recived)

    def create_word(self, tiles):
        self.next_word = "".join(tile.letter for tile in tiles)
        if self.next_word.lower() in self.dictionary.dictionary:
            self.next_word = self.next_word
            return True
        else:
            return 'Palabra inválida'

    def get_player_tile_index(self, letter):
        for tile in self.tiles:
            if letter == tile.letter:
                return self.tiles.index(tile)
        return None

    def put_tiles_on_board(self, row, column, direction, board):
        if direction == "v":
            for i, letter in enumerate(self.next_word):
                tile_index = self.get_player_tile_index(letter.upper())
                tile_to_add = self.tiles[tile_index]
                board.add_tile(tile_to_add, row + i, column)
                self.tiles.pop(tile_index)
        elif direction == "h":
            for i, letter in enumerate(self.next_word):
                tile_index = self.get_player_tile_index(letter.upper())
                tile_to_add = self.tiles[tile_index]
                board.add_tile(tile_to_add, row, column + i)
                self.tiles.pop(tile_index)
        self.next_word = ""

    def calculate_word_value(self, word):
        value = 0
        for letter in word:
            for tile in self.tiles:
                if tile.letter == letter:
                    value += tile.value
                    break
        return value

    def find_all_valid_words_on_board(self, board):
        words_found = set()

        # Búsqueda Horizontal (Filas)
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

        # Búsqueda Vertical (Columnas)
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
