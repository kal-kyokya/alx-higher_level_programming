#!/usr/bin/python3
"""
'0-rectangle' is a Rectangle creation module.
"""


class Rectangle:
    """
    This is the blueprint for all its instances of the 'Rectangle'.

    Attributes:
        Width: Numeral value defining the width of the rectangle.
        Height: Numeral value defining the height of the rectangle.
    """

    def __init__(self, input_width=0, input_height=0):
        """Constructor for the width and height Object Attributes."""
        self.__width = input_width
        self.__height = input_height

    @property
    def width(self):
        """Width Attribute's getter."""
        (self.__width)

    @width.setter
    def width(self, value):
        """Width Attribute's setter."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height Attribute's getter."""
        self.__height

    @height.setter
    def height(self, value):
        """Height Attribute's setter."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
