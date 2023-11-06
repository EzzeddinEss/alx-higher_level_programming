#!/usr/bin/python3
"""A class Model MyList"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """A Method that prints ascending sort List"""
        print(sorted(self))
