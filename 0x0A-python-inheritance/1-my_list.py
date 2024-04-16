#!/usr/bin/python3
"""This module represents a Class Mylist object

MyList inherits from list
"""


class MyList(list):
    """This is a class MyList that inherits from list.

    """
    def print_sorted(self):
        """This class method sorts sorts a list passed
        to the class as an argument

        """
        sorted_list = sorted(self)
        print(sorted_list)
