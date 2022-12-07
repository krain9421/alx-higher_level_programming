#!/usr/bin/python3
# A function that adds all unique
#   integers in a list (only once for each integer)
def uniq_add(my_list=[]):
    list_check = []
    result = 0
    flag = 0
    for x in my_list:
        flag = 0
        # Create the checker for duplicates
        if not list_check:
            result += x
            list_check.append(x)
        else:
            for i in list_check:
                # Activate flag if curr number is duplicate
                if i == x:
                    flag = 1
                    break

                # Adds number to result if flag is 0
                if flag == 0:
                    result += x
                list_check.append(x)
            return result
