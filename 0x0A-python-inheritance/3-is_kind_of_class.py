#!/usr/bin/python3
"""
Function to check if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Function to check if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class

    Args:
        obj: an object
        a_class: a class type
    """
    return isinstance(obj, a_class)
