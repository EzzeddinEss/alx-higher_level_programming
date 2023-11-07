#!/usr/bin/python3
"""a function that returns an object definition"""


import json


def from_json_string(my_str):
    """object represented by a JSON string function"""
    return json.loads(my_str)
