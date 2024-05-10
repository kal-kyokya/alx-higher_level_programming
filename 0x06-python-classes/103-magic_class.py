#!/usr/bin/python3
""" Docstring """
from math import pi


class MagicClass:
    """setting up magic"""

    def __init__(self, radius=0):
        """ Another docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """with the docstring"""
        return self.__radius ** 2 * pi

    def circumference(self):
        """Docstring"""
        return 2 * pi * self.__radius
