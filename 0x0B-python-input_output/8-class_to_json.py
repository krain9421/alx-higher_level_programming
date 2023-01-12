#!/usr/bin/python3
"""Class to JSON function"""



def class_to_json(obj):
    """Returns the dictionary representation of a data
        structure

        Args:
            obj(object): object file
    """
    return (obj.__dict__)
