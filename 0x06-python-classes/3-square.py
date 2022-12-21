#!/usr/bin/python3
"""Square class that defines a square."""


class Square:
    """Representation of square

    Args:
        size (int): The size of the new square.
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """Returns the current area of the square."""
            return (self.__size ** 2)
