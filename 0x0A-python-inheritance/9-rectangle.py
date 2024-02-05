#!/usr/bin/python3
"""
=============================
Module with the class Rectangle
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


class Rectangle(BaseGeometry):
    """sub class Rectangle"""

    def __init__(self, width, height):
        """
        initialization of object
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        informal string representation of the rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
