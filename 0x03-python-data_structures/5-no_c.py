#!/usr/bin/env python3
def no_c(my_string):

    """
     remove all characters c and C from a string
    ...

    Parameters
    ----------
    my_string : 
        input string

    Return:
        new_string
    """

    new_string = ""
    for c in my_string:
        if c not in "cC":
            new_string += c

    return new_string
