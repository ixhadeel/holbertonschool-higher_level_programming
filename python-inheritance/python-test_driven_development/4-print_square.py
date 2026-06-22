#!/usr/bin/python3
"""Module for printing a square.

This module provides a function `print_square` that prints a square
using the `#` character based on a given size.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: The size length of the square (must be an integer).

    Raises:
        TypeError: If size is not an integer, or if it's a float less than 0.
        ValueError: If size is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
