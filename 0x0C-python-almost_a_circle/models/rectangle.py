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
            
            
            
            
        """

        super().__init__(id)
        self.__width = input_w
        self.__height = input_h
        self.__x = input_x
        self.__y = input_y
