#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beginning(self):
        """Test a list where the max value is at the beginning."""
        max_first = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_first), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertIsNone(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with only one element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of float numbers."""
        floats = [1.53, 6.33, -9.12, 4.8]
        self.assertEqual(max_integer(floats), 6.33)

    def test_ints_and_floats(self):
        """Test a list containing both integers and floats."""
        mixed = [1, 2.5, 3, 4.5]
        self.assertEqual(max_integer(mixed), 4.5)

    def test_negative_numbers(self):
        """Test a list with only negative numbers."""
        negatives = [-1, -5, -10, -2]
        self.assertEqual(max_integer(negatives), -1)


if __name__ == '__main__':
    unittest.main()
