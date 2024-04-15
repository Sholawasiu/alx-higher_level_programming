#!/usr/bin/python3
"""
Class MyInt that inherits from the Python's built-in Class int.
MyInt is a rebel Class.
== and != are inverted.
"""


class MyInt(int):
    """
    Class MyInt that inherits from the Python's built-in Class int.
    MyInt is a rebel Class.
    == and != are inverted.
    """
    def __eq__(self, other):
        """
        Inverted equivalence.
        """
        # return int.__ne__(self, other)
        return type(self) == type(other)

    def __ne__(self, other):
        """
        Inverted difference.
        """
        # return int.__eq__(self, other)
        return type(self) != type(other)
