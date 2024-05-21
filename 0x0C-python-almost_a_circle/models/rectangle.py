#!/usr/bin/python3
"""
'rectangle' is a class creation module
"""
from models.base import Base


class Rectangle(Base):
    """Blueprint for all instances of type Rectangle.

    Parent class:
        Base: Module defined in '/models/base.py'.
    """

    def __init__(self, input_w, input_h, input_x=0, input_y=0, id=None):
        """Constructs and Initializes all instances of class Rectangle.

        Args:
            input_w: Width of the Rectangle.
            input_h: Height of the rectangle.
            input_x: Extra width unit.
            input_y: Extra height unit.
        """

        super().__init__(id)
        self.__width = input_w
        self.__height = input_h
        self.__x = input_x
        self.__y = input_y

    @property
    def width(self):
        """Getter for the attribute 'width'.

        The setter follows right after.
        """
        return (self.__width)

    @width.setter
    def width(self, input_value):
        self.__width = input_value
        return (self.__width)

    @property
    def height(self):
        """Getter for the attribute 'height'.

        The setter follows right after.
        """
        return (self.__height)

    @height.setter
    def height(self, input_value):
        self.__height = input_value
        return (self.__height)

    @property
    def x(self):
        """Getter for the attribute 'x'.

        The setter follows right after.
        """
        return (self.__x)

    @x.setter
    def x(self, input_value):
        self.__x = input_value
        return (self.__x)

    @property
    def y(self):
        """Getter for the attribute 'y'.

        The setter follows right after.
        """
        return (self.__y)

    @y.setter
    def y(self, input_value):
        self.__y = input_value
        return (self.__y)
