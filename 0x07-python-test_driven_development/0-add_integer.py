#!/usr/bin/python3
"""
'0-add_integer' is numeral addition module.
"""


def add_integer(a, b=98):
    """Computes the sum of two numbers.

    Args:
        a: First number.
        b: Second number, whose default value is 98.

    Return:
        The sum of a and b.
    """
    if isinstance(a, (int, float)) is not True:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is not True:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
