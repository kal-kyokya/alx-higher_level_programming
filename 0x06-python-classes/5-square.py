#!/usr/bin/python3
"""No modules, therefore, no module descriptions."""


class Square:
    """Enables creation and manipulations of a square.

    Arttribute:
        size: Numeral field defining the size of the square.
    """
    def __init__(self, user_size=0):
        """Constructs and initializes an 'self' object of type 'Square'.

        Args:
            user_size: Numeral value of 'size'.
        """
        self.__size = user_size

    @property
    def size(self):
        """This is the GETTER METHOD for the field attribute size.

        The SETTER METHOD follows right after.
        """
        return (self.__size)

    @size.setter
    def size(self, user_size):
        if type(user_size) is not int:
            raise TypeError("size must be an integer")
        if user_size < 0:
            raise ValueError("size must be >= 0")

        self.__size = user_size

    def area(self):
        """Computes the Surface area of the square.

        Args:
            None.

        Return:
            The Area of a square of size 'user_size'.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square of size user_size using the # characater.

        Args:
            None.

        Return:
            Nothing.
        """
        if self.__size is 0:
            print()
        else:
            for row in range(0, self.__size):
                for column in range(0, self.size):
                    print("#", end="")
                print()
