#!/usr/bin/python3
"""This model defines a base class for all the classes in
    the project
"""


class Base:
    """Defines a Base class"""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base object

        Args:
            id (int): id of the object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
