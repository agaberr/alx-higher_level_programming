#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    delete the item at a specific position in a list
    ...

    Parameters
    ----------
    my_list: 
        List of integers
    idx:
        index where number should be deleted
        
    Return:
        new_list after number is deleted
    """

    if idx >= len(my_list) or idx < 0:
        return my_list
    
    del my_list[idx]
    return my_list
