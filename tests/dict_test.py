import unittest
from src.simple_data_transformation_tools import dict_tools

class TestGetPath(unittest.TestCase):
    def test_get_path_key_not_in_dict(self):
        self.assertEqual(dict_tools.get_nested_value({'a': {'b': 1}}, ['a', 'c'], 2), 2)

    def test_get_path_key_not_in_dict(self):
        self.assertEqual(dict_tools.get_nested_value({'a': {'b': 1}}, ['a', 'c'], 2), 2)

    def test_get_path_key_in_dict(self):
        self.assertEqual(dict_tools.get_nested_value({'a': {'b': 1}}, ['a', 'b'], None), 1)

    def test_get_path_key_default_doesnt_override_none_value(self):
        self.assertEqual(dict_tools.get_nested_value({'a': {'b': None}}, ['a', 'b'], 1), None)

    def test_get_path_empty_path(self):
        self.assertEqual(dict_tools.get_nested_value({'a': {'b': None}}, [], 1), 1)

    def test_get_path_empty_dict(self):
        self.assertEqual(dict_tools.get_nested_value({}, ['a', 'b'], 1), 1)

    def test_get_path_none_path(self):
        self.assertEqual(dict_tools.get_nested_value({'a': {'b': None}}, None, 1), 1)

    def test_get_path_none_dict(self):
        self.assertEqual(dict_tools.get_nested_value(None, ['a', 'b'], 1), 1)

    def test_get_path_invalid_starting_dict(self):
        with self.assertRaises(AttributeError):
            dict_tools.get_nested_value(1, ['a', 'b'])


class TestSetPath(unittest.TestCase):
    # def __init__(self):
    #     self.data
    data = {'a': {'b': {'c': 1}}}
    path = ['a', 'b', 'c']

    def test_set_path_without_create(self):
        """
        Tests whether set_path will edit the value without creating the path.
        :return:
        """
        d = self.data.copy()
        dict_tools.set_nested_value(d, self.path, 2, False)
        self.assertEqual(dict_tools.get_nested_value(d, self.path), 2)

    def test_set_path_with_create_path_already_exists(self):
        """
        Tests whether set_path will edit the value of existing path
        even when create path is specified.
        :return:
        """
        d = self.data.copy()
        dict_tools.set_nested_value(d, self.path, 2, True)
        self.assertEqual(dict_tools.get_nested_value(d, self.path), 2)

    def test_set_path_with_create_path_does_not_exist(self):
        """
        Test will set nested value 4 layers deep with key 'd' to 3 even when d does not exist
        :return:
        """
        d = self.data.copy()
        path = ['a', 'b', 'c', 'd']
        dict_tools.set_nested_value(d, path, 3, True)
        self.assertEqual(dict_tools.get_nested_value(d, path), 3)

    def test_set_path_with_empty_path(self):
        """
        Test should do nothing to the dict
        :return:
        """
        d = self.data.copy()
        path = []
        dict_tools.set_nested_value(d, path, 3, True)
        self.assertEqual(d, self.data)

    def test_set_path_with_non_existent_first_key(self):
        d = self.data.copy()
        path = ['z','x']
        dict_tools.set_nested_value(d, path, 3, True)
        self.assertEqual(dict_tools.get_nested_value(d, path), 3)

    def test_set_path_with_none_value_and_create_path(self):
        d = {'a': {'b': None}}
        path = ['a','b','c']
        dict_tools.set_nested_value(d, path, 3, True)
        self.assertEqual(dict_tools.get_nested_value(d, path), 3)

    def test_set_path_with_none_value_and_do_not_create_path(self):
        d = {'a': {'b': None}}
        path = ['a','b','c']
        dict_tools.set_nested_value(d, path, 3, False)
        self.assertEqual(dict_tools.get_nested_value(d, ['a', 'b']), None)

    def test_set_path_with_empty_dict_with_create(self):
        d = {}
        dict_tools.set_nested_value(d, self.path, 3, True)
        self.assertEqual(dict_tools.get_nested_value(d, self.path), 3)

    def test_set_path_with_empty_dict_without_create(self):
        d = {}
        dict_tools.set_nested_value(d, self.path, 3, False)
        self.assertEqual(dict_tools.get_nested_value(d, self.path), None)

if __name__ == '__main__':
    unittest.main()