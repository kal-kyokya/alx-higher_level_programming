#!/usr/bin/python3
"""
'8-rectangle' is a Class creation module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Blueprint for all instances of type Rectangle.

    Attributes:
        width: Width of the Rectangle object.
        height: Height of the Rectangle object.
    """

    def __init__(self, input_width, input_height):
        """Constructs and Initializes all instances of type Rectangle.

        Args:
            input_width: Input_Width of the Rectangle object.
            input_height: Input_Height of the Rectangle object.
        """
        self.__width = super().integer_validator("width", input_width)
        self.__height = super().integer_validator("height", input_height)
