#!/usr/bin/python3
"""
An empty class defines a rectangle
"""


class Rectangle:
    """
    This class represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        """Rectangle initialization"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter for the Private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """a setter for the Private instance attribute width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter for the Private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """a setter for the Private instance attribute height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
