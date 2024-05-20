#!/usr/bin/python3
"""
'12-pascal_triangle' is a list of lists creation module.
"""


def pascal_triangle(n):
    """Generates a pascal triangle using lists."""

    pascTrg = []
    count = 1

    if n <= 0:
        pascTrg.append([])
        return (pascTrg)

    while count <= n:
        pascRow = [0] * count
        index = 0
        rvs_i = count - 1

        if count == 1:
            pascTrg.append([1])
            if n == 1:
                return (pascTrg)
            count += 1
            continue

        pascRow[index] = 1
        pascRow[rvs_i] = pascRow[index]
        index += 1
        rvs_i -= 1

        pascRow[index] = count - index
        pascRow[rvs_i] = pascRow[index]
        index += 1
        rvs_i -= 1

        while index <= rvs_i:
            pascRow[index] = pascTrg[- 1][index - 1] + pascTrg[- 1][index]
            pascRow[rvs_i] = pascRow[index]
            index += 1
            rvs_i -= 1

        pascTrg.append(pascRow)
        count += 1

    return (pascTrg)
