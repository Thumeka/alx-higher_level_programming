#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    squared_matrix = [[value ** 2 for value in row] for row in matrix]
    return squared_matrix
