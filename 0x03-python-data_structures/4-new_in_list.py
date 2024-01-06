#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    """
     replaces an element in a list at a 
     specific position without modifying the original list
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
        new_list modified
    """

    if idx >= len(my_list) or idx < 0:
        return my_list

    new_list = my_list.copy()
    new_list[idx] = element

    return new_list
