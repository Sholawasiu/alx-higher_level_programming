#!/usr/bin/python3

"""
This module divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        matrix (list): list of lists of integers or floats
        div (int or float): the divisor

    Returns:
        a new matrix
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(item, (float, int))
                    for item in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
