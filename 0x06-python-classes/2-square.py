#!/usr/bin/python3
"""Square class that defines a square."""


class Square:
    """Representation of square

    Args:
        size (int): The size of the new square.
    """

    def __init__(self, size=0):
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
            int(size)
        except ValueError:
            raise TypeError("size must be an integer")
        finally:
            self.__size = size
