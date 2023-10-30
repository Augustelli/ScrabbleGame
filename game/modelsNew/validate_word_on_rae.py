dictionary_path = "game/modelsNew/dictionary.txt"

with open(dictionary_path, "r") as file:
    dictionary = set(word.strip() for word in file)

def validate_word_on_rae(word):
    return word.lower() in dictionary
