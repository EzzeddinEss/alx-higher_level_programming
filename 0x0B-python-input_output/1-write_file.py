#!/usr/bin/python3
"""A function that write to a txt file"""


def write_file(filename="", text=""):
    """Function definition"""
    with open(filename, "w", encoding='utf-8') as myFile:
        return myFile.write(text)
