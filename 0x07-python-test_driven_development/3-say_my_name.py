#!/usr/bin/python3
"""
'3-say_my_name' is a string concatenation and printing module.
"""


def say_my_name(first_name, last_name=""):
    """Prints the input names as one.

    Args:
        first_name: String name printed first.
        last_name: String name printed last.

    Return:
        Nothing.
    """
    name_list = [first_name, last_name]

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if all(len(name) == 0 for name in name_list):
        raise ValueError("two empty strings detected")

    if ((len(first_name) == 0 or
            all(char == ' ' for char in first_name)) and
            len(last_name) != 0):
        print(f"My name is {last_name}")
    elif ((len(last_name) == 0 or
            all(char == ' ' for char in last_name)) and
            len(first_name) != 0):
        print(f"My name is {first_name}")
    else:
        print(f"My name is {first_name} {last_name}")


if __name__ == ("__main__"):
    import doctest
    doctest.testfile("3-say_my_name.txt")
