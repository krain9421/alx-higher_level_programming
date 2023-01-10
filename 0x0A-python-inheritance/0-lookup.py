#!/usr/bin/python3
"""Functon that returns the list of available attributes and methods"""


def lookup(obj):
    """Returns the list of attribute and methods

    Args:
        obj(object): The object to be checked.
    """
    list_of_attr = dir(obj)
    return (list_of_attr)
