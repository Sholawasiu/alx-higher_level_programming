#!/usr/bin/python3
"""
Class Square that inherits from Rectangle based on 9-rectangle.py
(task based on 10-square.py)
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Python Inheritance
    Class Square that inherits from the base Class Rectangle.
    """
    def __init__(self, size):
        """
        Initialize private attribute size of the Class Rectangle.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        Public instance method that implements the area.
        """
        return super().area()

    def __str__(self):
        """
        Formatted a printable string representation.
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
