#!/usr/bin/python3
# A function that prints a
#   dictionary by ordered keys.
def print_sorted_dictionary(a_dictionary):
    for x in sorted(a_dictionary):
        print("{}: {}".format(x, a_dictionary[x]))
