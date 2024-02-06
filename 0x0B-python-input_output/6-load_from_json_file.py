#!/usr/bin/python3
"""
=============================
Module with the method load_from_json_file
=============================
"""


import json


def load_from_json_file(filename):
    """
    Write a function that creates an Object
    from a “JSON file”
    """

    with open(filename, "w") as file:
        json_file = json.load(file)

    return json_file
