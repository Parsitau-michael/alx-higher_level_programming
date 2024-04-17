#!/usr/bin/python3
"""this module represents a function"""


def read_file(filename=""):
    """this function opens a file and reads its content"""
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read())
