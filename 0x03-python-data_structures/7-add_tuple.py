#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    """
    add 2 tuples
    ...

    Parameters
    ----------
    tuple_a: 
        first tuple
    tuple_b:
        second tuple

    Return:
        a tuple with 2 integers:
            -The first element should be the addition
            of the first element of each argument
            -The second element should be the addition 
            of the second element of each argument
    """

    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0

    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
