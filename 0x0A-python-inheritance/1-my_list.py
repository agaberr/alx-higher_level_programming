#!/usr/bin/python3
"""
=============================
Module with the class MyList
=============================
"""


class MyList(list):
    """Class My list inherits from list"""
    def __init__(self):
        """initializes the object"""

        super().__init__()

    def print_sorted(self):
        """method that sort a list ascending order"""

        print(sorted(list(self)))
