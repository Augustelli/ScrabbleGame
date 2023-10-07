class Player:
    
    def __init__(self, name):
        self.tiles = []
        self.name = name if name is not None else f"Jugador{random.randint(0, 99):02d}"
        self.points = 0
        self.next_play = ["", [0, 0], "h"]
        # [ palabra a jugar, [fila, columna], direccion ]