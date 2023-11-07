#!/usr/bin/python3
"""a script that adds all arguments to a Python list"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

args_list = list(sys.argv[1:])

try:
    existing_list = load_from_json_file("add_item.json")
except Exception:
    existing_list = []

existing_list.extend(args_list)
save_to_json_file(existing_list, "add_item.json")
