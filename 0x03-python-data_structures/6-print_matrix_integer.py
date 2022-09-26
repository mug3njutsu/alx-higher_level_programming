#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for num_list in matrix:
        print(int(" ".join([str(a) for a in num_list])))
