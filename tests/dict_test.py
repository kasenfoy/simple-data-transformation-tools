import unittest
from src.simple_data_transformation_tools import dict_tools


class TestDictMethods(unittest.TestCase):

    def test_get_path_key_not_in_dict(self):
        self.assertEqual(dict.get_path({'a': {'b': 1}}, ['a', 'c'], 2), 2)

    def test_get_path_key_in_dict(self):
        self.assertEqual(dict.get_path({'a': {'b': 1}}, ['a', 'b'], None), 1)

    def test_get_path_key_default_doesnt_override_none_value(self):
        self.assertEqual(dict.get_path({'a': {'b': None}}, ['a', 'b'], 1), None)

    def test_get_path_empty_path(self):
        self.assertEqual(dict.get_path({'a': {'b': None}}, [], 1), 1)

    def test_get_path_empty_dict(self):
        self.assertEqual(dict.get_path({}, ['a', 'b'], 1), 1)

    def test_get_path_none_path(self):
        self.assertEqual(dict.get_path({'a': {'b': None}}, None, 1), 1)

    def test_get_path_none_dict(self):
        self.assertEqual(dict.get_path(None, ['a', 'b'], 1), 1)

if __name__ == '__main__':
    unittest.main()