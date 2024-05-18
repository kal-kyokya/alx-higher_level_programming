#!/usr/bin/python3
"""
'2-is_same_class' is class comparision module
"""


def is_same_class(obj, a_class):
    """Tells if an input object belongs to the input class.

    Args:
        obj: Random object to be assessed.
        a_class: Class to to be compared to.

    Return:
        True if the object belongs to the class, False if not.
    """
    return (type(obj) == a_class)
