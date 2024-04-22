#!/usr/bin/python3
"""
Appends a string to the end of a text file (UTF-8).
"""


def append_write(filename="", text=""):
    """
    Function that appends to a text file (UTF-8) and returns
    the number of characters added.

    Args:
        filename (text file): the path to the filename
        text (string): the content to insert to the file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
