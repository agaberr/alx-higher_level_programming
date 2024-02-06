#!/usr/bin/python3
"""
=============================
Module with the method write_file
=============================
"""


def write_file(filename="", text=""):
    """
    function that writes a string to a text file (UTF8)
    and returns the number of characters written
    """

    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)

    return len(text)
