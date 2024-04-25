#!/usr/bin/python3
"""
Class Rectangle that inherits from Base class.
This class has:
    - private instance attribute width
    - private instance attribute height
    - private instance attribute x
    - private instance attribute y
    - class constructor def __init__(self, width, height, x=0, y=0, id=None):
"""
from models.base import Base


class Rectangle(Base):
    """
    Python Inheritance.
    Class Rectangle inherits from Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize private instance attributes."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Public method to compute the area of an Rectangle object."""
        return self.width * self.height

    def display(self):
        """Public method to print to the Rectangle instance with #."""
        char = "#"
        # line = ''
        # for _ in range(self.width):
        #     line += char
        # for _ in range(self.height):
        #     print(line)
        rectangle = self.y * "\n"
        for _ in range(self.height):
            rectangle += " " * self.x
            rectangle += (char * self.width) + "\n"

        print(rectangle, end="")

    def __str__(self):
        """Special method to print a custom string of a rectangle object."""
        # [Rectangle] (<id>) <x>/<y> - <width>/<height>
        string_start = "[Rectangle] "
        string_id = "({}) ".format(self.id)
        string_xy = "{}/{} - ".format(self.x, self.y)
        string_wh = "{}/{}".format(self.width, self.height)

        return string_start + string_id + string_xy + string_wh

    def update(self, *args, **kwargs):
        """Public method to assign an argument to each attribute."""
        if args is not None and len(args) != 0:
            list_attr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_attr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle. """
        return ({'x': self.x, 'y': self.y, 'id': self.id, 'height':
                 self.height, 'width': self.width})
