#!usr/bin/python3
"""
'0-lookup' is an attributes and methods listing module.
"""


def lookup(obj):
    """Avails all attributes & methods of an input object.

    Arg:
        obj: Object input to be assessed.

    Return:
        A list of the attributes and methods.
    """
    return (dir(obj))
