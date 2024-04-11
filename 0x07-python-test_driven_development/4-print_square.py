#!/usr/bin/python3

"""
This module prints a square with the character #.
"""


def print_square(size):
    """
    Function to print #.

    Args:
        size (int): the height/width of the square

    Returns:
        nothing to return
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        [print('#', end="") for j in range(size)]
        print('')
