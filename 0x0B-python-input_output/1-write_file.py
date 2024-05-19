#!/usr/bin/python3
"""
'1-write_file' is a file writing module.
"""


def write_file(filename="", text=""):
    """Writes an input text inside a specific filename.

    Args:
        filename: Name of the file written into.
        text: String to be written inside 'filename'.

    Return: The number of characters written.
    """
    with open(filename, "w") as my_file:
        length = my_file.write(text)
        return (length)
