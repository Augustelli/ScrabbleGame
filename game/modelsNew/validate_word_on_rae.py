import requests
from bs4 import BeautifulSoup

with open("game/modelsNew/dictionary.txt", "r") as file:
    contenido = file.read()
    palabras = contenido.split()


def validate_word_on_rae(word):
    if not word:
        return False
    if word.lower() in palabras:
        return True
    else:
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'
            }

            url = f'https://dle.rae.es/{word}?=form'
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                contenido = response.text
                soup = BeautifulSoup(contenido, 'html.parser')
                no_word_found_phrases = [
                    f"Aviso: La palabra {word} no está en el Diccionario.",
                    "Aviso: La palabra no está en el Diccionario."
                ]
                for phrase in no_word_found_phrases:
                    if phrase in soup.get_text():
                        return False
                return True

            else:
                print(f'La solicitud no fue exitosa. Código de estado: {response.status_code}')
                return False

        except requests.exceptions.RequestException as e:
            print(f'Error al hacer la solicitud: {e}')
            return False
