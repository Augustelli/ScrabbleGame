class Dictionary():

    def __init__(self) -> None:
        self.dictionary = set()
        with open('game/dictionary.txt', 'r') as f:
            for line in f:
                self.dictionary.add(line.strip())

    def is_valid_word(self, word):
        return word.lower() in self.dictionary
