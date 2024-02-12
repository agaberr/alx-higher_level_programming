#!/usr/bin/python3
"""
=============================
Module with the class Base
=============================
"""


class Base:
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base class constructor
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
