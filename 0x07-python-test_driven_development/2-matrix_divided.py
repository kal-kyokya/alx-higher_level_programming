#!/usr/bin/python3
"""
'2-matrix_divided' is a matrix division module.
"""


def matrix_divided(matrix, divisor):
    """Divides all numbers inside a matrix by a divisor.

    Args:
        matrix: The matrix to be perated on.
        divisor: The divisor to the matrix.

    Return:
        The divided matrix version.
    """
    divided_matrix = []

    if not isinstance(matrix, list) or\
       not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(divisor, (int, float)):
        raise TypeError("div must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(n, (int, float)) for row in matrix for n in row):
        raise ValueError("matrix elements must be integer or float")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    divided_matrix = [list(
        map(lambda num: round(num / divisor, 2), row)) for row in matrix]

    return (divided_matrix)


if __name__ == "__main__":
    import doctest
    doctest.testfile("2-matrix_divided.txt")
