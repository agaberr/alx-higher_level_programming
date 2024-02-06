#!/usr/bin/python3
"""
=============================
Module with the method class_to_json
=============================
"""


import json


def class_to_json(obj):
    """
    function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object
    """
    return vars(obj)
