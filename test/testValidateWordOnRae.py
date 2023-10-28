import unittest
from game.modelsNew.validate_word_on_rae import validate_word_on_rae
from unittest.mock import patch
import requests


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

    # @patch('requests.get')
    # def test_successful_request(self, mock_get):
    #     mock_response = mock_get.return_value
    #     mock_response.status_code = 200
    #     mock_response.text = 'El contenido de la página'
    #     result = validate_word_on_rae('palabra')
    #     self.assertTrue(result)
    #
    # @patch('requests.get')
    # def test_failed_request(self, mock_get):
    #     mock_get.side_effect = requests.exceptions.RequestException('Error simulado')
    #     result = validate_word_on_rae('lskdjlaskjlkdsajmñsalsald')
    #     self.assertFalse(result)
    #
    # @patch('requests.get')
    # def test_failed_status_code(self, mock_get):
    #     mock_response = mock_get.return_value
    #     mock_response.status_code = 404
    #     result = validate_word_on_rae('dfjkdsklfjdfjldksj')
    #     self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
