#!/usr/bin/python3
"""
'2-append_write' is a file append writing module.
"""


def append_write(filename="", text=""):
    """Appends an input text to the content of a specific file.

    Args:
        filename: Name of the file appended to.
        text: String to be appended to 'filename'.

    Return: The number of characters written.
    """
    with open(filename, "a") as my_file:
        length = my_file.write(text)
        return (length)
