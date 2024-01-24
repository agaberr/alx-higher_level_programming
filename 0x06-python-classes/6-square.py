#!/usr/bin/python3
"""square module"""


class Square:
    """define square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor

        Args:
            size: length of square side
            position: position of square on gird
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter for position

        Raises:
            TypeError: if not tuple of size 2
        """
        return self.__position

    @position.setter
    def position(self, p):
        if (not isinstance(p, tuple) or
            len(p) != 2 or
            isinstance(p[0], int) or
            isinstance(p[0], int) or
            p[0] < 0 or p[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = p

    def area(self):
        """get area of the square"""

        return self.__size * self.__size

    def my_print(self):
        """print square using #"""

        if self.__size == 0:
            print()
            return

        [print() for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print()
