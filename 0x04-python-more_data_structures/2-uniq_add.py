#!/usr/bin/python3
def uniq_add(my_list=[]):
    obj = set(my_list)
    summ = 0
    for elements in obj:
        summ += elements
    return summ
