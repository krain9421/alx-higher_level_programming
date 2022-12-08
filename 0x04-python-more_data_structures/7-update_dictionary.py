#!/usr/bin/python3
# A function that replaces or
#   adds key/value in a dictionary.
def update_dictionary(a_dictionary, key, value):
    if key:
        a_dictionary[key] = value
    return a_dictionary
