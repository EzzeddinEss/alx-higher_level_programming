#!/usr/bin/python3
"""A Model for inherits_form Method"""


def inherits_from(obj, a_class):
    """A Method to check directly or indirect inheritance of a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
