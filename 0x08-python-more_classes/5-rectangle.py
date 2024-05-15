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
        """Constructor for the width and height Object Attributes.

        Args:
            input_width: User input for the width Attribute.
            input_height: User input for the height Attribute.
        """
        self.width = input_width
        self.height = input_height

    @property
    def width(self):
        """Getter method for the width Attribute.

        The setter method follows right after.
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height Attribute.

        The setter method follows right after.
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """informal string representation of the object.

        It represents the rectangle using the '#' character.
        """
        rect = []
        if self.width == 0 or self.height == 0:
            return ("")
        char = '#' * self.width
        for h in range(self.height):
            rect.append(char)
        return ('\n'.join(rect))

    def __repr__(self):
        """Official string representation of the object."""
        return (f"{self.__class__.__name__}({self.width}, {self.height})")

    def __del__(self):
        """Overrides any call to the del command."""
        print("Bye rectangle...")
    
    def area(self):
        """Method computing the area of the Rectangle object."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Method computing the perimeter of the Rectangle object."""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * self.__width) + (2 * self.__height)
