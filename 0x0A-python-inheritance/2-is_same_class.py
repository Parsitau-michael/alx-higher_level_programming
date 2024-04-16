#!/usr/bin/python3
"""This module represents a function """


def is_same_class(obj, a_class):
    """This function checks whether obj
    is an instance of a_class"""
    if type(obj) is a_class:
        return True
    else:
        return False
