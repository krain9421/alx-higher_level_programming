#!/usr/bin/python3
# A function that returns
#   a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    for x in sorted(a_dictionary):
        a_dictionary[x] = a_dictionary[x] * 2
    return a_dictionary
