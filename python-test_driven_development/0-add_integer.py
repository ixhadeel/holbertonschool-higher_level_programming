#!/usr/bin/python3
"""Module for adding two integers.

This module provides a simple function `add_integer` that takes two arguments,
casts them to integers if they are floats, and returns their sum.
"""


def add_integer(a, b=98):
    """Adds two integers or floats (casted to integers).

    Args:
        a: The first number, must be an int or float.
        b: The second number, must be an int or float. Defaults to 98.

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float, or if they
                   are NaN or Infinity.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # التحقق من حالات NaN و Infinity لمنع الـ Overflow والأخطاء الأخرى
    if a != a or a in (float('inf'), float('-inf')):
        raise TypeError("a must be an integer")
    if b != b or b in (float('inf'), float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
