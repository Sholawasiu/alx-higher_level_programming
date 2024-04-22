#!/usr/bin/python3
"""
Function that creates an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a “JSON file”.

    Arg:
        filename (file): the path to the JSON file.
    """
    with open(filename) as file:
        return json.load(file)
