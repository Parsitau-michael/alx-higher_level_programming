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


class Rectangle(BaseGeometry):
    """This is the Rectangle class.
    It inherits from the class BaseGeometry
    """
    def __init__(self, width, height):
        """this method inializes width and height when the class is called.
        """
        super().__init__()
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """this is a Square class that inherits from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
