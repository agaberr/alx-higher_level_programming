#!/usr/bin/python3
""" module for printing name """

def say_my_name(first_name, last_name=""):
    """
        function that prints My name is <first name> <last name>

        Args:
            first_name
            last_name

        Raises:
            TypeError: if first and last names are not string
        
        Return:
            None
    """
    if not isinstance(first_name, str) or not isinstance(first_name, str):
        raise TypeError('first_name must be a string or last_name must be a string')
    else:
        print('My name is {} {}'.format(first_name, last_name))
    
if __name__ == '__main__':
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
