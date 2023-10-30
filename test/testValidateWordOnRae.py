import unittest
from game.modelsNew.validate_word_on_rae import validate_word_on_rae

class TestValidateWordOnRae(unittest.TestCase):

    def test_valid_word(self):
        result = validate_word_on_rae("computadora")
        self.assertTrue(result)

    def test_invalid_word(self):
        result = validate_word_on_rae("xyzabc")
        self.assertFalse(result)

    def test_word_with_related_entry(self):
        result = validate_word_on_rae("holaa")
        self.assertFalse(result)

    def test_empty_word(self):
        result = validate_word_on_rae("")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
