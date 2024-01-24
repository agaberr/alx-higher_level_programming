#!/usr/bin/python3
"""square module"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """Constructor

        Args:
            size: length of square side
        """
        self.__size = size

    @property
    def size(self):
        """getter for size

        Raises:
            TypeError: if size is not int
            ValueError: if size is < 0
        """
        return self.__size

    @size.setter
    def size(self, s):
        if not isinstance(s, int):
            raise TypeError("size must be an integer")
        if s < 0:
            raise ValueError("size must be >= 0")
        self.__size = s

    def area(self):
        """get area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """print square using #"""

        if self.__size == 0:
            print()
        else:
            for i in range (self.__size):
                print("#" * self.__size)
