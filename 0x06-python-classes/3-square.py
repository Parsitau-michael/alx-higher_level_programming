#!/usr/bin/python3
"""
This module is a Square class.
"""


class Square:
    """
    this is the square class
    Size is a private class attribute
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
