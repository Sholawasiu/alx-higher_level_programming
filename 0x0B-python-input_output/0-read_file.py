#!/usr/bin/python3
"""
Reads a text file encoded with the standard encoding mode UTF-8.
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (text file): the path to the filename
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
