#!/usr/bin/python3
import json
"""this module represents a function"""


def from_json_string(my_str):
    """this function returns an object represented by a JSON str"""
    return json.loads(my_str)
