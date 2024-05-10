#!/usr/bin/python3
"""No modules, therefore, no module descriptions"""


class Square():
    """Facilitates creation and manipulation of a square.

    Attribute:
        size: Numeral field defining the size of the square.
    """
    def __init__(self, user_size):
        """Constructs and initializes an object 'self' of type 'Square'.

        Arg:
            user_size: Numeral value assigned by user to the 'size' attribute.
        """
        self.__size = user_size
