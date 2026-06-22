#!/usr/bin/python3
"""Module for defining a Square class.

This module provides a class representation of a geometric square,
including input validation for the private size attribute.
"""


class Square:
    """A class that defines a square geometric shape."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size length of the square's sides.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
