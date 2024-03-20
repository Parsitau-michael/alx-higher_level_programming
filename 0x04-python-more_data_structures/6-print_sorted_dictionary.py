#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    skeys = sorted(a_dictionary.keys())
    for key in skeys:
        print('{}: {}'.format(key, a_dictionary[key]))
