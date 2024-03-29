#!/usr/bin/python3
"""
=============================
Module with the method inherits_from
=============================
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
