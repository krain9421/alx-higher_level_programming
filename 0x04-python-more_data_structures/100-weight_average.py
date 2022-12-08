#!/usr/bin/python3
# A function that returns the weighted
#   average of all integers tuple (<score>, <weight>)
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        score_sum = 0
        weight_sum = 0
        for row in my_list:
            weight_sum += row[0] * row[1]
            score_sum += row[1]
        return (weight_sum/score_sum)
