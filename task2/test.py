import unittest
from unittest.mock import patch
from solution import (fetch_main_categories, fetch_animals_from_category,
                      count_animals_by_letter)

class TaskTestCase(unittest.TestCase):

    @patch('solution.requests.get')
    def test_fetch_main_categories(self, mock_get):
        mock_get.return_value.text = '''
            <a href="/wiki/ABC">Аб</a>
            <a href="/wiki/DEF">Бв</a>
            <a href="/wiki/GHI">Аб</a>
        '''
        categories = fetch_main_categories()
        self.assertEqual(categories, ['Аб', 'Бв'])

    @patch('solution.requests.get')
    def test_fetch_animals_from_category(self, mock_get):
        mock_get.return_value.text = '''
            <a href="/wiki/Абботины" title="Абботины">Абботины</a>
            <a href="/wiki/Абелизавр" title="Абелизавр">Абелизавр</a>
        '''
        animals = fetch_animals_from_category('Аб')
        self.assertEqual(len(animals), 2)
        self.assertEqual(animals[0][0], 'Абботины')

    def test_count_animals_by_letter(self):
        with patch('solution.fetch_animals_from_category') as mock_fetch:
            mock_fetch.side_effect = lambda cat: [
                ('Абелизавр', 'Абелизавр'),
                ('Абботины', 'Абботины')
            ] if cat == 'Аб' else []

            counts = count_animals_by_letter(['Аб', 'Бв'])
            self.assertEqual(counts['А'], 2)

if __name__ == '__main__':
    unittest.main()
