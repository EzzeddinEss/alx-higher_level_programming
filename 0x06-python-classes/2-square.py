#!/usr/bin/python3
''' This module defines a Square class '''


class Square:
    """
    A class that represents a square.

    Attributes:
    size: The size of the square.

    Methods:
    __init__(self, size=0): Initializes a Square instance with the given size.

    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with the given size.

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
        self.size = size
