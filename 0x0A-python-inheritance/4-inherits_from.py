#!/usr/bin/python3
"""This module represents a function. 

"""


def inherits_from(obj, a_class):
    """the function checks whether an object is an instance
    of a class that inherited from the specified class.

    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
