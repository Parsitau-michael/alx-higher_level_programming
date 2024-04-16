#!/usr/bin/python3
"""This module represents a class object

"""


class BaseGeometry:
    """This is the class object.

    """
    def area(self):
        """this method raises an Exception: area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this method validates the value passed """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
