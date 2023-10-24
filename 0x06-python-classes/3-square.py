#!/usr/bin/python3
""" This module defines a Square class. """


class Square:
    """ A class that represents a square. """

    def __init__(self, size=0):
        """Initializer.

        Args:
            size: the size of square.
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('Size must be >= 0')
        self.__size = size

    def area(self):
        """
        Calculates the area of the square.

        Returns:
             The area of the square.
        """
        return self.__size ** 2
