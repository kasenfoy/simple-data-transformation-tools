# Simple Data Transformation Tools
## Overview
Simple Data Transformation Tools (SDTT) is a simplistic Python package for primarily working with dicts, JSON and CSV data. 

## Highlights
`get_path` Navigate a deeply nested dictionary to find a value using a [path] similar to the default `.get()` method this allows you to find deeply nested values without having to loop/check validity of the dictionary. Example:

```python
from src.simple_data_transformation_tools.dict_tools import get_path 

data={
  "employee": {
    "first_name": "Fake",
    "last_name": "Name",
    "location": {
      "country": "A Real Country",
      "address": "123 A Street"
    }
  },
  "job": {
    "title": "Important Person"
  }
}

country = get_path(data, ["employee", "location", "country"], "Default - No Country")

print(country)

# Output 
"A Real Country"
```

This is useful for a number of reasons, the two primary being 
1. If your JSON/dict is non-standard and varies. Perhaps not all records have an `employee` or `location` key, and you don't know this ahead of time. `get_path` accounts for this and will not error if the key does not exist, it will simply return your default value.
2. When used with `JsonMap` defined in `src.simple_data_transformation_tools.json_map`You can use the builtin `JsonMap` or roll your own method by creating a dictionary of keys, paths, and defaults. This allows you to serialize your objects into and out of dicts/JSON. It is particularly useful when converting dicts/JSON to CSV.


### Supported Transformations
* JSON to CSV
* CSV to JSON

### Fun Helper modules
* dicts
