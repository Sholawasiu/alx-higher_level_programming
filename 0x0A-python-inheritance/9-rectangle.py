#!/usr/bin/python3
"""
Class Rectangle that inherits from BaseGeometry based on 7-base_geometry.py
(task based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Python Inheritance
    Class Rectangle inherits from the base Class baseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialize private attributes of the Class Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Public instance method that implements the area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Formatted a printable string representation.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
