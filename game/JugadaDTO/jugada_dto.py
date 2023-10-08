from dataclasses import dataclass, field


@dataclass
class JugadaDto:
    pasarTurno: bool = False
    cambiarFichas: bool = False  # o puede ser la cantidad a cambiar
    fichas: list = field(default_factory=list)   # Voy a pasar las fichas que se van a jugar/cambiar
    posiciones: list = field(default_factory=list)   # [x, y]
    palabra: str = ""
    tilesACambiar: list = field(default_factory=list)   # ["A", "B", "C""]

    # Pasar los Tiles que quiero cambiar
    @staticmethod
    def intercambioDeFichas(fichasListado: list, fichasACambiar: list):
        return JugadaDto(cambiarFichas=True, fichas=fichasListado, tilesACambiar=fichasACambiar)

    @staticmethod
    def intercambioDeFichasACK():
        return JugadaDto(cambiarFichas=True)

    @staticmethod
    def pasarTurnoJugador():
        return JugadaDto(pasarTurno=True)

