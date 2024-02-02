#!/usr/bin/python3
""" module for addition """

def add_integer(a, b=98):

    """
        Add two numbers

        Args:
            a: first number
            b: second number

        Raises:
            TypeError: if not integers or float
        
        Return:
            a + b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)


if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
