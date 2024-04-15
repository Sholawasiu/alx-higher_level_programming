#!/usr/bin/python3
"""
Function that checks if a given object is an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Function that checks if a given object is an instance
    of a given class.

    Args:
        obj: an object
        a_class: a class type

    Returns:
        True if type of obj is a_class
        False, otherwise
    """
    return type(obj) is a_class
