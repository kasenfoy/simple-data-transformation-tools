def get_path(dictionary: dict, path: list, default=None):
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
    return get_path(dictionary.get(path[0]), path[1:], default)


def get_path_list(dictionary: dict, path: list, default=None):
    raise NotImplemented
