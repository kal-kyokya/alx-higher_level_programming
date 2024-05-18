#!/usr/bin/python3
"""
'4-inherits_from' is a class comparison module
"""


def inherits_from(obj, a_class):
    """Tells if an input object belongs to any of the class' superclass(es).

    Args:
        obj: Random object to be assessed.
        a_class: Class to to be compared to.

    Return:
        True if the object belongs to the class, False if not.
    """
    if (issubclass(type(obj), a_class)) and\
       type(obj) is not a_class:
        return (True)
    return (False)
