#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if (type(text) not in [str]):
        raise TypeError("text must be a string")

    i = 0
    size = len(text)
    while i < size and text[i] == ' ':
        i += 1

    while i < size:
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < size and text[i] == ' ':
                i += 1
            continue
        i += 1
