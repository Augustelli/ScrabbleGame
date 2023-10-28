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
    def returnTiles(self, word):
        word = word.upper()
        tileToReturn = []
        for letter in word:
            for tile in self.tiles:
                if tile.letter == letter:
                    tileToReturn.append(tile)
                    self.tiles.remove(tile)
                    break
        return tileToReturn

    # def returnTiles(self, word):
    #     word = word.upper()  # Convertimos la palabra a mayúsculas para que coincida con las fichas
    #     tileToReturn = []
    #
    #     for letter in word:
    #         for tile in self.tiles:
    #             if tile.letter == letter:
    #                 tileToReturn.append(tile)
    #                 self.tiles.remove(tile)
    #                 break  # Rompemos el bucle interno después de encontrar una ficha
    #
    #     return tileToReturn

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
    