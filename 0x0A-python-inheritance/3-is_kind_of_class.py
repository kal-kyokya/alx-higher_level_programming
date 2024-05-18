#!/usr/bin/python3
"""
'3-is_same_class' is a class comparison module
"""


def is_kind_of_class(obj, a_class):
    """Tells if an input object belongs to the class or its subclass(es).

    Args:
        obj: Random object to be assessed.
        a_class: Class to to be compared to.

    Return:
        True if the object belongs to the class, False if not.
    """
    return (isinstance(obj, a_class))
