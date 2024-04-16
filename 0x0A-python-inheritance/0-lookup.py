#!/usr/bin/python3
"""this module represents a function lookup. """


def lookup(obj):
    """This function returns a list of available attributes and methods of an object.

    It takes an object as an argument, returns a list of attributes and methods of the object.
    """
    return dir(obj)
