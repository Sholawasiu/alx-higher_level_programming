#!/usr/bin/python3
"""
Class Square that inherits from Rectangle class.
This class has:
    - private instance attribute width
    - private instance attribute height
    - private instance attribute x
    - private instance attribute y
    - class constructor def __init__(self, size, x=0, y=0, id=None):
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Python Inheritance.
    Class Square inherits from Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize instances from attributes of Rectangle class. """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """Special method to print a custom string of a square object."""
        # [Square] (<id>) <x>/<y> - <size>
        string_start = "[Square] "
        string_id = "({}) ".format(self.id)
        string_xy = "{}/{} - ".format(self.x, self.y)
        string_s = "{}".format(self.width)

        return string_start + string_id + string_xy + string_s

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) != 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):

        """ Returns the dictionary representation of a Square. """
        return ({'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y})
