#!/usr/bin/python3
"""
=============================
Module with the class Rectangle
=============================
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
