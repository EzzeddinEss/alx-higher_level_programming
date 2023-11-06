#!/usr/bin/python3
"""Lookup Method"""

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
        obj (object): The object for which to retrieve the attributes and methods.

    Returns:
        list: A list of strings representing the names of the available attributes and methods.
    """
    return dir(obj)
