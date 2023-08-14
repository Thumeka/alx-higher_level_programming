#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for n in r:
            print("{}".format(n), end="\t")
        print()
