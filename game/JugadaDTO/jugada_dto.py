from dataclasses import dataclass, field


@dataclass
class JugadaDto:
    pasarTurno: bool = False
    cambiarFichas: bool = False
    fichas: list = field(default_factory=list)
    posiciones: list = field(default_factory=list)
    palabra: str = ""
    tilesACambiar: list = field(default_factory=list)
