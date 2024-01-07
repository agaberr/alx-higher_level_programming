#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    find the biggest integer of a list
    ...

    Parameters
    ----------
    my_list: 
        List of integers

    Return:
        max element in list, otherwise return None
    """

    if len(my_list) <= 0:
        return None
    
    max = -999
    for num in my_list:
        if num > max:
            max = num

    return max
