#!/usr/bin/python3
def remove_char_at(str, n):
    strans = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            strans += str[i]
    return strans