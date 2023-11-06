#!/usr/bin/python3
"""Lookup Method"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
        obj (object): The obj to retrieve the attributes and methods.

    Returns:
        list: A list of strings representing the names of atts and meths.
    """
    return dir(obj)
