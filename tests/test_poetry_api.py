import unittest
from utils.api_client import APIClient


class TestPoetryAPI(unittest.TestCase):

    def test_search_by_author_and_invalid_output_field(self):
        response = APIClient.get('/author/Dickinson/wrongfield')
        self.assertIn('"reason":"wrongfield output field not available. Only author, title, lines, and linecount allowed."', response.text)
        self.assertIn('"status":"405"', response.text)

    def test_search_by_author_and_valid_and_invalid_output_fields(self):
        response = APIClient.get('/author/Dickinson/author,wrongfield')
        self.assertIn('"reason":"wrongfield output field not available. Only author, title, lines, and linecount allowed."', response.text)
        self.assertIn('"status":"405"', response.text)

    def test_invalid_output_format(self):
        response = APIClient.get('/author/Dickinson/all.invalid')
        self.assertIn('"status":"405"', response.text)
        self.assertIn('"reason":"invalid output format not available. Only text and json allowed."', response.text)

if __name__ == '__main__':
    unittest.main()
