from modelsNew.ScrabbleGameNew import Scrabble
import os
import pdb
import time


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
    # Seteo el nombre a los jugadoresi
    for i in range(num_players):
        print(f"Jugador {i+1}: {player_names[i]}")
        juego.setPlayerName(player_names[i], i)
    time.sleep(1)
    os.system("clear")
    while not juego.gameFinished:
        print('-'*50)
        print("Para realizar jugadas: \n\t- Ingrese la palabra que desea jugar.\n\t- Si desea cambiar fichas, ingrese 'change'.\n\t- Si desea pasar el turno, ingrese 'skip o  ENTER'.")
        print('-'*50)
        juego.endGame()
        print("\n")
        print(f"Turno de {juego.current_player.name}: ")
        # juego.showTurnInfo()
        accion_ingresada = input("Ingrese una acción: ").lower()
        print("\n")
        print('-'*50)
        pdb.set_trace()
        if accion_ingresada == "skip" or accion_ingresada == "":
            juego.passTurn()
        elif accion_ingresada == "change":
            juego.current_player.exchangeTiles()
        else:
            juego.playWord(accion_ingresada)
        # os.system("clear")


if __name__ == "__main__":
    main()
