from src.simple_data_transformation_tools.dict_tools import get_nested_value, set_nested_value


class TransformerMap:
    """
    modify the map to make it a dictionary of key=header value={path: [], default: str}
    # TODO Add path disambiguation JSON to CSV (location->state and location->province map to same column)
    """

    def __init__(self):
        """
        The map property is the primary focus here it is used for mapping the transformation from dict/json to csv.
        The map should be formatted like so:

        :return:
        """
        self.data_map = {}

    def add_row(self, header: str, path: list, default=None):
        """
        Helper function to format the map correctly.
        NOTE - Will override an existing key/header
        Not explicitly necessary, the map can be manually modified/built.
        :param header: The column name/key in the dict
        :param path: The list of string keys used to map the JSON
        :param default: The default value that will be filled if none is found
        :return: None
        """
        print(self.data_map)
        self.data_map[header] = {"path": path, "default": default}

    def delete_row(self, header: str):
        """
        Helper function - removes header from the map
        Not explicitly necessary, the map can be manually modified/built.
        :param header:
        :return: None
        """
        self.data_map.pop(header)

    def get_headers(self):
        """
        Helper - Retrieves the top level keys used for the map
        These are the names of the CSV columns in the order of the map.
        :return: list[]
        """
        return list(self.data_map.keys())

    def dict_to_array(self, dictionary: list[dict], include_header_column: bool = True):
        """
        Transforms a dictionary into an array of arrays using the map.

        :param dictionary:
        :param include_header_column:
        :return: 2D list [[]] first layer is rows second layer is values.
        """
        records = []

        # Include headers as first row.
        if include_header_column:
            records.append(self.get_headers())

        # Iterate over each Dict record
        for row in dictionary:
            record_row = []

            # Iterate over each header in the map
            for header in self.get_headers():
                path = self.data_map.get(header).get('path')
                default = self.data_map.get(header).get('default')

                # Retrieve the value from the dict using the path
                value = get_nested_value(row, path, default)

                # Add the record to our row
                record_row.append(value)

            # Append the row to our records
            records.append(record_row)

        return records

    def array_to_dict(self, records_list: list[list], headers: list):
        """
        Transforms a list of lists into a dict representation using the map.

        Note that headers must be in the same order as the values in records_list
        :param records_list: - List of Lists
        :param headers:
        :return: List of Dicts [{}]
        """

        records = []

        # Iterate over each row in the records
        for row in records_list:

            record = {}

            # Iterate over each header and find its path in the map
            for i in range(len(headers)):
                map_entry = self.data_map.get(headers[i])

                # Skip if header does not exist
                # TODO log warning
                if map_entry is None:
                    continue

                # Use the path to regenerate the JSON
                set_nested_value(record, map_entry.get('path'), row[i])

            # Append the record to records
            records.append(record)

        return records
