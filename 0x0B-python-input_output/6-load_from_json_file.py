#!/usr/bin/python3
"""
'6-load_from_json_file' file writing module.
"""
import json


def load_from_json_file(filename):
    """Returns a python object from a JSON file

    Arg:
        filename: JSON file.

    Return:
        The python object.
    """
    with open(filename, "r") as json_file:
        content = json.load(json_file)
    return (content)
