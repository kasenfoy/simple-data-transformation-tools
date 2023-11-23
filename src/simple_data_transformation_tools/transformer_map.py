class TransformerMap:
    """
    modify the map to make it a dictionary of key=header value={path: [], default: str}
    """
    def __int__(self):
        """
        The map property is the primary focus here it is used for mapping the transformation from dict/json to csv.
        The map should be formatted like so:

        {
            "prop_name": {"path": ["first level", "second level", "etc."], "default: "default_value"}
            "prop_nam2": {"path": ["first leve2", "second leve2", "et2."], "default: "default_valu2"}
            ...
        }

        :return:
        """
        self.map = {}

    def add_row(self, header: str, path: list, default=None):
        """
        Helper function to format the map correctly. Not necessary, the map can be manually modified/built.
        :param header:
        :param path:
        :param default:
        :return:
        """
        self.map[header] = {path, default}
