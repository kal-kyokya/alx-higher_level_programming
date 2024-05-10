#!/usr/bin/python3
"""No modules, therefore, no module descriptions"""


class Square():
    """Enables creation and manipulation of a square.

    Attribute:
        size: Numeral defining the size of the actual square.
    """
    def __init__(self, user_size=0):
        """Constructs and initializes an instance 'self' of type 'Square'.

        Arg:
            user_size: Numeral value to be assigned to the size attribute.
        """
        try:
            int(user_size)
            if user_size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            raise TypeError("size must be an integer")
        self.__size = user_size
