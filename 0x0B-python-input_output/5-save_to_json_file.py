#!/usr/bin/python3
"""
'5-save_to_json_file' file writing module.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a python object inside a JSON file

    Arg:
        my_obj: Python Object:
        filename: JSON file.

    Return:
        Nothing.
    """
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
