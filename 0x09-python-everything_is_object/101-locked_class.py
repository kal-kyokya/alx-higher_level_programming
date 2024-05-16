#!/usr/bin/python3
"""
'101-locked_class' is class creation module
"""


class LockedClass:
    """Creates a class restricting dynamic initializations
    of new attributes unless named 'first_name'.
    """
    __slots__ = ['first_name']

    def __init__(self):
        """Constructs and Initializes Object Attributes."""
        pass
