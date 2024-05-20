#!/usr/bin/python3

"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        print(f"triangles {triangles} -- len(triangles) {len(triangles)}")

        tri = triangles[-1]
        print(f"tri = triangles[-1]: {tri}")

        tmp = [1]
        print(f"tmp b4: {tmp}")

        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])

        print(f"tmp: {tmp}")

        tmp.append(1)

        triangles.append(tmp)
        print(f"triangles.append(tmp): {triangles}\n")

    print(f"triangles: {triangles}")
    return triangles
