#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    up = 0
    down = 0
    for val1, val2 in my_list:
        up += val1 * val2
        down += val2
    return up/down
