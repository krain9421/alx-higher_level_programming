#!/usr/bin/python3
"""Square class that defines a square."""


class Square:
    """Representation of square

    Args:
        size (int): The size of the new square.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        """Set the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for j in range(self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for l in range(self.__size):
                    print("#", end="")
                print("")
