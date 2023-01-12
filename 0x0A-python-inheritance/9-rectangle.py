#!/usr/bin/python3
"""Rectangle class that inherits from BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangl based on ``BaseGeometry``"""

    def __init__(self, width, height):
        """Initializes a new Rectangle

        Args:
            width(int): Width of the rectangle
            height(int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the string representation of
            a rectangle
        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
