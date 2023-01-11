#!/usr/bin/python3
"""Function that creates an Object from a JSON file."""
import json


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file'

    Args:
        filename(string): text file
    """

    with open(filename, "r") as myFile:
        my_obj = json.load(myFile)
        return (my_obj)
