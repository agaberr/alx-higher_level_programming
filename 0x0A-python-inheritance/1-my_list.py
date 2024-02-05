#!/usr/bin/python3
"""
=============================
Module with the class MyList
=============================
"""


class MyList(list):
    """Class My list inherits from list"""
    pass

    def print_sorted(self):
        """method that sort a list ascending order"""

        print(sorted(list(self)))
