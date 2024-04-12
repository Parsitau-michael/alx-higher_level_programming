#!/usr/bin/python3
"""This module represents an add_integer function

Raises: TypeError: if a and b are neither floats nor integers

"""


def add_integer(a, b=98):
    """The function adds two integers and  returns the result.

    """

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    # casting floats into ints
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # now add the two
    return a + b
