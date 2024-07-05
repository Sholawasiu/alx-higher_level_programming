#!/usr/bin/python3
# 6-peak.py
# @tonybnya
"""
This module is to find a peak of a list.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list.
    Arg:
        list_of_integers (list): list of unsorted integers
    Return:
        An integer element of the list representing the peak
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]

    return None
