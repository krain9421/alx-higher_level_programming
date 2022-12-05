#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_cpy = my_list[:]

    for i in reversed(my_list_cpy):
        print("{:d}".format(i))
