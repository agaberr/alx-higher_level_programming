#!/usr/bin/python3
"""square module"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """Constructor
        
        Args:
            size: length of square side

        Raises:
            TypeError: if size is not int
            ValueError: if size is < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
