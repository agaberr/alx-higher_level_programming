import unittest
from max_integer import max_integer

class MaxInteger(unittest.TestCase):
    """Test max_integer func"""

    def test_normal(self):
        """regular test"""
        l = [1, 2, 3, 4, 5]
        result = max_integer(l)
        self.assertEqual(result, 5)

    def test_not_int(self):
        """non int in list"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty_list(self):
        """Empty list"""
        l = []
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_negative_number(self):
        """list of negative numbers"""
        l = [-2, -6, -1]
        result = max_integer(l)
        self.assertEqual(result, -1)

    def test_float_number(self):
        """float number in list"""
        l = [3, 4, 2.5]
        result = max_integer(l)
        self.assertEqual(result, 4)

    def test_not_list(self):
        """list is not of type list"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_one_val(self):
        """one value only in list"""
        l = [45]
        result = max_integer(l)
        self.assertEqual(result, 45)

    def test_same_number(self):
        """same number in list"""
        l = [8, 8, 8, 8, 8]
        result = max_integer(l)
        self.assertEqual(result, 8)

    def test_string(self):
        """string in list"""
        l = ["hi", "hello"]
        result = max_integer(l)
        self.assertEqual(result, None)

    def test_none(self):
        """list is None"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
