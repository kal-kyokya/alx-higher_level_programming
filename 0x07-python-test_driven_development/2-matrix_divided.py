#!/usr/bin/python3
"""
'2-matrix_divided' is a matrix division module.
"""


def matrix_divided(matrix, divisor):
    """Divides all numbers inside a matrix by divisor.

    Args:
        matrix: The matrix to be perated on.
        divisor: The divisor to the matrix.

    Return:
        The divided matrix version.
    """
    prev_list_len = 0
    divided_matrix = []

    if isinstance(matrix[0], list) is not True:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
    if isinstance(divisor, (int, float)) is not True:
        raise TypeError("div must be a number")
    if divisor == 0:
        raise ZeroDivisionError("division by zero")
    for submatrix in matrix:
        new_matrix = []
        for num in submatrix:
            if isinstance(num, (int, float)) is not True:
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
            new_num = num / divisor
            if isinstance(new_num, float):
                new_num = round(new_num, 2)
            else:
                int(new_num)
            new_matrix.append(new_num)
            if prev_list_len == 0:
                prev_list_len = len(submatrix)
            elif prev_list_len != len(submatrix):
                raise TypeError("Each row of the matrix must\
 have the same size")
        divided_matrix.append(new_matrix)

    return (divided_matrix)


if __name__ == "__main__":
    import doctest
    doctest.testfile("2-matrix_divided.txt")
