#!/usr/bin/python3
"""Function that checks if an object is an instance of, or if an
    object is an instance of class that inherited from, specified class
"""


def is_same_class(obj, a_class):
    """Returns True if ``obj`` is an instance of, or
    instance of class that inherited from ``a_class``

    Args:
        obj(object): The object to be checked.
        a_class (class): The specified class.
    """
    return isinstance(obj, a_class)
