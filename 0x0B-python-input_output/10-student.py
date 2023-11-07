#!/usr/bin/python3
"""a class Student model"""


class Student:
    """Class representation"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.
        """
        if attrs is not None:
            if type(attrs) is not list:
                return self.__dict__
            else:
                myDict = {}
                for attr in attrs:
                    if type(attr) is not str or attr not in self.__dict__:
                        continue
                    myDict[attr] = self.__dict__[attr]
                return myDict
        else:
            return self.__dict__
