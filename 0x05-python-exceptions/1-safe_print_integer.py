#!/usr/bin/python3
# Print an integer with "{:d}".format().
# @value: The integer to print.
# Return: False if a TypeError or ValueError occurs
# True otherwise
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
