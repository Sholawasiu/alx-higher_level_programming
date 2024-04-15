#!/usr/bin/python3
"""
Check if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Function Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Args:
        obj: an object
        a_class: a class type
    """
    if type(obj) is a_class:
        return False

    return isinstance(obj, a_class)
