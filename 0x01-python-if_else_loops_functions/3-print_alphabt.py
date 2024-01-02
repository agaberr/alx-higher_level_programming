#!/usr/bin/python3
for alphabet in range('a', 'z' + 1):
    if alphabet != 'q' and alphabet != 'e':
        print("{}".format(chr(alphabet)), end="")
