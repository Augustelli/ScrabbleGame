class Cell:

    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier  # 1, 2, 3
        self.multiplier_type = multiplier_type  # w / l
        self.letter = None  # Instancia de Tile
        self.used = False

    def addLetter(self, letter):
        self.letter = letter

    def calculateCellValue(self):
        # Calcula el valor por letra
        if self.letter is None:
            return 0
        if self.multiplier_type.lower() == 'l' and self.used is False:
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

    def __str__(self):
        if self.letter is None:
            return f"  - {self.multiplier} {self.multiplier_type} -"
        else:
            return f"  - {self.multiplier} {self.multiplier_type} {self.letter} -"
