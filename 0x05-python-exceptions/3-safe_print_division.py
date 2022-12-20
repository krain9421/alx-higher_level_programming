#!/usr/bin/python3
# Function that divides 2 integers and prints the result.
# @a: first integer
# @b: divisor integer
# Return: value of the division
# None otherwise
def safe_print_division(a, b):
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
