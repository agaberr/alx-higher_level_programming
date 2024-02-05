#!/usr/bin/python3
"""
=============================
Module with the class BaseGeometry
=============================
"""


class BaseGeometry():
    """class BaseGeometry"""

    def area(self):
        """
        Raises an Exception with the
        message area() is not implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        method that validate value
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(value))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(value))
