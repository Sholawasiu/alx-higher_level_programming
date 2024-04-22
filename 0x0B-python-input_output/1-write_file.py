#!bin/bash/python3

def write_file(filename="", text=""):
    """
    Function that writes to a text file (UTF-8) and returns
    the number of characters written.

    Args:
        filename (text file): the path to the filename
        text (string): the content to insert to the file

    Returns:
        the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)

    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        chars = 0
        for line in lines:
            chars += len(line)

    return chars
