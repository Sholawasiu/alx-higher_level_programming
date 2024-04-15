#!/usr/bin/python3
"""
Function to add a new attribute to an object if it’s possible.
"""


def add_attribute(obj, name, value):
    """
    Adds an attribute to an object.
    Args:
        obj: an object
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
