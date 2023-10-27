from .RackModel import Rack
from JugadaDTO.jugada_dto import JugadaDto
import random


class Player:

    def __init__(self, name, tilebag):
        self.rack = Rack(tilebag)
        self.name = name if name is not None else f"Jugador{random.randint(0, 99):02d}"
        self.points = 0

    def __str__(self):
        # Convierte cada ficha (Tile) a cadena antes de unirlas
        rack_str = ', '.join(str(tile) for tile in self.rack.tiles)
        return f"Nombre: {self.name}\n  - Puntuación: {self.points}\n  - Rack: {rack_str}"


    def exchangeTiles(self):
        print("ENTRO A PLAYER")
        incorrecto = True
        while incorrecto:
            tilesToExchangeStr = input("Ingrese las fichas que desea cambiar separadas por espacios: ").upper()
            tilesToExchangeStr = tilesToExchangeStr.split()
            tilesOnRack = self.rack.getTilesOnRack()

            for letter in tilesToExchangeStr:
                if letter not in [tile.letter for tile in tilesOnRack]:
                    print(f"La letra '{letter}' no está en su rack.")
                    break
            else:
                incorrecto = False

        dtoCambio = JugadaDto(cambiarFichas=True, tilesACambiar=list(tilesToExchangeStr))

        return self.rack.changeTiles(dtoCambio)

    def addTiles(self):
        self.rack.addTileToPlayer()
    def isRackEmpty(self):
        return self.rack.isEmpty()
