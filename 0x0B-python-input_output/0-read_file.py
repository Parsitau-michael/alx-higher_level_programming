#!/usr/bin/python3
"""this module represents a function"""


def read_file(filename=""):
    """ A function to read a textfile and print its content to stdout """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
