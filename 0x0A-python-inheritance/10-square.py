#!/usr/bin/python3
"""Square class (subclass of Rectangle)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class representation"""

    def __init__(self, size):
        """Initialize a Square

        Args:
            size(int): Size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
