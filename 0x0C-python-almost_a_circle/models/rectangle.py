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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """Gets the value of width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the value of height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the value of x position"""
        return (self.__X)

    @x.setter
    def x(self, value):
        """Sets the value of x position"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the value of y position"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the value of y position"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle
            instance
        """
        return (self.__width * self.__height)

    def display(self):
        """Prints out the Rectangle instance
            with the character `#`
        """
        for i in range(self.__y):
            print("")
        for h in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """Returns the printable representation
            of the Rectangle instance
        """
        rect = "[Rectangle] (" + str(self.id)
        rect += ") " + str(self.__x) + "/"
        rect += "" + str(self.__y) + " - "
        rect += "" + str(self.__width) + "/"
        rect += "" + str(self.__height) + ""
        return (rect)

    def update(self, *args):
        """Updates attributes of the Rectangle
            instance
        """
        count = 0
        for arg in args:
            count += 1
            if count == 1:
                self.id = arg
            elif count == 2:
                self.__width = arg
            elif count == 3:
                self.__height = arg
            elif count == 4:
                self.__x = arg
            elif count == 5:
                self.__y = arg
