#!/usr/bin/python3
"""This is a function module"""


import json


def load_from_json_file(filename):
    """The function creates an object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
