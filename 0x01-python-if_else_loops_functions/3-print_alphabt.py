#!/usr/bin/python3
for alphabet in range(97, 122 + 1):
    if alphabet != 101 and alphabet != 113:
        print("{}".format(chr(alphabet)), end="")
