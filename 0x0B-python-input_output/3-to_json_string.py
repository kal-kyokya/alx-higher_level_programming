#!/usr/bin/python3
"""
'3-to_json_string' is a python object serialization.
"""
import json


def to_json_string(my_obj):
    """Converts a python object into an equivalent JSON representation.

    Arg:
        my_obj: Python object to be converted.

    Return:
        The JSON representation.
    """
    return (json.dumps(my_obj))
