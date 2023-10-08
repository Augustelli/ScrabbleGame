from dataclasses import dataclass


@dataclass
class JugadaDto:
    pasarTurno: bool = False
    cambiarFichas: bool = False  # o puede ser la cantidad a cambiar
    fichas: list = []  # Voy a pasar las fichas que se van a jugar/cambiar
    posiciones: list = []  # [x, y]
    palabra: str = ""
