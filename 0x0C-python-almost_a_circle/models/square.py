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
                                              self.width))

    @property
    def size(self):
        """Getter for the attribute 'size'.

        The setter follows right after.
        """
        return (self.width)

    @size.setter
    def size(self, input_value):
        self.width = input_value
        self.height = input_value
        return (self.width)

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """"returns the dictionary representation of a Square."""
        list_attr = ['id', 'size', 'x', 'y']
        new_dict = {}
        for key in list_attr:
            new_dict[key] = getattr(self, key)
        return (new_dict)
