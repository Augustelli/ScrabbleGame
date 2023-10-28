class Cell:

    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None  # Instancia de Tile
        self.used = False
