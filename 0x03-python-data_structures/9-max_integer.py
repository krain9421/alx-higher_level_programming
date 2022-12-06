#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        nmax = my_list[0]
        for i in my_list:
            if i > nmax:
                nmax = i
        return nmax
    else:
        return None
