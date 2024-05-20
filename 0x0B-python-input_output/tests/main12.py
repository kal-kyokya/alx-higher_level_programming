#!/usr/bin/python3
"""
12-main
"""
pascal_triangle = __import__('pascal_triangle').pascal_triangle


def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    for value in range(0, 7):
        print("\n;););););););););););););)\nn:", value)
        print_triangle(pascal_triangle(value))
