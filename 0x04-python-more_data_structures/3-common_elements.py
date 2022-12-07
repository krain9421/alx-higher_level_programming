#!/usr/bin/python3
# A function that returns a set
#   of common elements in two sets.
def common_elements(set_1, set_2):
    new_set = {x for x in set_1 & set_2}
    return new_set
