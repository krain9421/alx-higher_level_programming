#!/usr/bin/python3
"""Program that reads a text file and prints out the contents to stdout"""


def read_file(filename=""):
    """Prints out the contents of a text file to the stdout

    Args:
        filename (string): name of the file to read
    """
    if not isinstance(filename, str):
        raise TypeError("File name must be a string!")

    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
