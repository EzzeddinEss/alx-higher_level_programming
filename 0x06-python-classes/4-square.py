#!/usr/bin/python3
""" This module defines a Square class. """


class Square:
    """ A class that represents a square. """

    def __init__(self, size=0):
        """Initializer.

        Args:
            size: the size of square.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method to retrieve the size of the square.

            Raises:
                TypeError: if size is not an integer.
                ValueError: if size is less than zero.

        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('Size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
             The area of the square.
        """
        return self.__size ** 2
