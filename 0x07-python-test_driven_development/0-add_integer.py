#!/usr/bin/python3

"""
This module performs the addition of two numbers.
"""


def add_integer(a, b=98):
    """
    Function that adds two numbers.

    Args:
        a (int or float): 1st number
        b (int or float): 2nd number - default value is 98

    Returns:
        The integer addition of a and b.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
