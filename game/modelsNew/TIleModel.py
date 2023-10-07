class Tile():
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    def __str__(self) -> str:
        return f"{self.letter} ({self.value})"
