#!/usr/bin/python3
"""
This class MyList inherits from Python's built-in list Class.
"""


class MyList(list):
    """
    This class MyList inherits from Python's built-in list Class.

    Args:
        list: class list.
    """
    def print_sorted(self):
        """
        Public instance method.
        Prints the list sorted in ascending order.
        """
        list_sorted = self[:]
        list_sorted.sort()

        print(list_sorted)
