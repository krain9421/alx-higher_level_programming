#!/usr/bin/python3
"""This model defines a rectangle class that inherits from
    Base
"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a rectangle class

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): The x position of the rectangle
            y (int): The y position of the retangle
            id (int): The id of the object
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Gets the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        self.__width = value

    @property
    def height(self):
        """Gets the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        self.__height = value

    @property
    def x(self):
        """Gets the value of x position"""
        return (self.__X)

    @x.setter
    def x(self, value):
        """Sets the value of x position"""
        self.__x = value

    @property
    def y(self):
        """Gets the value of y position"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the value of y position"""
        self.__y = value
