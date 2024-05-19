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
    return(json.loads(my_str))
