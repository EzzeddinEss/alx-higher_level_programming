#!/usr/bin/python3
""" A function that reads file definition"""


def read_file(filename=""):
    """Function Definition"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end="")
