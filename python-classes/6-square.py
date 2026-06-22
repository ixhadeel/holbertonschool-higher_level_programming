#!/usr/bin/python3
"""Module for defining a Square class.

This module provides a class representation of a geometric square,
including size and position validation, area calculation, and custom printing.
"""


class Square:
    """A class that defines a square geometric shape."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size (int): The size length of the square's sides.
            position (tuple): The structural position coordinates of the square.
        """
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the private position attribute of the square.

        Returns:
            tuple: A tuple of two positive integers representing position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the private position attribute of the square with validation.

        Args:
            value (tuple): A tuple containing 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of exactly 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the current square area.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square instance using '#' with position spacing.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

