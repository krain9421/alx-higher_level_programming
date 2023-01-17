#!/usr/bin/python3
"""This model defines a Square class that inherits from
    Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square class

        Args:
            size (int): The size of the side of the square
            x (int): The x position of the square
            y (int): The y position of the square
            id (int): The id of the object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the printable representation
            of the Square instance
        """
        rect = "[Square] (" + str(self.id)
        rect += ") " + str(self.__x) + "/"
        rect += "" + str(self.__y) + " - "
        rect += "" + str(self.__width) + ""
        return (rect)
