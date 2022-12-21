#!/usr/bin/python3
"""Square class that defines a square."""


class Square:
    """Representation of square

    Args:
        size (int): The size of the new square.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current area of the square."""
        return (self.__size ** 2)
