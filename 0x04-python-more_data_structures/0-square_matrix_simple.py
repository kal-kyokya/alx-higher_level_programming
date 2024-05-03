#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Creates a matrix version where all elements are raised to 2.

    Arg:
        matrix: The original matrix.

    Return:
        The new matrix version.
    '''
    return [[n ** 2 for n in matrix[i]] for i in range(0, len(matrix))]
