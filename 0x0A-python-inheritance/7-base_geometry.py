#!/usr/bin/python3
"""BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class"""

    def area(self):
        """Function that raises and exception

        Args:
            self(object)
        """
        raise Exception("area() is not implemented")

    def integer_validation(self, name, value):
        """Validates a value to be an integer

        Args:
            name(str): Parameter name
            value(int): Parameter value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
