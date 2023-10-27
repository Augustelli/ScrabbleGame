class Cell:

    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier  # 1, 2, 3
        self.multiplier_type = multiplier_type  # w / l
        self.letter = None  # Instancia de Tile
        self.used = False
