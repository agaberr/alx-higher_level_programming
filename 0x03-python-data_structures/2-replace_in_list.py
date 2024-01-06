#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    """
    replace an element of a list at a specific position
    ...

    Parameters
    ----------
    my_list: 
        List of integers
    idx:
        index of element to retrieve
    element:
        element to replace

    Return:
        my_list
    """

    if idx >= len(my_list) or idx < 0:
        return my_list

    my_list[idx] = element

    return my_list
