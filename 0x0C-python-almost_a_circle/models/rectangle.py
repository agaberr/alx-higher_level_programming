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

        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """
        height getter
        """

        return self.__height
    
    @height.setter
    def height(self, val):

        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        """
        x getter
        """

        return self.__x
    
    @x.setter
    def x(self, val):

        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """
        y getter
        """

        return self.__y
    
    @y.setter
    def y(self, val):

        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        """
        return area of rectangle
        """

        return self.__width * self.__height

    def display(self):
        """
        display rectangle using #
        """

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print("{}{}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        update values of each attribute
        """

        if (len(args) > 0):
            try:
                self.id = args[0]
            except IndexError:
                pass

            try:
                self.width = args[1]
            except IndexError:
                pass

            try:
                self.height = args[2]
            except IndexError:
                pass

            try:
                self.x = args[3]
            except IndexError:
                pass

            try:
                self.y = args[4]
            except IndexError:
                pass
        
        else:
            args_list = ["id", "width", "height", "x", "y"]
    
            for attributes in args_list:
                if attributes in kwargs:
                    if attributes == "id":
                        self.id = kwargs[attributes]
                    if attributes == "width":
                        self.width = kwargs[attributes]
                    if attributes == "height":
                        self.height = kwargs[attributes]
                    if attributes == "x":
                        self.x = kwargs[attributes]
                    if attributes == "y":
                        self.y = kwargs[attributes]

                else:
                    pass

    def to_dictionary(self):
        """
        Return dictionary representation
        """
        d = {}

        d['id'] = self.id
        d['width'] = self.width
        d['height'] = self.height
        d['x'] = self.x
        d['y'] = self.y
        return d
