import random


class TilesBag:

    def __init__(self, tiles):
        self.tiles = (tiles)
        random.shuffle(self.tiles)

    def getTiles(self, count):
        tiles_taken = []
        if count <= len(self.tiles):
            for _ in range(count):
                tiles_taken.append(self.tiles.pop())
        else:
            return "No hay suficientes fichas en la bolsa"  # Debe ser un raise
        random.shuffle(self.tiles)
        return tiles_taken

    def putTiles(self, tiles):
        self.tiles.extend(tiles)
        random.shuffle(self.tiles)

    def isTileBagEmpty(self):
        return len(self.tiles) == 0
