#!/usr/bin/python3
"""this module represents a function"""


def append_write(filename="", text=""):
    """this function appends some text to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
