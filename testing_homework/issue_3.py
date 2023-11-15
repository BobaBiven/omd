import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):

    def test_cities(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
            ]
        actual = fit_transform(cities)
        self.assertEqual(actual, expected)

    def test_weather(self):
        weather = [
            'cold', 'cold', 'warm',
            'cold', 'hot', 'hot',
            ]
        expected = [
            ('cold', [0, 0, 1]),
            ('cold', [0, 0, 1]),
            ('warm', [0, 1, 0]),
            ('cold', [0, 0, 1]),
            ('hot', [1, 0, 0]),
            ('hot', [1, 0, 0])
        ]
        actual = fit_transform(weather)
        self.assertEqual(actual, expected)

    def test_not_none(self):
        arr = []
        actual = fit_transform(arr)
        self.assertIsNotNone(actual)

    def test_letters_in(self):
        letters = ['a', 'b', 'c', 'c', 'c', 'c']
        result = fit_transform(letters)
        incorrect_set = [('d', [1, 1, 1])]
        self.assertNotIn(incorrect_set, result)

    def test_raise(self):
        try:
            fit_transform(1)
        except Exception:
            self.assertRaises(Exception)
