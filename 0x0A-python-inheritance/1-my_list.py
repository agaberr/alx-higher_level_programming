#!/usr/bin/python3
"""
=============================
Module with the class MyList
=============================
"""


class MyList(list):

    """Class My list inherits from list"""

    def print_sorted(self):
        """print sorted list in ascending order"""
        print(sorted(self))
