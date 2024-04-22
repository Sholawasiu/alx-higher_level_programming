#!/usr/bin/python3
"""
Function that returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation
    of a string object.

    Arg:
        my_obj (string): a string object
    """
    return json.dumps(my_obj)
