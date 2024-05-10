#!/usr/bin/python3
"""No modules, therefore, no module descriptions."""


class Square():
    """Enables creation and manipulation of a square.

    Attributes:
        size: Numeral value defining the size of the square.
    """
    def __init__(self, user_size):
        """Constructs and initializes an instance 'self' of type 'Square'.

        Args:
            user_size: A numeral value assigned by the user to 'size'.
        """
        if type(user_size) is not int:
            raise TypeError("size must be an integer")
        if user_size < 0:
            raise ValueError("size must be >= 0")

        self.__size = int(user_size)

    def area(self):
        """Computes the Surface area of the square.

        Args:
            None.

        Return:
            The Area of a square of size 'user_size'.
        """
        return (self.__size ** 2)
