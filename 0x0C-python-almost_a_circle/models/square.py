#!/usr/bin/python3
"""A model for a subclass that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a subclass from rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        '''class constructor'''
        super().__init__(id, x, y, size, size)

    def __str__(self):
        """Return a string representation of the square"""
        return '[{}] ({}) {}/{} - {}/{}'.format(
                type(self).__name__,
                self.id,
                self.x,
                self.y,
                self.width)
