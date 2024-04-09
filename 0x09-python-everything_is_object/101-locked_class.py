#!/usr/bin/python3
"""
this module represents a class LockedClass
"""


class LockedClass:
    """
    this class is locked 
    it prevents the user from dynamically creating new instance attributes
    """
    __slots__ = ['first_name']
