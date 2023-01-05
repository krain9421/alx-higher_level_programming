#!/usr/bin/python3
"""Rectangle class that defines a rectangle"""


class Rectangle:
    """Rectangle class

    Args:
        width (int): The width of the new rectangle
        height (int): The height of the new rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the current width of the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the current width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the current height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the current height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
