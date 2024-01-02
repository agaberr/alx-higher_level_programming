#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        number = chr(i)
    else:
        number = chr(i - 32)
    print("{}".format(number), end="")
