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

    with open(filename, "r") as file:
        return json.load(file)
