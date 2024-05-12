#!/usr/bin/python3
"""No modules imported, therefore, no module descriptions."""


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

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    """This module provides our script with the method:
        'testfile(<filne_name>)'
    that automates testing of add function using
    scenarios in the specified file.
    """

    doctest.testfile("test/0-add_integer.txt")
