#!/usr/bin/python3
"""
'12-pascal_triangle' is a list of lists creation module.
"""


def pascal_triangle(input_num):
    """Generates a pascal triangle using lists.

    Arg:
        input_num: Base of generated pascal triangle.

    Return:
        A list representation of the generated triangle.
    """
    if input_num <= 0:
        return ([])
    pascTrg = [[1]]
    for row in range(2, input_num + 1):
        pascRow = [0] * row
        index = 0
        rvs_i = row - 1
        pascRow[index] = pascRow[rvs_i] = 1
        index += 1
        rvs_i -= 1
        pascRow[rvs_i] = pascRow[index] = row - index
        index += 1
        rvs_i -= 1
        while index <= rvs_i:
            pascRow[rvs_i] = pascRow[index] = pascTrg[- 1][index - 1] + pascTrg[- 1][index]
            index += 1
            rvs_i -= 1
        pascTrg.append(pascRow)
    return (pascTrg)
