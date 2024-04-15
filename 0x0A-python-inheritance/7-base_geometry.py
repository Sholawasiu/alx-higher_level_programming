#!/usr/bin/python3
"""
Class BaseGeometry based on 6-base_geometry.py
"""


class BaseGeometry(object):
    """
    Class BaseGeometry with an public instance method.
    """
    def area(self):
        """
        Public instance method not implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method to validate 'value'
        'name'  is always a string.

        Args:
            name: name of the object
            value: value of the attribute
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
