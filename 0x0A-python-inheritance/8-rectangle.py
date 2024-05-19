#!/usr/bin/python3
"""
'8-rectangle' is a Class creation module.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Blueprint for all instances of type Rectangle.

    Attributes:
        width: Rectangle object's Width.
        height: Rectangle object's Height.
    """

    def __init__(self, input_width, input_height):
        """Constructs and Initializes all instances of type Rectangle.

        Args:
        input_width: Rectangle object's Input_Width.
        input_height: Rectangle object's Input_Height.
        """
        self.__width = super().integer_validator("width", input_width)
        self.__height = super().integer_validator("height", input_height)
