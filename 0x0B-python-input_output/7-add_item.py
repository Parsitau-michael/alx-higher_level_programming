#!/usr/bin/python3
"""This module represents a python script"""


from sys import argv
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# Get the commandline argument(s)
argument = argv[1:]

# Load existing list from the file 
if exists("add_item.json"):
    existing = load_from_json_file("add_item.json")
else:
    existing = []

# Adding the new arguments to the existing list
existing.extend(argument)

# Save to the .json file
save_to_json_file(existing, "add_item.json")
