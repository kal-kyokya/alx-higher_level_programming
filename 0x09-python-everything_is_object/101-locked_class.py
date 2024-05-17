#!/usr/bin/python3
"""
'101-locked_class' is class creation module.
"""


class LockedClass:
    """Class that restricts dynamic creation of unspecified attributes."""
    __slots__ = ['first_name']

    def __init__(self):
        """Constructs and Initializes Object Attributes."""
        pass
