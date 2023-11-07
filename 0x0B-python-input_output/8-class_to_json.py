#!/usr/bin/python3
"""Class to JSON Model"""


def class_to_json(obj):
    """ a function that returns the dictionary description with
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """
    return obj.__dict__
