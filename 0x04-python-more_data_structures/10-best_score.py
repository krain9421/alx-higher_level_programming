#!/usr/bin/python3
# A function that returns a key
#   with the biggest integer value.
def best_score(a_dictionary):
    key_max = None
    val_max = float(-inf)
    # Check if dictionary is None
    if a_dictionary == None:
        return None
    # Loop through the items in the dictionary
    for key, val in a_dictionary.items():
        # If the value is greater than the current maximum,
        #   update the maximum and the key
        if val > val_max:
            val_max = val
            key_max = key
    # Return the key with the maximum value
    return key_max
