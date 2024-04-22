#!/usr/bin/python3
"""
Class Student that defines a student by:
    - public instance attributes:
        - first_name
        - last_name
        - age
    - instantiation with def __init__(self, first_name, last_name, age):
    - public method def to_json(self, attrs=None): that retrieves a dictionary
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

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if (isinstance(attrs, list) and all(isinstance(item, str)
                                            for item in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self,
                                                                        key)}

        return self.__dict__
