#!/usr/bin/python3
"""a func that writes an Obj to a txt file, using a JSON rep"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file using json"""
    with open(filename, 'w', encoding="utf-8")as myFile:
        json.dump(my_obj, myFile)
