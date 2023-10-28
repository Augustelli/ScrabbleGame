class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.letter == other.letter
        return False
