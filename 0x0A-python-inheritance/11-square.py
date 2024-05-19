#!/usr/bin/python3
"""
'10-square' is a Class creation module.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Blueprint for all instances of type Square.

    Direct Parent Class:
        Rectangle: First superclass.

    Attributes:
        size: Length of the Square's side.
    """

    def __init__(self, input_size):
        """Constructs and Initializes all instances of Square.

        Arg:
            input_size: Numeral value defining the side of square.
        """
        super().integer_validator("size", input_size)
        self.__size = input_size
        super().__init__(input_size, input_size)
