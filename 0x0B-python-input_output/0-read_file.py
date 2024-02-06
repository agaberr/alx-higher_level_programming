#!/usr/bin/python3
"""
=============================
Module with the method read_file
=============================
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8)
    and prints it to stdout
    """

    with open(filename, "r", encoding="UTF-8") as file:
        print(file.read(), end="")
