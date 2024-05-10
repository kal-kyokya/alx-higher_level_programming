#!/usr/bin/python3
"""No modules, therefore, no module descriptions."""


class Square():
    """Enables creation and manipulations of a square.

    Arttribute:
        size: Numeral field defining the size of the square.
    """
    def __init__(self, user_size=0, position=(0, 0)):
        """Constructs and initializes an 'self' object of type 'Square'.

        Args:
            user_size: Numeral value of 'size'.
            position: Location at which to add space
        """
        self.__size = user_size
        self.__position = position

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

    @property
    def position(self):
        """This is the GETTER METHOD for the field attribute position.

        The SETTER METHOD follows right after.
        """
        return self.__position

    @position.setter
    def position(self, position):
        if type(value) is not tuple or len(value) != 2 or\
            type(value[0]) is not int or type(value[1]) is not int or\
                value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

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
            for new_lines in range(0, self.position[1]):
                print()
            for row in range(0, self.__size):
                for space in range(0, self.position[0]):
                    print(" ", end="")
                for column in range(0, self.size):
                    print("#", end="")
                print()
