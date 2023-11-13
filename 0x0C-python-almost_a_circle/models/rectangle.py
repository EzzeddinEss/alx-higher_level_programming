#!/usr/bin/python3
"""a Model for subclass rectangle"""
from models.base import Base


class Rectangle(Base):
    """ A sub Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.validate_integer("width", value, False)
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.validate_integer("height", value, False)
            self.__height = value

        @property
        def x(self):
            return self.x

        @x.setter
        def x(self, value):
            self.validate_integer("x", value)
            self.__x = value

        @property
        def y(self):
            return self.y

        @y.setter
        def y(self, value):
            self.validate_integer("y", value)
            self.__y = value

        def validate_integer(self, name, value, equal=True):
            """a method to validate all setter"""
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if not equal and value <= 0:
                raise ValueError("{} must be > 0".format(name))
            if equal and value < 0:
                raise ValueError("{} must be >= 0".format(name))
