import os
import redis
import pickle

def saveScrabble(scrabble, nombre_partida):
    redis_host = os.environ.get('REDIS_HOST', 'redis')
    redis_client = redis.StrictRedis(host=redis_host, port=6379, db=0)

    clave_partida = f'scrabble_{nombre_partida}'
    scrabble_serializado = pickle.dumps(scrabble)
    redis_client.set(clave_partida, scrabble_serializado)

def loadScrabble(nombre_partida):
    redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

    clave_partida = f'scrabble_{nombre_partida}'
    scrabble_serializado = redis_client.get(clave_partida)
    if scrabble_serializado:
        scrabble = pickle.loads(scrabble_serializado)
        return scrabble

    else:
        print(f"No se encontró ninguna partida Scrabble con el nombre '{nombre_partida}' en Redis")
        return None


def returnOrCreatePlay(nombre_partida):
    if nombre_partida == "":
        return False
    partida_cargada = loadScrabble(nombre_partida)
    if partida_cargada:
        print(f"Cargando partida: {nombre_partida}")
        return partida_cargada
    else:
        print(f"La partida '{nombre_partida}' no existe. Creando una nueva partida...")
        return False