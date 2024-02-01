#!/usr/bin/python3
"""Rectangle Module"""

class Rectangle:
    """Rectangle class"""
    no_rectangles = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.no_rectangles += 1

    @property
    def width(self):
        """get width of  rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of  rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height of  rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set  height of  rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """calculate perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """string representation of rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """print string representation of rectangle (width, height)"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """constructor msg"""
        print("Bye rectangle...")
        Rectangle.no_rectangles -= 1
