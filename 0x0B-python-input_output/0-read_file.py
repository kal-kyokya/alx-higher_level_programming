#!/usr/bin/python3
"""
'0-read_file' is a file reading module.
"""


def read_file(filename=""):
    """Reads an input file and prints it to stdout.

    Arg:
        filename: File to be processed.

    Return:
        Nothing.
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content)
