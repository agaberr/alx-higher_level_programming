#!/usr/bin/python3
"""
=============================
Module with the class MyInt
=============================
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __new__(cls, *args, **kwargs):
        """
        create a new instance of the class
        """

        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """
        what was != is now ==
        """

        return int(self) != other

    def __ne__(self, other):
        """
        what was == is now !=
        """

        return int(self) == other
