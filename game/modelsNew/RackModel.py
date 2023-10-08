class Rack:

    def __init__(self, tilebag) -> None:
        self.tiles = list(tilebag.getTiles(7))
        self.maxTiles = 7

    def __str__(self):
        tile_str = ', '.join(str(tile) for tile in self.tiles)
        return f"Rack:\n  - Cantidad de fichas: {len(self.tiles)}\n  - Fichas: {tile_str}"

    def addTiles(self, tiles: list):
        self.tiles.extend(tiles)

    """
    Doy una palabra y me devuelve los tiles que necesito para formarla
    Si no tengo alguno, devuelve los que tenga
    """
    def returnTiles(self, word):
        tileToReturn = []
        for letter in word:
            for tile in self.tiles:
                if tile.letter == letter:
                    tileToReturn.append(tile)
                    self.tiles.remove(tile)
                    break
        return tileToReturn
