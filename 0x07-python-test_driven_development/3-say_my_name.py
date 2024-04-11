#!/usr/bin/python3
"""
This module prints a name.
"""


def say_my_name(first_name, last_name=""):
    """
    Function for name printing.

    Args:
        first_name (str): the first name
        last_name (str): the last name

    Returns:
        nothing to return
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
