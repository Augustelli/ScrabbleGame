import unittest
from game.models.model_dictionary import Dictionary


class TestDictionary(unittest.TestCase):

    def setUp(self):
        self.dictionary = Dictionary()

    def test_load_dictionary(self):
        self.assertTrue(isinstance(self.dictionary.dictionary, set))
        self.assertGreater(len(self.dictionary.dictionary), 0)
        self.assertEqual(len(self.dictionary.dictionary), 88)

    def test_is_valid_word_valid(self):
        self.assertTrue(self.dictionary.is_valid_word("hombre"))
        self.assertTrue(self.dictionary.is_valid_word("cama"))
        self.assertTrue(self.dictionary.is_valid_word("Hombre"))

    def test_is_valid_word_invalid(self):
        self.assertFalse(self.dictionary.is_valid_word("xyz"))
        self.assertFalse(self.dictionary.is_valid_word("invalid"))


if __name__ == '__main__':
    unittest.main()
