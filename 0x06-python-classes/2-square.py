#!/usr/bin/python3
""" This module defines a Square class """


class Square:
    """ A class that represents a square. """

    def __init__(self, size=0):
        """Initializer"""
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be greater than or equal to 0")
        self.__size = size
