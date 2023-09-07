class Cell:

    def __init__(self, multiplier, multiplier_type):

        self.multiplier = multiplier
        self.multiplier_type = multiplier_type  # word / letter
        self.letter = None  # Instancia de Tile

    def add_letter(self, letter):
        self.letter = letter

    def calculate_value(self):
        # Calcula el valor por letra
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
