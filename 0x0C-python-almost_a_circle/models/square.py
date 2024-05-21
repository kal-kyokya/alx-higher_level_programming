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
        super().__init__(input_size, input_size, input_x, input_y, id)

    def __str__(self):
        """Overrides the string representation of the 'self' object."""
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x, self.y,
                                              self.height))
