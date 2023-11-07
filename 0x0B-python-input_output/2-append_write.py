#!/usr/bin/python3
"""A function that appends string to end of file"""


def append_write(filename="", text=""):
    """Function definition"""
    with open(filename, "a", encoding='utf-8') as myFile:
        return myFile.write(text)
