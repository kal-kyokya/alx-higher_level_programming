#!/usr/bin/python3
"""
'0-read_file' is a file reading module.
"""


def read_file(filename=None):
    """Reads an input file and prints it to stdout.

    Arg:
        filename: File to be processed.

    Return:
        Nothing.
    """

    if filename == None or filename == "":
        raise ValueError("[ValueError]: No input detected.")

    with open(filename, "r") as file:
        my_file = file.read()
        print(my_file)
