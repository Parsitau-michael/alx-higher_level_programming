#!/usr/bin/python3
"""
this module is of a function that safely prits the values of a list
"""


def safe_print_list(my_list=[], x=0):
    """
    my_list - is a list that may contain any type.
    x - represents the number of  elements to print
    Return: the actual number printed.
    """
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
