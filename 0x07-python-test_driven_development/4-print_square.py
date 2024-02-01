#!/usr/bin/python3
""" module for printing square """

def print_square(size):
    """
        function that prints a square with the character #

        Args:
            size: size of square

        Raises:
            TypeError: if size not int
            ValueError: if size < 0
        
        Return:
            None
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for x in range(size):
            for y in range(size):
                print('#', end='')
            print()

if __name__ == '__main__':
        import doctest
        doctest.testfile("tests/4-print_square.txt")
