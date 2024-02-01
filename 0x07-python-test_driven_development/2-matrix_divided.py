#!/usr/bin/python3
""" module for dividing a matrix """

def matrix_divided(matrix, div):
    """
        Divide all elements of a matrix.

        Args:
            matrix: matrix entered
            div: number to divide elements of matrix by

        Raises:
            TypeError: if matrix elements not integers or float
            TypeError: if matrix rows are not the same size
            TypeError: if div is not integer or float
            ZeroDivisionError: if div equal 0
        
        Return:
            matrix after division
    """
    if not matrix:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif type(div) not in (int, float):
        raise TypeError('div must be a number')
    elif not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    elif len(set(len(row) for row in matrix)) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    else:
        new_mat = [[round(element/div, 2) for element in row] for row in matrix]
    return new_mat 


if __name__ == '__main__':
        import doctest
        doctest.testfile("tests/2-matrix_divided.txt")
