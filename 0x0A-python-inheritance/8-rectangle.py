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
