#!/usr/bin/python3

def pascal_triangle(n):

    print(f"\tn: {n}\n")
    pascTrg = []
    count = 1

    if n <= 0:
        pascTrg.append([])
        return (pascTrg)

    while count <= n:
        pascRow = [1] * count
        index = 0
        reversed_index = count - 1

        print("count: ", count, "--", pascRow, "--", pascTrg)
        if count == 1:
            pascTrg.append(pascRow)
            print("count: ", count, "--", pascRow, "--", pascTrg, end="\n\n")
            if n == 1:
                return (pascTrg)
            count += 1
            continue

        print("\nindex: ", index, " -- r_i:", reversed_index)
        pascRow[index] = 1
        pascRow[reversed_index] = pascRow[index]
        index += 1
        reversed_index -= 1

        print("count: ", count, "--", pascRow, "--", pascTrg)
        print("index: ", index, " -- r_i:", reversed_index)
        pascRow[index] = count - index
        pascRow[reversed_index] = pascRow[index]
        index += 1
        reversed_index -= 1

        print("count: ", count, "--", pascRow, "--", pascTrg)
        print("index: ", index, "r_i:", reversed_index)
        if index <= reversed_index:
            pascRow[index] = (count - index) + pascTrg[- 1][index]
            pascRow[reversed_index] = pascRow[index]

        pascTrg.append(pascRow)
        print("End Product at count: ", count, "--",
              pascRow, "--", pascTrg, end="\n\n")
        count += 1

    return (pascTrg)
