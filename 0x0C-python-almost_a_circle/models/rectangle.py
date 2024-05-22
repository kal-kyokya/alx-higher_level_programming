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
        self.width = input_w
        self.height = input_h
        self.x = input_x
        self.y = input_y

    @property
    def width(self):
        """Getter for the attribute 'width'.

        The setter follows right after.
        """
        return (self.__width)

    @width.setter
    def width(self, input_value):
        if type(input_value) is not int:
            raise TypeError("width must be an integer")
        if input_value <= 0:
            raise ValueError("width must be > 0")
        self.__width = input_value

    @property
    def height(self):
        """Getter for the attribute 'height'.

        The setter follows right after.
        """
        return (self.__height)

    @height.setter
    def height(self, input_value):
        if type(input_value) is not int:
            raise TypeError("height must be an integer")
        if input_value <= 0:
            raise ValueError("height must be > 0")
        self.__height = input_value

    @property
    def x(self):
        """Getter for the attribute 'x'.

        The setter follows right after.
        """
        return (self.__x)

    @x.setter
    def x(self, input_value):
        if type(input_value) is not int:
            raise TypeError("x must be an integer")
        if input_value < 0:
            raise ValueError("x must be >= 0")
        self.__x = input_value

    @property
    def y(self):
        """Getter for the attribute 'y'.

        The setter follows right after.
        """
        return (self.__y)

    @y.setter
    def y(self, input_value):
        if type(input_value) is not int:
            raise TypeError("y must be an integer")
        if input_value < 0:
            raise ValueError("y must be >= 0")
        self.__y = input_value

    def area(self):
        """Computes the area of the rectangle."""
        return (self.width * self.height)

    def display(self):
        """Represents the rectangle using the character '#'."""
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(end=" ")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Overrides the string representation of the 'self' object."""
        return ("[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                 self.id, self.x, self.y,
                                                 self.width, self.height))

    def update(self, *args, **kwargs):
        """Reassigns n  specific object attributes.

        Arg:
          IF 'ARGS' DOESN'T EXIST OR IS EMPTY:
            kwargs: A collection of 'Key=value' pairs linked to attributes.
          ELSE:
            args: A tuple representation of the new values:
              ->  1st argument should be the id attribute
              ->  2nd argument should be the width attribute
              ->  3rd argument should be the height attribute
              ->  4th argument should be the x attribute
              ->  5th argument should be the y attribute
        """

        if len(args) == 0 or args is None:
            for attr, value in kwargs.items():
                if attr == "id":
                    super().__init__(value)
                elif attr == "width":
                    self.width = value
                elif attr == "height":
                    self.height = value
                elif attr == "x":
                    self.x = value
                elif attr == "y":
                    self.y = value
        else:
            if len(args) >= 1:
                super().__init__(args[0])
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
            if len(args) > 5:
                raise ValueError("Clash in arguments detected.")
