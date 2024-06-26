#!/usr/bin/python3

def pascal_triangle(n):

    print(f"\tn: {n}\n")
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

        print(f"count: {count} -- i: {index} -- r_i: {rvs_i}")
        while index <= rvs_i:
            if index == rvs_i:
                pascRow[index] = (count - index) + pascTrg[- 1][index]
            else:
                pascRow[index] = (count - index) + pascTrg[- 1][index]
            pascRow[rvs_i] = pascRow[index]
            index += 1
            rvs_i -= 1

        print(f"{pascRow}")
        pascTrg.append(pascRow)
        print(f"{pascTrg}\n")
        count += 1

    return (pascTrg)
