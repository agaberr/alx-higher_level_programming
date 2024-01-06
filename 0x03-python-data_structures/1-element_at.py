#!/usr/bin/python3
def element_at(my_list, idx):
    """
    retrieves an element from a list like in C
    ...

    Parameters
    ----------
    my_list: 
        List of integers
    idx:
        index of element to retrieve

    Return:
        element in idx, otherwise None
    """

    if(idx >= len(my_list) or idx < 0):
        return None

    return my_list[idx]
