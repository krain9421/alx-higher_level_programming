#!/usr/bin/python3
# A function that returns a key
#   with the biggest integer value.
def best_score(a_dictionary):
    key_max = None
    val_max = 0
    count = 0
    # Check if dictionary is None
    if not a_dictionary:
        return None
    # Loop through the items in the dictionary
    for key, val in a_dictionary.items():
        # If count is 0, update maximum value
        if count == 0:
            val_max = val
            if key:
                key_max = key
        # If the value is greater than the current maximum,
        #   update the maximum and the key
        if val > val_max:
            val_max = val
            if key:
                key_max = key
            else:
                key_max = None
        # Update value of count
        count += 1
    # Return the key with the maximum value
    return key_max
