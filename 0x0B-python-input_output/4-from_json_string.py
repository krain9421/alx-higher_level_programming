#!/usr/bin/python3
"""Function that returns an object represented by
    a JSON string
"""
import json


def from_json_string(my_str):
    """Returns the JSON representation of an object (string)

    Args:
        my_str(string): string
    """

    return (json.load(my_str))
