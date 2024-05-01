#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''Prints an integer matrix to stdout.

    Args:
        matrix: A two-dimensional list, i.e a matrix.

    Return:
        Nothing
    '''
    for count1 in range(0, len(matrix)):
        for count2 in range(0, len(matrix[count1])):
            print("{}".format(matrix[count1][count2]), end="")
            if count2 + 1 < len(matrix[count1]):
                print(" ", end="")
        print()
