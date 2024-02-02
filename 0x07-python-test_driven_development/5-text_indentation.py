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
        for delim in "?:.":
            txt = (delim + "\n\n").join([index.strip(" ") for index in txt.split(delim)])
            
if __name__ == '__main__':
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
