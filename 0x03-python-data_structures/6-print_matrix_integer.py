#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        num = ' '.join(map(str,row))
        print('{}'.format(num))
