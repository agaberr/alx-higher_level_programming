#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    find all multiples of 2 in a list.
    ...

    Parameters
    ----------
    my_list: 
        List of integers

    Return:
        list with True if number divisible by 2
        False otherwise
    """

    divisible = []

    for num in my_list:
        if num % 2 == 0:
            divisible.append(True)
        else:
            divisible.append(False)
    
    return divisible
