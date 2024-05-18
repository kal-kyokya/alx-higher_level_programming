#!/usr/bin/python3
"""
'7-base_geometry' integer validator module.
"""


class BaseGeometry:
    """Empty class"""
    def __init__(self):
        """Constructs and Initializes any class' instance."""
        pass

    def area(self):
        """Raises an Exception with a message."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the input value.

        Args:
            name: Input assumed to always being a string.
            value: Input expected to be an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
