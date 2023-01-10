#!/usr/bin/python3
"""Function that checks if an object is an instance of specified class"""


def is_same_class(obj, a_class):
    """Returns True if ``obj`` is exactly an instance of ``a_class``

    Args:
        obj(object): The object to be checked.
        a_class (class): The specified class.
    """
    if not isinstance(obj, a_class):
        return (False)
    else:
        return (True)
