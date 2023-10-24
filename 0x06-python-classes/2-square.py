#!/usr/bin/python3
""" This module defines a Square class """


class Square:
    """ A class that represents a square. """

    def __init__(self, size=0):
        """Initializer
        arguments:
            size: the size of square
        raise:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an intger")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
