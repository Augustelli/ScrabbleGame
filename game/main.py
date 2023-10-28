from .modelsNew.ScrabbleGameNew import Scrabble
from .modelsNew.TileModel import Tile
from .modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
import os
import time

tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]

def get_num_players():
    while True:
        num_players = input("Seleccione la cantidad de jugadores (2-4): ")
        if num_players.isdigit():
            num_players = int(num_players)
            if 2 <= num_players <= 4:
                return num_players
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
    juego = Scrabble(num_players, tiles)
    # Seteo el nombre a los jugadoresi
    for i in range(num_players):
        print(f"Jugador {i+1}: {player_names[i]}")
        juego.setPlayerName(player_names[i], i)
    time.sleep(1)
    os.system("clear")
    while not juego.gameFinished:
        print('-'*350)
        print("Para realizar jugadas: \n\t- Ingrese la palabra que desea jugar.\n\t- Si desea cambiar fichas, ingrese 'change'.\n\t- Si desea pasar el turno, ingrese 'skip o  ENTER'.")
        print('-'*350)
        print(f"Turno de {juego.current_player.name}: ")
        print("     1         2         3         4         5         6         7         8         9         10       11        12         13        14        15  ")
        juego.showTurnInfo()
        accion_ingresada = input("Ingrese una acción: ").lower()
        if accion_ingresada == "skip" or accion_ingresada == "":
            juego.passTurn()
        elif accion_ingresada == "change":
            juego.current_player.exchangeTiles()
            juego.nextTurn()
            juego.skippedTimes = 0
        else:
            juego.playWord(accion_ingresada) # Palabra a jugar
            time.sleep(1.5)
        os.system("clear")
        juego.endGame()


if __name__ == "__main__":
    main()
