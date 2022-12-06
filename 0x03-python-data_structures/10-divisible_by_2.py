#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_2 = []
    for i in my_list:
        if i % 2 == 0:
            list_2.append(True)
        else:
            list_2.append(False)
    return list_2
