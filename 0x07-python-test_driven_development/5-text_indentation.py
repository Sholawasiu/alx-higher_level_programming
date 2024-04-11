#!/usr/bin/python3

"""
This module defines a text-indentation function.
"""


def text_indentation(text):
    """
    Prints text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.

    Returns:
        nothing to return
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        print(text[char], end="")
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                print("\n")
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
