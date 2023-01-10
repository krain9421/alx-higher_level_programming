#!/usr/bin/python3
"""Functon that returns the list of available attributes and methods"""


def lookup(obj):
    list_of_attr = dir(obj)
    return (list_of_attr)
