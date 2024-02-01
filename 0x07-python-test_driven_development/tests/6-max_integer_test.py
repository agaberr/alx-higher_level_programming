#!/usr/bin/python3
"""Unittest formaxInteger module"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxInteger(unittest.TestCase):
    """Test max_integer func"""

    def normal(self):
        """regular test"""
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def not_int(self):
        """non int in list"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def empty_list(self):
        """Empty list"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def negative_number(self):
        """list of negative numbers"""
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def float_number(self):
        """float number in list"""
        l = [3, 4.5, 2]
        result = max_integer(l)
        self.assertEqual(result, 4.5)

    def not_list(self):
        """list is not of type list"""
        self.assertRaises(TypeError, max_integer, 7)

    def one_val(self):
        """one value only in list"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def same_number(self):
        """same number in list"""
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def string(self):
        """string in list"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, "hi")

    def none(self):
        """list is None"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
