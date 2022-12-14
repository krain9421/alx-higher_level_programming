#!/usr/bin/python3
"""Function that checks that inherited (directly or indirectly) from
    the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if ``obj`` is an instance of
    a class that inherited from ``a_class``

    Args:
        obj(object): The object to be checked.
        a_class (class): The specified class.
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
