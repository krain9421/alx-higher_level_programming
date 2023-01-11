#!/usr/bin/python3
import json
"""Function that returns the JSON representation of
    and object (string)
"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj(object): object
    """

    return (json.dumps(my_obj))
