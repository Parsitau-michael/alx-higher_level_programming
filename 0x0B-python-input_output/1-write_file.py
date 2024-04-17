#!/usr/bin/python3
"""this module represents a function"""


def write_file(filename="", text=""):
    """this function writes some text into a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
