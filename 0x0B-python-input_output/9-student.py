#!/usr/bin/python3
"""
Class Student that defines a student by:
    - public instance attributes:
        - first_name
        - last_name
        - age
    - instantiation with def __init__(self, first_name, last_name, age):
    - public method def to_json(self): that retrieves a dictionary
      representation of a Student instance.
"""


class Student:
    """
    Class Student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        return self.__dict__
