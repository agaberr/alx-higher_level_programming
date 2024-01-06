#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    """
    Prints a matrix of integers
    ...

    Parameters
    ----------
    matrix : 
        matrix of integers

    Return:
        None
    """

    for row in matrix:
        for col in row:
            print("{:d} ".format(col), end='')
        print()
