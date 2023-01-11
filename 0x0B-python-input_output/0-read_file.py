#!/usr/bin/python3
"""Read File"""


def read_file(filename=""):
    """ Function reads a text file (UTF8) and prints it to stdout

    Args:
        filename (string): name of the file to read
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
