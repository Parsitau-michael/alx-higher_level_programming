#!/usr/bin/python3
"""This module represents a class object"""


class Student:
    """This class represents student objects"""
    def __init__(self, first_name, last_name, age):
        """This method initializes a new instance of class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public method that retrieves a dictionary
        representation of a Student instance"""
        if attrs is not None:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
