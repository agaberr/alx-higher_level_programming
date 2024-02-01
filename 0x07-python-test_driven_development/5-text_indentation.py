#!/usr/bin/python3
""" module for printing text """

def text_indentation(text):
    """
        function that prints a text with 2 new lines after each of these characters: ., ? and :

        Args:
            text: input txt

        Raises:
            TypeError: if txt is not string
        
        Return:
            None
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    else:
        for char in text:
            if char != ' ':
                if char not in ('.', '?', ':'):
                    print(char, end='')
                else:
                    print(char)
                    print()
            

if __name__ == '__main__':
        import doctest
        doctest.testfile("tests/5-text_indentation.txt")
