#!/usr/bin/python3
# Prints an integer with "{:d}".format()
# @value: integer to print
# Return: False if a TypeError or ValueError occurs
# True: otherwise
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
