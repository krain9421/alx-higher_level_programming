#!/usr/bin/python3
# A function that returns
#   a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    # Dictionary to store the multiplied values
    multiplied = {}
    # Loop through the items in the original dictionary
    for key, val in a_dictionary.items():
        # Multiply the value by 2 and store it
        multiplied[key] = val * 2
    # Return the new dictionary
    return multiplied
