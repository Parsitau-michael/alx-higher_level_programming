#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    func = lambda x : x ** 2
    new_mat = []
    for row in matrix:
        new_row = list(map(func, row))
        new_mat.append(new_row)
    return new_mat
