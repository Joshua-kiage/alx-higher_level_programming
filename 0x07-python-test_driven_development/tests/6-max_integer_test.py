#!/usr/bin/python3
"""
Unittests for max_integer function
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class containing unittests for max_integer function
    """

    def test_empty_list(self):
        """
        Test max_integer with an empty list
        """
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """
        Test max_integer with a list containing a single element
        """
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """
        Test max_integer with a list of positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([10, 20, 30, 40, 50]), 50)
        self.assertEqual(max_integer([100, 200, 300, 400, 500]), 500)

    def test_negative_numbers(self):
        """
        Test max_integer with a list of negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -40, -50]), -10)
        self.assertEqual(max_integer([-100, -200, -300, -400, -500]), -100)

    def test_mixed_numbers(self):
        """
        Test max_integer with a list of mixed positive and negative numbers
        """
        self.assertEqual(max_integer([-5, 0, 5, -10, 10]), 10)
        self.assertEqual(max_integer([-100, 0, 100, -200, 200]), 200)
        self.assertEqual(max_integer([-3, -2, 0, 2, 3]), 3)

    def test_float_numbers(self):
        """
        Test max_integer with a list of floating-point numbers
        """
        self.assertEqual(max_integer([1.5, 2.3, 3.7, 4.2, 5.9]), 5.9)
        self.assertEqual(max_integer([10.6, 20.4, 30.2, 40.8, 50.1]), 50.1)
        self.assertEqual(max_integer([100.9, 200.1, 300.5, 400.2, 500.7]), 500.7)

    def test_strings(self):
        """
        Test max_integer with a list of strings
        """
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")
        self.assertEqual(max_integer(["cat", "dog", "elephant"]), "elephant")
        self.assertEqual(max_integer(["one", "two", "three"]), "two")


if __name__ == '__main__':
    unittest.main()
