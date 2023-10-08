import random


class TilesBag:

    def __init__(self, tiles):
        self.tiles = list(tiles)
        random.shuffle(self.tiles)

    def __str__(self):
        # Convierte cada ficha (Tile) a cadena antes de unirlas
        tile_str = ', '.join(str(tile) for tile in self.tiles)
        return f"TileBag:\n  - Cantidad de fichas: {len(self.tiles)}\n  - Fichas: {tile_str}"

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
