#!/usr/bin/python3
"""
=============================
Module with the class Square
=============================
"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        String representation
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
    
    @property
    def size(self):
        """
        size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

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

                self.size = args[1]
            except IndexError:
                pass

            try:

                self.x = args[2]
            except IndexError:
                pass

            try:

                self.y = args[3]
            except IndexError:
                pass

        else:
            args_list = ["id", "size", "x", "y"]

            for attributes in args_list:
                if attributes in kwargs:
                    if attributes == "size":
                        self.size = kwargs[attributes]
                    if attributes == "x":
                        self.x = kwargs[attributes]
                    if attributes == "y":
                        self.y = kwargs[attributes]
                    if attributes == "id":
                        self.id = kwargs[attributes]
                else:
                    pass
