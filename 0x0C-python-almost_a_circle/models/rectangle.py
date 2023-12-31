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
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

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

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle with '#' characters"""
        string = '\n' * self.y
        line = ' ' * self.x + '#' * self.width + '\n'
        string += line * self.height
        print(string, end="")

    def __str__(self):
        """Return a string representation of the rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.format(
                type(self).__name__,
                self.id,
                self.x,
                self.y,
                self.width,
                self.height)

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Assigns arguments to each attribute."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
