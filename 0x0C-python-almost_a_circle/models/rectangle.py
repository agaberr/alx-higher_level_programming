#!/usr/bin/python3
"""
=============================
Module with the class Rectangle
=============================
"""


from modles.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for class rectangle
        """

        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width
    
    @width.setter
    def width(self, val):
        self.__width = val


    @property
    def height(self):
        """width getter"""
        return self.height
    
    @height.setter
    def height(self, val):
        self.height = val

    @property
    def x(self):
        """width getter"""
        return self.x
    
    @x.setter
    def x(self, val):
        self.x = val


    @property
    def y(self):
        """width getter"""
        return self.y
    
    @y.setter
    def y(self, val):
        self.y = val
