#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    Print integers in list
    ...

    Parameters
    ----------
    my_list : 
        List of integers

    Return:
        None
    """

    for num in my_list:
        print('{:d}'.format(num))