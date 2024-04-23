#!/usr/bin/python3
"""This module represents a class"""


import json


class Base:
    """This is the Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        """this method initializes an instance of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method returns the json string representation of the obj"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation
        of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding="utf-8") as f:
            json_str = cls.to_json_string([obj.__dict__ for obj in list_objs])
            f.write(json_str)

    def from_json_string(json_string):
        """This method returns the list of the JSON string
        representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    def create(cls, **dictionary):
        """this method returns an instance with all attributes already set"""
