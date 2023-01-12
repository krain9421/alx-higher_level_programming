#!/usr/bin/python3
"""Function that adds all arguments to a python list.."""
import sys


if __name__ == "__main__":
    saveToJSON = __import__('5-save_to_json_file').save_to_json_file
    loadFromJSON = __import__('6-load_from_json_file').load_from_json_file

    try:
        argv = loadFromJSON("add_item.json")
    except FileNotFoundError:
        argv = []
    argv.extend(sys.argv[1:])
    saveToJSON(argv, "add_item.json")
