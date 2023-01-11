#!/usr/bin/python3
"""Function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using JSON
        representation.

    Args:
        my_obj(object): Object file.
        filename(string): text file to be written into.
    """

    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)
