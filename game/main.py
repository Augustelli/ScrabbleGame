import pdb
import curses
from modelsNew.ScrabbleGameNew import Scrabble
import npyscreen


class JuegoForm(npyscreen.Form):
    def create(self):
        # Obtenemos el tamaño de la pantalla
        max_y, max_x = self.useable_space()

        # Ventana izquierda para el tablero (ocupará la mitad izquierda de la pantalla)
        width = max_x // 2
        height = max_y - 4
        self.tablero = self.add(npyscreen.BoxTitle, name="Tablero", max_width=width, max_height=height, rely=2, relx=2)

        # Ventana superior derecha para la tabla de puntos
        self.tabla_puntos = self.add(npyscreen.BoxTitle, name="Tabla de Puntos", rely=2, relx=width + 2, max_height=10, max_width=-2)
        self.tabla_turnos = self.add(npyscreen.BoxTitle, name="Turnos", rely=2, relx=width + 2, max_height=10, max_width=-2)

        # Ventana inferior derecha para las fichas del jugador
        self.fichas_jugador = self.add(npyscreen.BoxTitle, name="Fichas del Jugador", rely=12, relx=width + 2, max_height=10, max_width=-2)

        # Campo de entrada para las acciones del jugador
        self.accion_jugador = self.add(npyscreen.MultiLineEditableBoxed, name="Acción del Jugador", rely=22, relx=width + 2, max_width=-2)

    def while_waiting(self, juego: Scrabble):
        accion_ingresada = self.accion_jugador.value.lower()
        if accion_ingresada == "skip":
            juego.passTurn()
        elif accion_ingresada == "change":
            juego.changeTiles()
        else:
            juego.playWord(accion_ingresada)
            self.accion_jugador.value = ""


def get_num_players():
    while True:
        try:
            num_players = int(input("Seleccione la cantidad de jugadores (2-4): "))
            if 2 <= num_players <= 4:
                return num_players
            else:
                print("Ingrese un número válido (2-4).")
        except ValueError:
            print("Ingrese un número válido (2-4).")


def get_player_names(num_players):
    player_names = []
    for i in range(num_players):
        name = input(f"Ingrese el nombre del Jugador {i + 1}: ")
        player_names.append(name)
    return player_names


def main():
    print("¡Bienvenido a Scrabble!")

    num_players = get_num_players()
    player_names = get_player_names(num_players)
    juego = Scrabble(num_players)
    # Seteo el nombre a los jugadores
    for i in range(num_players):
        print(f"Jugador {i+1}: {player_names[i]}")
        juego.setPlayerName(player_names[i], i)

    curses.wrapper(run_game)

def run_game(stdscr):
    app = npyscreen.NPSAppManaged()
    form = JuegoForm()
    form.edit()
if __name__ == "__main__":
    main()
