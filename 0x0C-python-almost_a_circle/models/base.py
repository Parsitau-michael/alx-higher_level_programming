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

    def to_json_string(list_dictionaries):
        """This method returns the json string representation 
        of list_dictionaries"""
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation
        of list_objs to a file"""
        with open(self.__name__.json, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write([])
            else:
                ret = to_json_string(list_objs)
                f.write(ret)

    def from_json_string(json_string):
        """This method returns the list of the JSON string
        representation json_string"""
        if json_string is None :
            return []
        else:
            return json.loads(json_string)
