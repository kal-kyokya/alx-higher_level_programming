#!/usr/bin/python3
"""
'9-rectangle' is a Class creation module.
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
        super().integer_validator("width", input_width)
        self.__width = input_width
        super().integer_validator("height", input_height)
        self.__height = input_height

    def area(self):
        """Superclass method computing the area of Rectangle object.

        Arg:
            None.

        Return: The computed area.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Unofficial, user-friendly object representation."""
        return (f"[{self.__class__.__name__}] {self.__width}/{self.__height}")
