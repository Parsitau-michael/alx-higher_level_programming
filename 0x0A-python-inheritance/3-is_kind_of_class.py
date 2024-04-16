#!/usr/bin/python3
"""this module represents a function"""


def is_kind_of_class(obj, a_class):
    """This function checks whether an object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
