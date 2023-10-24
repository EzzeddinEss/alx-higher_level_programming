#!/usr/bin/python3
""" This module defines a Square class """



class Square:
    """ A class that represents a square. """

    def __init__(self, size=0):
        """
        Initializer

        Args:
        size :The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an intger")
        if size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = size
