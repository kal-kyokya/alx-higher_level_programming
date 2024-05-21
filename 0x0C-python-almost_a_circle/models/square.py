#!/usr/bin/python3
"""
'square' is a class creation module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Blueprint for all instances of type Square.

    Parent class:
        Rectangle: Module defined in '/models/rectangle.py'.
    """

    def __init__(self, input_size, input_x=0, input_y=0, id=None):
        """Constructs and Initializes all instances of class Rectangle.

        Args:
            input_size: Square's side length.
            input_x: Extra width unit.
            input_y: Extra height unit.
        """
        self.__size = input_size
        super().__init__(self.__size, self.__size, input_x, input_y, id)

    def __str__(self):
        """Overrides the string representation of the 'self' object."""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x, self.y,
                                              self.size))

    @property
    def size(self):
        """Getter for the attribute 'size'.

        The setter follows right after.
        """
        return (self.__size)

    @size.setter
    def size(self, input_value):
        if not isinstance(input_value, int):
            raise TypeError("size must be an integer")
        if input_value <= 0:
            raise ValueError("size must be > 0")
        self.__size = input_value
        self.__width = input_value
        return (self.__size)

    @property
    def size(self):
        """Getter for the attribute 'size'.

        The setter follows right after.
        """
        return (self.__size)

    @size.setter
    def size(self, input_value):
        if not isinstance(input_value, int):
            raise TypeError("size must be an integer")
        if input_value <= 0:
            raise ValueError("size must be > 0")
        self.__size = input_value
        self.__height = input_value
        return (self.__size)
