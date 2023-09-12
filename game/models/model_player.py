class Player:
    def __init__(self, name):
        self.tiles = []
        self.name = name
        self.points = 0
        self.next_word = ""

    def get_tile_from_tilebag(self, tilebag, count):
        tiles_recived = tilebag.take(count)
        if isinstance(tiles_recived, str):
            return tiles_recived
        else:
            self.tiles.extend(tiles_recived)

    def create_word(self, word: str):
        new_word = ""
        for letter in word:
            if self.get_player_tile_index(letter.upper()) is not None:
                new_word += letter.upper()
                if len(new_word) == len(word):
                    self.next_word = new_word
            else:
                return "No tienes las fichas necesarias para crear esa palabra"

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

    def get_tile_value(self, letter):
        for tile in self.tiles:
            if letter == tile.letter:
                return tile.value
        return None
