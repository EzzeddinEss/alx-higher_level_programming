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
        """Getter for the Private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the Private instance attribute width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the Private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the Private instance attribute height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        rect_str = ""
        if self.__width != 0 and self.__height != 0:
            for idx in range(self.__height):
                rect_str += "#" * self.__width
                if idx != self.__height - 1:
                    rect_str += "\n"
        return rect_str

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when the object is deleted"""
        print("Bye rectangle...")
