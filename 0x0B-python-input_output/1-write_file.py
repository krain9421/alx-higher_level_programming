#!/usr/bin/python3
"""Function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text and returns the number of
        characters written.

    Args:
        filename(string): name of the file to be written.
        text(string): text to be written to the file.
    """

    with open(filename, 'w', encoding="utf-8") as myFile:
        """Printing the contents of the file"""
        return (myFile.write(text))
