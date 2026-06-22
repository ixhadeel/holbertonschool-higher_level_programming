#!/usr/bin/python3
"""Module for defining a Square class.

This module provides a class representation of a geometric square,
including property getters/setters, area calculation, and a print method.
"""


class Square:
    """A class that defines a square geometric shape."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size length of the square's sides.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the private size attribute of the square.

        Returns:
            int: The size length of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the private size attribute of the square with validation.

        Args:
            value (int): The new size length to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square instance to stdout using the '#' character.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
