#!/usr/bin/python3
# A function that replaces all occurrences of an element by another in a new list.
def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        new_list.append(replace if x == search else x)
    return new_list
