#!/usr/bin/python3
"""A model for a subclass that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a subclass from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square"""
        return '[{}] ({}) {}/{} - {}'.format(
                type(self).__name__,
                self.id,
                self.x,
                self.y,
                self.width)

    @property
    def size(self):
        """Getter for the size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def __update(self, id=None, size=None, x=None, y=None):
        """Assigns arguments to each attribute."""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
