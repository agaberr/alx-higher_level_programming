#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    """
    Print integers of a list, in reverse order.
    ...

    Parameters
    ----------
    my_list : 
        List of integers

    Return:
        None
    """

    for num in reversed(my_list):
        print("{:d}".format(num))
