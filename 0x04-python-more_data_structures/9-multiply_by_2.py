#!/usr/bin/python3
# A function that returns
#   a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    for key, val in a_dictionary.items():
        a_dictionary[key] = val * 2
    return a_dictionary
