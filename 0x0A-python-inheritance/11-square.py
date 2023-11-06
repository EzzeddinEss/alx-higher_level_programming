#!/usr/bin/python3
"""BaseGeometry class model"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """
        Compute the area of the geometry.

        Raises:
            Exception: This method is not implemented.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the value as an integer.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """class constructor"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """Compute the area of the rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the rectangle description"""
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Class constructor"""
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """An area square method"""
        return (self.__size ** 2)    

    def __str__(self):
        """Return the square description"""
        return ('[Square] {}/{}'.format(self.__size, self.__size))
