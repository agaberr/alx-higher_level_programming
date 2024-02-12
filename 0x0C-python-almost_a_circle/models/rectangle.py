#!/usr/bin/python3
"""
=============================
Module with the class Rectangle
=============================
"""


from .base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for class rectangle
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width getter
        """
        return self.__width
    
    @width.setter
    def width(self, val):
        self.__width = val


    @property
    def height(self):
        """
        height getter
        """
        return self.__height
    
    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def x(self):
        """
        x getter
        """
        return self.__x
    
    @x.setter
    def x(self, val):
        self.__x = val


    @property
    def y(self):
        """
        y getter
        """
        return self.__y
    
    @y.setter
    def y(self, val):
        self.__y = val
