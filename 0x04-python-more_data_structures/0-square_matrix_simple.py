#!/usr/bin/python
#A function that computes the square value of all integers of a matrix.
def square_matrix_simple(matrix=[]):
    new_matrix = [[i ** 2 for i in row] for row in matrix]
    return new_matrix
