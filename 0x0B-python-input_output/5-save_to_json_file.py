#!/usr/bin/python3
"""This is a function module"""


import json


def save_to_json_file(my_obj, filename):
    """The function serializes an object and saves it in a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
