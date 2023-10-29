from game.JugadaDTO.jugada_dto import JugadaDto  # noqa
import pdb  # noqa


class Rack:

    def __init__(self, tilebag) -> None:
        self.tiles = tilebag.getTiles(7)
        self.maxTiles = 7
        self.tilebag = tilebag


    def addTiles(self, tiles: list):
        self.tiles.extend(tiles)

    def addTileToPlayer(self):
        self.tiles.extend(self.tilebag.getTiles(7 - len(self.tiles)))
    """
    Doy una palabra y me devuelve los tiles que necesito para formarla
    Si no tengo alguno, devuelve los que tenga
    """

    def lookForLetter(self, letter, tileToReturn):
        for tile in self.tiles:
            if tile.letter == letter:
                tileToReturn.append(tile)
                self.tiles.remove(tile)
                break
    def returnTiles(self, word):
        tileToReturn = []
        for letter in word.upper():
            self.lookForLetter(letter, tileToReturn)
        return tileToReturn

    # Método de intercambio con Tilebag
    def changeTiles(self, dtoCambio):
        tilesToTilebag = list()
        for letter in dtoCambio.tilesACambiar:
            for tile in self.tiles:
                if tile.letter == letter:
                    tilesToTilebag.append(tile)
                    self.tiles.remove(tile)
                    break
        nuevosTiles = self.tilebag.getTiles(len(tilesToTilebag))
        self.tiles.extend(nuevosTiles)
        self.tilebag.putTiles(tilesToTilebag)
        return JugadaDto(cambiarFichas=True)

    def getTilesOnRack(self):
        return self.tiles

    def isEmpty(self):
        return len(self.tiles) == 0
    