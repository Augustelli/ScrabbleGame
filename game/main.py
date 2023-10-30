import pdb

from game.redisModule.redis import returnOrCreatePlay, saveScrabble
from game.modelsNew.ScrabbleGameNew import Scrabble
from game.modelsNew.TileModel import Tile
from game.modelsNew.configuration import puntaje_por_letra, cantidad_de_fichas_por_letra
import os
import time
import redis

tiles = [Tile(letter, puntaje_por_letra[letter]) for letter, count in cantidad_de_fichas_por_letra.items() for _ in range(count)]
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


def get_num_players():
    while True:
        num_players = input("Seleccione la cantidad de jugadores (2-4): ")
        if is_valid_num_players(num_players):
            return int(num_players)
        print("Ingrese un número válido (2-4).")

def is_valid_num_players(num_players):
    if num_players.isdigit():
        num_players = int(num_players)
        if 2 <= num_players <= 4:
            return True
    return False


def get_player_names(num_players):
    player_names = []
    for i in range(num_players):
        name = input(f"Ingrese el nombre del Jugador {i + 1}: ")
        player_names.append(name)
    return player_names
def display_info(juego):
    print('-' *150)
    print(
        "Para realizar jugadas: \n\t- Ingrese la palabra que desea jugar.\n\t- Si desea cambiar fichas, ingrese 'change'.\n\t- Si desea pasar el turno, ingrese 'skip o  ENTER'.\n\t- Para guardar la partida y salir 'SAVE''")
    print('-' * 150)
    print(f"Turno de {juego.current_player.name}: ")
    print("       1      2      3      4      5      6      7      8      9      10     11     12     13     14     15   ")
    print("    --------------------------------------------------------------------------------------------------------")
    juego.showTurnInfo()

def change_tiles(juego):
    juego.current_player.exchangeTiles()
    juego.nextTurn()
    juego.skippedTimes = 0

def set_player_names(juego, num_players, player_names):
    for i in range(num_players):
        print(f"Jugador {i+1}: {player_names[i]}")
        juego.setPlayerName(player_names[i], i)
    time.sleep(1)
    os.system("clear")

def load_or_create_game(play_name):
    if play_name:
        played_game = returnOrCreatePlay(play_name)
        if played_game:
            print("Partida cargada correctamente.")
            return played_game
    num_players = get_num_players()
    player_names = get_player_names(num_players)
    juego = Scrabble(num_players, tiles)
    set_player_names(juego, num_players, player_names)
    return juego

def clear_screen():
    os.system("clear")
def main():
    print("¡Bienvenido a Scrabble!")
    play_name = input("¿Tienes una partida guardada? Retómala con su nombre, sino presiona ENTER: ")
    juego = load_or_create_game(play_name)
    while not juego.gameFinished:
        display_info(juego)
        action = input("Ingrese una acción: ").lower()
        if action == "skip" or action == "":
            juego.passTurn()
        elif action == "change":
            change_tiles(juego)
        elif action == "save":
            saveScrabble(juego)
            break  # Terminar el juego
        else:
            juego.playWord(action)
        clear_screen()
        juego.endGame()



if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()
