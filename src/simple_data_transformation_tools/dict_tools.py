def get_nested_value(dictionary: dict, path: list, default=None):
    """
    Navigates down a deeply nested dictionary by recursively iterating over each key in the path arg.

    :param dictionary: A dictionary of data iterable by keys from the path arg
    :param path: A list of str keys used to navigate down the dict. For dicts with lists in the path see get_path_list()
    :param default: The default value to return if the key is not found. If value is found but is None, default is ignored
    :return: any - The value in the dict or default.
    """

    # Confirm path is valid.
    if path is None or len(path) == 0:
        return default

    # Base Case - None type dict - Key is not in dictionary
    if dictionary is None:
        return default

    # Base Case - Final element
    if len(path) == 1:
        return dictionary.get(path[0], default)

    # Recurse
    return get_nested_value(dictionary.get(path[0]), path[1:], default)


def get_nested_values_with_list(dictionary: dict, path: list, default=None):
    raise NotImplemented


def set_nested_value(dictionary: dict, path: list, value, create_path: bool = True):
    """
    Sets a value at the path in a dictionary.

    :param dictionary: The dict that we will be setting our value into at path
    :param path: The list of keys we will navigate to set our value
    :param value: The value to insert at our path in the dict
    :param create_path: Will create the dict path if it does not exist. Default True
    :return: None
    """

    # Validation - First run - Path is empty
    if len(path) == 0:
        return

    # Validation - First run - Dict is None
    if dictionary is None:
        if create_path:
            dictionary = {}

    # Validation - Only continue if key exists or user asked to create path
    if path[0] not in dictionary.keys() and create_path == False:
        return

    # Base Case - final element in Path
    # At this stage we know to create the path as a result of the previous condition
    if len(path) == 1:
        dictionary[path[0]] = value
        return

    # Make sure a value exists for us to recurse down into.
    # Setting a new key will only work if it's a dict.
    # Validation - Dict is None or dictionary is not a dict
    if dictionary.get(path[0]) is None or type(dictionary[path[0]]) != dict:
        # Validation - User wants to create the path
        if create_path:
            # To avoid AttributeError on .keys() call in recursions - set the dict to {}
            dictionary[path[0]] = {}
        else:
            # Else the user doesn't wish to create the path - do nothing.
            return

    # Recurse - going down the dict
    set_nested_value(dictionary[path[0]], path[1:], value, create_path)


def set_nested_values_with_list(self):
    raise NotImplemented