#!/usr/bin/python3
"""a function that creates an Object from a JSON file rep"""


import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as myFile:
        return json.load(myFile)
