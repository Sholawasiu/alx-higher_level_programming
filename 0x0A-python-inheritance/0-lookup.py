#!/usr/bin/python3
"""
dir() function is an built-in function that will return a list
of attributes and methods of any object.
"""


def lookup(obj):
    """
    Function that returns the list of available attributes
    and methods of an object

    Args:
        obj (object): an object

    Returns:
        a list object
    """
    return dir(obj)
