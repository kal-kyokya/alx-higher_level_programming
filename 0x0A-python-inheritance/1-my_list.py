#!/usr/bin/python3
"""
'1-my_list' is a subclass creation module 
"""


class MyList(list):
    """Derived class that only accepts integer inputs.

    Parent Class:
        list
    """

    def __init__(self):
        """Constructs and initializes MyList's instances."""
        pass

    def append(self, num):
        """Appends a integer and only an integer to a list."""
        if not isinstance(num, int):
            raise TypeError("Input must be an integer.")
        super().append(num)

    def print_sorted(self):
        """Prints a sorted version of a MyList object."""
        print(sorted(self))

if __name__ == "__main__":
    import doctest
    doctest.testfile("1-my_list.txt")
