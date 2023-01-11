#!/usr/bin/python3
"""Function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string to a text and returns the number of
        characters added.

    Args:
        filename(string): name of the file to be written.
        text(string): text to be written to the file.
    """

    with open(filename, 'a', encoding="utf-8") as myFile:
        """Printing the contents of the file"""
        return (myFile.write(text))
