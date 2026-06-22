#!/usr/bin/python3
"""Module for defining a Square class.

This module provides a class representation of a geometric square,
handling private attributes for square instantiation.
"""


class Square:
    """A class that defines a square geometric shape."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size (int): The size length of the square's sides.
        """
        self.__size = size
