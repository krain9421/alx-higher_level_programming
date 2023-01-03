#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints/floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is neither an int nor float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")

    for row in matrix:
        if (type(row) not in [list]):
            raise TypeError("matrix must be a matrix (list of lists) of "
                    "integers/floats")
        if (len(row) != len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")

        for num in row:
            if (type(num) not in [int, float]):
                raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if (type(div) not in [int, float]):
            raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = [ [round(x/div, 2) for x in row] for row in matrix]
    return (new_matrix)
