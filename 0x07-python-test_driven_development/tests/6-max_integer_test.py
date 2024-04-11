#!/usr/bin/python3

"""
Unit tests for max_integer module.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines unit tests for max_integer module.
    """
    def test_ordered_list(self):
        """Ordered list"""
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(lst), 5)

    def test_unordered_list(self):
        """Unordered list"""
        lst = [2, 4, 5, 1, 3]
        self.assertEqual(max_integer(lst), 5)

    def test_at_beginning(self):
        """Max integer at the beginning of the list"""
        lst = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(lst), 5)

    def test_empty_list(self):
        """Empty list"""
        lst = []
        self.assertEqual(max_integer(lst), None)

    def test_one_item(self):
        """One item"""
        lst = [3]
        self.assertEqual(max_integer(lst), 3)

    def test_float(self):
        """List of floats"""
        lst = [-3.1, 1.7, 6.5, 4.0]
        self.assertEqual(max_integer(lst), 6.5)

    def test_float_int(self):
        """List with floats and ints"""
        lst = [-3.1, 7, 7.5, 4]
        self.assertEqual(max_integer(lst), 7.5)

    def test_strings(self):
        """List of strings"""
        lst = ["John", "Doe", "Julien", "Barbier"]
        self.assertEqual(max_integer(lst), "Julien")

    def test_string(self):
        """String"""
        string = "John"
        self.assertEqual(max_integer(string), 'o')

    def test_empty_string(self):
        """Empty string"""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
