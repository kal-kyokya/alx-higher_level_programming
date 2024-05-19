#!/usr/bin/python3
"""
'4-from_json_string' is a python object Decoding.
"""
import json


def from_json_string(my_str):
    """Converts a JSON representation into an equivalent python object.

    Arg:
        my_str: JSON representation to be converted.

    Return:
        The Python object.
    """
    with open("JavaSON.json", "r") as json_file:
        json_file = json.loads(my_str)
        return(json_file)
